import argparse
import sys
from pathlib import Path
from typing import List, Tuple

from rdflib import BNode, Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS
from rdflib.query import ResultRow
from tabulate import tabulate

RDM_NAMESPACE_BASE_URI = "https://purl.org/rdm/ontology/"
XSD_NAMESPACE_BASE_URI = "http://www.w3.org/2001/XMLSchema#"


def parse_args(args: List[str]) -> Tuple[Path, Path]:
    parser = argparse.ArgumentParser(
        description="Convert RDF/Turtle to Markdown format."
    )
    parser.add_argument(
        "-t",
        "--turtle-file",
        type=str,
        help="The path to the RDF/Turtle file to convert. (default: ./ontology/RDM_ontology.ttl)",
        default="./ontology/RDM_ontology.ttl",
    )
    parser.add_argument(
        "-m",
        "--markdown-file",
        type=str,
        help="The path to the Markdown file to write. (default: ./frontend/README.md)",
        default="./frontend/README.md",
    )

    parsed_args = parser.parse_args(args)
    turtle_file_path = Path(parsed_args.turtle_file).resolve()
    markdown_file_path = Path(parsed_args.markdown_file).resolve()

    if not turtle_file_path.exists():
        raise FileNotFoundError(f"{turtle_file_path} does not exist.")

    return turtle_file_path, markdown_file_path


GENERATION_BOUNDARY = "<!-- The following is generated automatically -->"


def extract_manual_section(file_path: Path) -> List[str]:
    if not file_path.exists():
        return []
    manual_section = []
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(GENERATION_BOUNDARY):
                break
            manual_section.append(line.strip())

    return manual_section


def append_class(
    lines: List[str],
    rdm_namespace: Namespace,
    rdf_graph: Graph,
    class_name: str
) -> None:
    for class_ in rdf_graph.subjects(RDFS.subClassOf, rdm_namespace[class_name]):
        table_rows: List[Tuple[str, str]] = [("IRI", str(class_))]
        for predicate, object_ in rdf_graph.predicate_objects(class_):
            if predicate == RDFS.comment:
                table_rows.append((f"definition@{object_.language}", str(object_.value)))  # type: ignore
            if predicate == RDFS.seeAlso:
                table_rows.append(("seeAlso", str(object_.value)))  # type: ignore

        table_rows.append(("subClassOf", f"rdm:{class_name}"))
        lines.extend(["",
                      tabulate(table_rows, headers=["Class", str(class_).replace(RDM_NAMESPACE_BASE_URI, "")], tablefmt="github"),
                      ""])
        append_class(lines, rdm_namespace, rdf_graph, str(class_).replace(RDM_NAMESPACE_BASE_URI, ""))


def replace_uri(uri: str) -> str:
    if uri.startswith(RDM_NAMESPACE_BASE_URI):
        return uri.replace(RDM_NAMESPACE_BASE_URI, "rdm:")
    if uri.startswith(XSD_NAMESPACE_BASE_URI):
        return uri.replace(XSD_NAMESPACE_BASE_URI, "xsd:")

    return uri


UNION_QUERY_TEMPLATE = """
    SELECT ?elem
    {{
        rdm:{0} rdfs:{1} ?o .
        ?o owl:unionOf ?domain .
        ?domain rdf:rest*/rdf:first ?elem .
    }}
"""


def append_property(
    lines: List[str],
    rdm_namespace: Namespace,
    rdf_graph: Graph,
    predicate: URIRef,
    object_: URIRef
) -> None:
    for subject in rdf_graph.subjects(predicate, object_):
        subject_label = str(subject).replace(rdm_namespace, "")
        table_rows: List[Tuple[str, str]] = [("IRI", str(subject))]

        if object_.fragment == "":
            table_rows.append(("subPropertyOf", replace_uri(object_)))

        has_super_props = False

        for subject_predicate, subject_object in rdf_graph.predicate_objects(subject):
            if object_ in [OWL.DatatypeProperty, OWL.ObjectProperty] and subject_predicate == RDFS.subPropertyOf:
                # Exclude properties with super properties
                has_super_props = True
            if subject_predicate == RDFS.comment:
                table_rows.append((f"definition@{subject_object.language}", str(subject_object.value)))  # type: ignore
            if subject_predicate == OWL.inverseOf:
                table_rows.append(("inverseOf", replace_uri(str(subject_object))))

            if subject_predicate == RDFS.domain:
                domain_str = ""
                if isinstance(subject_object, BNode):
                    domains = []
                    for domain in rdf_graph.query(UNION_QUERY_TEMPLATE.format(subject_label, "domain")):
                        if isinstance(domain, ResultRow) and hasattr(domain, "elem"):
                            domains.append(replace_uri(domain.elem))
                    domain_str = ", ".join(domains)
                else:
                    domain_str = replace_uri(str(subject_object))
                table_rows.append(("domain", domain_str))

            if subject_predicate == RDFS.range:
                range_str = ""
                if isinstance(subject_object, BNode):
                    ranges = []
                    for range_ in rdf_graph.query(UNION_QUERY_TEMPLATE.format(subject_label, "range")):
                        if isinstance(range_, ResultRow) and hasattr(range_, "elem"):
                            ranges.append(replace_uri(range_.elem))
                    range_str = ", ".join(ranges)
                else:
                    range_str = replace_uri(str(subject_object))
                table_rows.append(("range", range_str))

            if subject_predicate == RDFS.seeAlso:
                table_rows.append(("seeAlso", str(subject_object.value)))  # type: ignore

        if not has_super_props:
            lines.extend(["",
                          tabulate(table_rows, headers=["Property", subject_label], tablefmt="github"),
                          ""])
            append_property(lines, rdm_namespace, rdf_graph, RDFS.subPropertyOf, rdm_namespace[subject_label])


