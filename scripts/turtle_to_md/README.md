# turtle_to_md

This script converts a turtle file to a markdown file.

Basically, it is used to convert [RDM_ontology.ttl](../../ontology/RDM_ontology.ttl) to [README.md](../../frontend/README.md).

## Usage

```bash
python3 -m pip install .
turtle_to_md -t input.ttl -m output.md
```

Alternatively, if using Docker:

```bash
docker compose up -d --build
docker compose exec turtle_to_md turtle_to_md -t input.ttl -m output.md

# Since ../../ontology and ../../frontend are mounted in the container:
docker compose exec turtle_to_md turtle_to_md -t ./ontology/RDM_ontology.ttl -m ./frontend/README.md
```
