from rdflib import BNode, Graph, Namespace, URIRef
from rdflib.namespace import  OWL, RDF, RDFS
from tabulate import tabulate

file_path:str = "frontend/README.md"
RDM_ns:str = "https://purl.org/rdm/ontology/"
XSD_ns:str = "http://www.w3.org/2001/XMLSchema#"

q ="""
          SELECT ?elem
  {{ rdm:{0} rdfs:{1} ?o .

  ?o owl:unionOf ?domain .

 ?domain rdf:rest*/rdf:first ?elem .
    }}"""

q_same_as ="""
          SELECT ?s
  {{ ?s owl:sameAs rdm:{} .

    }}"""


def replace_URI(uri:str) -> str:
  if uri.startswith(RDM_ns):
    return uri.replace(RDM_ns,"rdm:")
  elif uri.startswith(XSD_ns):
    return uri.replace(XSD_ns,"xsd:")

def add_class(base_text:str, cls_name:str) -> str:

  for cls in g.subjects(RDFS.subClassOf, RDM[cls_name]):
    data:list[tuple] =[]
    data.append(("IRI",cls))
    for p, o in g.predicate_objects(cls):
      if(p == RDFS.comment):
        data.append(("definition@"+o.language,o.value))
      if(p == RDFS.seeAlso):
        data.append(("seeAlso",o.value))

    data.append(("subClassOf","rdm:"+cls_name))
    base_text += "\n" + tabulate(data, headers=["Class",cls.replace(RDM_ns,"")], tablefmt="github") +"\n"
    base_text = add_class(base_text, cls.replace(RDM_ns,""))

  return base_text

def add_property(base_text:str, prop_s: URIRef, prop_o:URIRef ) -> str:

  for prop in g.subjects(prop_s, prop_o):
    prop_label:str = prop.replace(RDM_ns,"")
    data:list[tuple] =[]
    data.append(("IRI",prop))
    if prop_o.fragment =="":
      data.append(("subPropertyOf",replace_URI(prop_o)))

    for p, o in g.predicate_objects(prop):
      if (prop_o == (OWL.DatatypeProperty and OWL.ObjectProperty) and p == RDFS.subPropertyOf):
        data = []
        continue
      if(p == RDFS.comment):
        data.append(("definition@"+o.language,o.value))
      if(p == OWL.inverseOf):
        data.append(("inverseOf",replace_URI(o)))

      if (p == RDFS.domain):
        domain_str:str = ""
        if (isinstance(o, BNode)):
          for domain in g.query(q.format(prop_label,"domain")):
            domain_str += " ," + replace_URI(domain.elem)
          domain_str = domain_str[2:]
        else:
          domain_str = replace_URI(o)
        data.append(("domain", domain_str))

      if (p == RDFS.range):
        range_str:str = ""
        if (isinstance(o, BNode)):
          for range in g.query(q.format(prop_label,"range")):
            range_str += " ," + replace_URI(range.elem)
          range_str = range_str[2:]
        else:
          range_str = replace_URI(o)
        data.append(("range",range_str))

      if(p == RDFS.seeAlso):
        data.append(("seeAlso",o.value))

    if len(data) > 0 :
      base_text += "\n" + tabulate(data, headers=["Property",prop_label], tablefmt="github") +"\n"
      base_text = add_property(base_text, RDFS.subPropertyOf, RDM[prop_label])

  return base_text

def add_ni(base_text:str) -> str:

  for ni in g.subjects(RDF.type, OWL.NamedIndividual):
    if not ni.startswith(RDM_ns):
      continue
    data:list[tuple] =[]
    data.append(("IRI", ni))
    for p, o in g.predicate_objects(ni):
      if(p == RDF.type and o.startswith(RDM_ns)):
        data.append(("type",replace_URI(o)))
      if(p == RDFS.comment):
        data.append(("definition@"+o.language,o.value))
      if(p == OWL.sameAs):
        data.append(("sameAs",o.value))

    for same_as in g.query(q_same_as.format(ni.replace(RDM_ns,""))):
      data.append(("sameAs",same_as.s))
    base_text += "\n" + tabulate(data, headers=["Named Individual",ni.replace(RDM_ns,"")], tablefmt="github") +"\n"

  return base_text


if __name__ == "__main__":
  RDM:Namespace = Namespace(RDM_ns)
  g:Graph = Graph()
  g.parse("ontology/RDM_ontology.ttl",format="turtle")

  base_text:str = ""

  with open(file_path, "r", encoding="utf-8") as file:
    origin_text = file.read()
    target = "<!-- The following is generated automatically -->"
    idx = origin_text.find(target) + 50
    base_text += origin_text[:idx]

  base_text += "\n### Activity\n"
  base_text = add_class(base_text, "Activity")
  base_text += "\n### Actor\n"
  base_text = add_class(base_text, "Actor")
  base_text += "\n### Object\n"
  base_text = add_class(base_text, "Object")

  base_text += """## Property\n"""
  base_text += "\n### Datatype Property\n"
  base_text = add_property(base_text,RDF.type,OWL.DatatypeProperty)
  base_text += "\n### Object Property\n"
  base_text = add_property(base_text,RDF.type,OWL.ObjectProperty)

  base_text += """\n## Named Individual\n"""
  base_text += add_ni(base_text)

  with open(file_path, "w", encoding="utf-8") as file:
    file.write(base_text)