SAME_AS_QUERY_TEMPLATE = """
    SELECT ?s
    {{
        ?s owl:sameAs rdm:{} .
    }}
"""


def append_name_individual(
    lines: List[str],
    rdf_graph: Graph,
) -> None:
    for subject in rdf_graph.subjects(RDF.type, OWL.NamedIndividual):
        if not str(subject).startswith(RDM_NAMESPACE_BASE_URI):
            continue
        table_rows: List[Tuple[str, str]] = [("IRI", str(subject))]
        for subject_predicate, subject_object in rdf_graph.predicate_objects(subject):
            if subject_predicate == RDF.type and str(subject_object).startswith(RDM_NAMESPACE_BASE_URI):
                table_rows.append(("type", replace_uri(str(subject_object))))
            if subject_predicate == RDFS.comment:
                table_rows.append((f"definition@{subject_object.language}", str(subject_object.value)))  # type: ignore
            if subject_predicate == OWL.sameAs:
                table_rows.append(("sameAs", str(subject_object.value)))  # type: ignore

        for same_as in rdf_graph.query(SAME_AS_QUERY_TEMPLATE.format(str(subject).replace(RDM_NAMESPACE_BASE_URI, ""))):
            if isinstance(same_as, ResultRow) and hasattr(same_as, "s"):
                table_rows.append(("sameAs", same_as.s))

        lines.extend(["",
                      tabulate(table_rows, headers=["Named Individual", str(subject).replace(RDM_NAMESPACE_BASE_URI, "")], tablefmt="github"),
                      ""])


def condense_empty_strings(lst: List[str]) -> List[str]:
    result = []
    previous_was_empty = False

    for item in lst:
        if item == "":
            if not previous_was_empty:
                result.append(item)
            previous_was_empty = True
        else:
            result.append(item)
            previous_was_empty = False

    return result


def main() -> None:
    turtle_file_path, markdown_file_path = parse_args(sys.argv[1:])
    rdm_namespace = Namespace(RDM_NAMESPACE_BASE_URI)
    rdf_graph = Graph()
    rdf_graph.parse(turtle_file_path, format="turtle")

    manual_section_lines = extract_manual_section(markdown_file_path)
    generate_section_lines = [GENERATION_BOUNDARY, ""]

    generate_section_lines.extend(["", "### Activity", ""])
    append_class(generate_section_lines, rdm_namespace, rdf_graph, "Activity")
    generate_section_lines.extend(["", "### Actor", ""])
    append_class(generate_section_lines, rdm_namespace, rdf_graph, "Actor")
    generate_section_lines.extend(["", "### Object", ""])
    append_class(generate_section_lines, rdm_namespace, rdf_graph, "Object")

    generate_section_lines.extend(["", "## Property", ""])
    generate_section_lines.extend(["", "### Datatype Property", ""])
    append_property(generate_section_lines, rdm_namespace, rdf_graph, RDF.type, OWL.DatatypeProperty)
    generate_section_lines.extend(["", "### Object Property", ""])
    append_property(generate_section_lines, rdm_namespace, rdf_graph, RDF.type, OWL.ObjectProperty)

    generate_section_lines.extend(["", "## Named Individual", ""])
    append_name_individual(generate_section_lines, rdf_graph)

    generate_section_lines = condense_empty_strings(generate_section_lines)
    lines = manual_section_lines + generate_section_lines

    with markdown_file_path.open("w", encoding="utf-8") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
