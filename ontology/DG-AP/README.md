# Abstract
The Data Governance Application Profile (DG-AP) is an application profile of Research Data Management Ontology (RDM Ontology) specialized to [Data Governance application](https://github.com/NII-DG/nii-dg-web), which can monitor the status of research data and its metadata. [Gakunin RDM](https://rdm.nii.ac.jp/), research data management platform, is necessary as a target of monitoring by DG application.

# Data Model
In DG-AP, root entity of metadata MUST be the instance of rdm:Project class because the monitoring scope of DG application is a single research project. 
DG-AP has minimal description of cardinality restrictions and required level. Most of these restriction depends on governance sheet, which is a rule set that is applied to monitoring by DG application.

# Namespace
https://github.com/RCOSDP/RDM/tree/main/ontology/DG-AP/dg_ap.ttl#

## suggested prefix
dgap

# Deliverables
## Domain Model
- DG-AP domain model <!-- データモデル図 -->

## Description Set Profile
- [turtle](./dg_ap.ttl)
- DG-AP usage guidelines <!-- 記入方法、推奨例／非推奨例、注意点等 -->
