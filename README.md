# Introduction

The Research Data Management ontology (RDM ontology) is developed to describe research data and all activities related to its management. RDM ontology was developed as a communication hub between the NII Research Data Cloud (NII-RDC) systems, but is being developed as an ontology that can be applied to any research data management platform. The domain model of RDM ontology is designed to comply with best practices regarding persistent identifiers. RDM ontology is also activity-centered in its design philosophy inspired by the Activity Streams 2.0, W3C Document 13 April 2018 (https://www.w3.org/ns/activitystreams#).

# Objectives

The purpose of the RDM Ontology is to represent the lifecycle of NII-RDC compliant research data as a metadata specification that can be described in RDF. The phases covered by RDM Ontology are the management, publication, discovery, and potentially future extraction phases that comprise the research data lifecycle.

# Namespace

https://purl.org/rdm/ontology/

## suggested prefix

rdm

# Deliverables

## Functional Requirements

- Functional requirements specification <!-- 機能要件と対応するユーザーストーリー一覧へのリンク -->
<!-- 追加 --> (Coming soon)

## Domain Model

The RDM Ontology is based on two data models: a standard data model used to describe resources, and Activity-focused data model used to describe user stories of research activities using RDM systems. See the link below for the actual data model diagram.

- RDM Ontology domain model <!-- データモデル図 -->
  - [focused on Resource](./docs/domain_model_Resource.png)
  - [focused on Activity](./docs/domain_model_Activity.png)

## Description Set Profile

The RDM Ontology is developed to describe items common to multiple applications of NII-RDC by comparing the schema definitions of these applications. Guidelines are also provided to expand the RDM Ontology aligning with specific application.

- RDM Ontology <!-- 記述項目の一覧 -->
  - [turtle](./ontology/RDM_ontology.ttl)
  - [RDF/XML](./ontology/RDM_ontology.xml)
  - [OWL/XML](./ontology/RDM_ontology.owl)
- [RDM Ontology usage guidelines](./docs/RDM_Ontology_usage_guidelines.md) <!-- 記入方法、推奨例／非推奨例、注意点等 -->
- [expansion guidelines](./docs/RDM_Ontology_expansion_guidelines.md)

## Syntax Encoding as Application Profile <!-- 各基盤／機能でのエンコーディング例 -->

The RDM Ontology can describe items that are fundamentally common to multiple applications of NII-RDC. Applications that wish to adopt the RDM Ontology but find it incomplete can first import the RDM Ontology and then add their own classes and vocabulary. The following are examples of extensions of RDM Ontology for each application of NII-RDC.

- GakuNin RDM
- WEKO3
- CiNii Research
- Data Governance
  - [DG-AP](./ontology/DG-AP/)
- Code Package
- Data Curation

## Mappings <!-- 他のスキーマへのマッピング -->

The following are mappings to schemas compatible with the RDM Ontology. Please note that the information in this section is updated based on the latest available data at the time of application, so be sure to check the version information of the target schema when using this information.

- [Summary Document](./ontology/mapping/mapping_summary.md)
- Mapping the RDM Ontology to schema.org
  - [turtle](./ontology/mapping/mapping_to_schemaorg.ttl)
- Mapping the RDM Ontology to JPCOAR schema
  - [turtle](./ontology/mapping/mapping_to_jpcoar.ttl)

# Publications <!-- 関連出版物 -->

1. Minamiyama, Y., Hayashi, M., Fujiwara, I., Onami, J., Yokoyama, S., Komiyama, Y., & Yamaji, K. (2023). Toward the Development of NII-RDC Application Profile Using Ontology Technology. In Proceedings of the Conference on Research Data Infrastructure (Vol. 1). TIB Open Publishing. https://doi.org/10.52825/cordi.v1i.260
2. 南山泰之, 林正治, 藤原一毅, 大波純一, 横山重俊, 込山悠介, 山地一禎 (2023). オントロジー技術を用いた NII-RDC アプリケーションプロファイル開発に向けて. 情報知識学会誌. Vol.33, No.2, p.212-220.
