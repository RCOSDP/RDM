# Domain Model
![Domain Model](DG_AP_domain_model.png)
The main entity is Project class in DG-AP domain model, unlike Resource and Activity class in RDM Ontology. This is because DG-AP supports only [Gakunin RDM](https://rdm.nii.ac.jp/) as a research data management platform for now. A project is base unit in Gakunin RDM and can exist without any files that is described by using Resource class. A instance of Project class in DG-AP indicates a single project of Gakunin RDM.


# Term Definitions Overview
|prefix|Namespace|
|--|--|
|dgap|https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#|
|rdm|https://purl.org/rdm/ontology/|
|owl|http://www.w3.org/2002/07/owl#|
|rdf|http://www.w3.org/1999/02/22-rdf-syntax-ns#|
|rdfs|http://www.w3.org/2000/01/rdf-schema#|
|xsd|http://www.w3.org/2001/XMLSchema#|

## New Vocabulary
||dgap:filePath|
|--|--|
|URI|https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#filePath|
|rdf:type|owl:DatatypeProperty|
|rdfs:subPropertyOf|rdm:localIdentifier|
|rdfs:comment|File path in Gakunin RDM.<br>Gakunin RDMにおけるファイルパス|
|rdfs:domain|rdm:Resource|
|rdfs:range|xsd:string|

||dgap:runCrate|
|--|--|
|URI|https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#runCrate|
|rdf:type|owl:DatatypeProperty|
|rdfs:comment|URL of a run-crate file in a project of Gakunin RDM<br>Gakunin RDM プロジェクト内にある run-crate ファイルの URL|
|rdfs:domain|rdm:Project|
|rdfs:range|xsd:string|

# Classes and Properties
## AccessRights
||rdm:AccessRights|
|--|--|
|URI|https://purl.org/rdm/ontology/AccessRights|
|rdfs:comment|Access rights.<br>アクセス権関連情報|

### Properties used with AccessRights Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:conditionOfAccess|rdm:ConditionOfAccessEnumeration|0..1|Access rights type.|Select from 4 types of ConditionOfAccessEnumeration.|
|rdm:dataAccessRequirements|csd:string|0..1|Conditions and method of access to the data under access restrictions.|The value is required when rdm:conditionOfAccess is rdm:RestrictedAccess.|
|rdm:dateAvailable|xsd:date or xsd:dateTime|0..1|A date the data becomes rdm:OpenAccess status.|The value is required when rdm:conditionOfAccess is rdm:EmbargoedAccess.|

## DataManagementPlan
||rdm:DataManagementPlan|
|--|--|
|URI|https://purl.org/rdm/ontology/DataManagementPlan|
|rdfs:comment|A data management plan (DMP).<br>データ管理計画(DMP)|

### Properties used with DataManagementPlan Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:approximateSize|xsd:string|0..1|Approximate size of the data to which this DataManagementPlan refers.||
|rdm:contact|xsd:string|0..1|A contact information for data management organizations and managers to be described in this DataManagementPlan.||
|rdm:dataAccessRightsInformation|rdm:AccessRights|0..1|An information of access rights of the data  to which this DataManagementPlan refers.||
|rdm:dataCreator|rdm:Person|0..*|A creator of the data to which this DataManagementPlan refers.||
|rdm:dataDescription|xsd:string|0..1|A description of the data to which this DataManagementPlan refers.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:dataEncodingFormat|xsd:string|0..*|A MIME format of the data to which this DataManagementPlan refers.||
|rdm:dataLicenseInformation|rdm:License|0..1|A license information of the data to which this DataManagementPlan refers.||
|rdm:dataManager|rdm:Person|0..*|A manager of the data to which this DataManagementPlan refers.||
|rdm:dataNumber|xsd:nonNegativeInteger|0..1|The data number assigned to this DataManagementPlan.||
|rdm:dmpFormat|xsd:string|0..1|A format name of this DataManagementPlan.||
|rdm:dmpFormatProvider|rdm:Institution|0..1|A institution which provides this DataManagementPlan format.||
|rdm:hostingInstitution|rdm:Institution|0..*|A hosting institution of the data to which this DataManagementPlan refers.||
|rdm:measurementTechnique|xsd:string|0..1|A technique, method or technology used to create the data to which this DataManagementPlan refers.||

## FundingAgency
||rdm:FundingAgency|
|--|--|
|URI|https://purl.org/rdm/ontology/FundingAgency|
|rdfs:subClassOf|rdm:Institution|
|rdfs:comment|An organization that funds research activities.<br>研究資金提供機関|

### Properties used with FundingAgency Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:address|xsd:string|0..*|An address of this FundingAgency.|The value MUST be either in Japanese or in English. When this property has multiple values, all values MUST be in the same language.<br>(additional usage notes compared to RDM-O) |
|rdm:funderId|xsd:string|0..1|Funder ID of this FundingAgency.||
|rdm:name|xsd:string|0..1|A name of this FundingAgency.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:ror|xsd:anyURI|0..1|ROR ID of this FundingAgency.||

## Grant
||rdm:Grant|
|--|--|
|URI|https://purl.org/rdm/ontology/Grant|
|rdfs:comment|A grant for research activities.<br>研究資金プログラム|

### Properties used with Grant Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:description|xsd:string|0..1|A description of this Grant.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:funder|rdm:FundingAgency|0..*|A funder of this Grant.||
|rdm:japanGrantNumber|xsd:string|0..1|Japan grant number(体系的課題番号) of this Grant.||
|rdm:name|xsd:string|0..1|A name of this Grant.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:url|xsd:anyURI|0..1|A url of this Grant.||

## Institution
||rdm:Institution|
|--|--|
|URI|https://purl.org/rdm/ontology/Institution|
|rdfs:comment|A organization or institution Person belongs to.<br>Person の所属先である組織または機関|

### Properties used with Institution Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:address|xsd:string|0..*|An address of this Institution.|The value MUST be either in Japanese or in English. When this property has multiple values, all values MUST be in the same language.<br>(additional usage notes compared to RDM-O)|
|rdm:name|xsd:string|0..1|A name of Institution.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:ror|xsd:anyURI|0..1|ROR ID of this Institution.||

## License
||rdm:License|
|--|--|
|URI|https://purl.org/rdm/ontology/License|
|rdfs:comment|A license of the data.<br>ライセンス情報|

### Properties used with License Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:copyright|xsd:string|0..*|A copyright note.||
|rdm:name|xsd:string|0..1|A name of this License.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:url|xsd:anyURI|0..1|A url of this License.||

## Person
||rdm:Person|
|--|--|
|URI|https://purl.org/rdm/ontology/Person|
|rdfs:comment|A user of Gakunin RDM or any other person related to a research project.<br>GRDMの1ユーザーもしくはその他研究関係者|

### Properties used with Person Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:affiliation|rdm:Institution|0..*|An affiliation of this Person.||
|rdm:email|xsd:string|0..*|An e-mail address of this Person.|||rdm:name|xsd:string|0..1|Person's full name.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:eradResearcherNumber|xsd:string|0..1| e-rad Researcher Number (e-Rad 研究者番号) of this Person.||
|rdm:name|xsd:string|0..1|Person's full name.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:orcid|xsd:anyURI|0..1|ORCID iD of this Person.||

## Project
||rdm:Project|
|--|--|
|URI|https://purl.org/rdm/ontology/Project|
|rdfs:comment|A Gakunin RDM project.<br>GRDM の 1 プロジェクト|

### Properties used with Project Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:accessRightsInformation|rdm:AccessRights|0..1|An information of access rights of this Project and Resources in it.||
|rdm:dateStarted|xsd:date or xsd:dateTime|0..1|A date this Project is created on GRDM.||
|rdm:description|xsd:string|0..1|A description of this Project.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:dmp|rdm:DataManagementPlan|0..*|A data management plan of this Project and Resources in it.||
|rdm:field|xsd:string|0..1|A field of this Project.|The value MUST be selected from filed value list.|
|rdm:funder|rdm:FundingAgency|0..*|A funder of this Project.||
|rdm:funding|rdm:Grant|0..*|A funding program and grant of this Project.||
|rdm:licenseInformation|rdm:License|0..1|A license information of this Project and Resources in it.||
|rdm:name|xsd:string|1|A name of this Project.|The value MUST be either in Japanese or in English ans is mandatory.<br>(additional usage notes compared to RDM-O)|
|rdm:projectItem|rdm:Resource|0..*|A Resource managed in this Project.||
|rdm:raid|xsd:string|0..1|RAiD of this Project.||
|rdm:researcher|rdm:Person|0..*|A researcher or participant of this Project.||
|dgap:runCrate|xsd:string|0..*|A run-crate file in this Project.||
|rdm:url|xsd:anyURI|1|URL of this Project.|This value MUST be a URL of GRDM, e.g. `https://rdm.nii.ac.jp/{project_id}`, and is mandatory.<br>(additional usage notes compared to RDM-O)|

## Resource
||rdm:Resource|
|--|--|
|URI|https://purl.org/rdm/ontology/Resource|
|rdfs:comment|A file managed in Gakunin RDM.<br>GRDMで管理されている1ファイル|

### Properties used with Resource Class
|Property|rdfs:range|Cardinality|Definition|Usage Note|
|--|--|--|--|--|
|rdm:creator|rdm:Person|0..*|A creator of this Resource.||
|rdm:dateCreated|xsd:date or xsd:dateTime|1|A date this Resource is created.|This value is mandatory<br>(additional usage notes compared to RDM-O)|
|rdm:dateModified|xsd:date or xsd:dateTime|0..1|A date this Resource is recently modified.||
|rdm:description|xsd:string|0..1|A description of this Resource.|The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)|
|rdm:dmp|rdm:DataManagementPlan|0..1|A data management plan of this Resources.||
|rdm:doi|xsd:anyURI|0..1|DOI of this Resource.||
|rdm:encodingFormat|xsd:string|0..1|A MIME format of this Resource.||
|dgap:filePath|xsd:string|0..1|A relative file path of this Resource in GRDM.||
|rdm:field|xsd:string|0..1|A field of this Resource.|The value MUST be selected from filed value list.|
|rdm:name|xsd:string|0..1|A file name.|The value can contain a file extension as well as the filename obtained from GRDM's API.<br>(additional usage notes compared to RDM-O)|
|rdm:sha256|xsd:string|0..1|A sha256 hash value.||
|rdm:size|xsd:string or xsd:nonNegativeInteger|0..1|A file size of this Resource.|When the value is in xsd:nonNegativeInteger, the unit is `B` as well as the file size obtained from GRDM's API.<br>(additional usage notes compared to RDM-O)|
|rdm:url|xsd:anyURI|1|URL of this Resource.|This value MUST be a URL of GRDM, e.g. `https://rdm.nii.ac.jp/{project_id}/files/{path}`, and is mandatory.<br>(additional usage notes compared to RDM-O)|
|rdm:version|xsd:string|1|A version of this Resource.|This value MUST be in xsd:string (not in xsd:nonNegativeInteger) and is mandatory.<br>(DG-AP specific extension)|
