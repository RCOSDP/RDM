# Introduction
The Research Data Management Ontology (RDM Ontology) is developed to describe research data and all activities related to its management. RDM was developed as a communication hub between the NII Research Data Cloud (NII-RDC) systems, but is being developed as an ontology that can be applied to any research data management platform. The definition of Activity Class and its sub-classes in RDM Ontology is inspired by the Activity Streams 2.0 Terms, W3C Document 13 April 2018 (https://www.w3.org/ns/activitystreams#.) published by W3C.

# Objectives
The purpose of RDM Ontology is to represent the lifecycle of NII-RDC compliant research data as a metadata specification that can be described in RDF. The phases covered by RDM Ontology are the management, publication, discovery, and potentially future extraction phases that comprise the research data lifecycle.

# Namespace
https://purl.org/rdm/ontology#

## suggested prefix
rdm

# Deliverables
## Functional Requirements
- [Functional requirements specification](./userstories/list.md) <!-- 機能要件と対応するユーザーストーリー一覧へのリンク -->

## Domain Model
- RDM Ontology domain model <!-- データモデル図 -->

## Description Set Profile
- RDM Ontology <!-- 記述項目の一覧 -->
  - [turtle](./ontology/RDM_ontology.ttl)
  - [XML](./ontology/RDM_ontology.xml)
- RDM Ontology usage guidelines <!-- 記入方法、推奨例／非推奨例、注意点等 -->

## Syntax Encoding as Application Profile <!-- 各基盤／機能でのエンコーディング例 -->
- GakuNin RDM
- WEKO3
- CiNii Research
- Data Governance
- Code Package
- Data Curation

## Mappings <!-- 他のスキーマへのマッピング -->
- [Summary Document](./ontology/mapping/mapping_summary.md)
- Mapping the RDM Ontology to schema.org
  - [turtle](./ontology/mapping/mapping_to_schemaorg.ttl)
- Mapping the RDM Ontology to JPCOAR schema
  - [turtle](./ontology/mapping/mapping_to_jpcoar.ttl)

# Publications <!-- 関連出版物 -->
(Coming soon)

# License
[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). See [LICENSE](./LICENSE.txt) for more detail.
