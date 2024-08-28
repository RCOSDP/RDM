# Domain Model

![Domain Model](DG_AP_domain_model.png)
The main entity is Project class in DG-AP domain model, unlike Resource and Activity class in RDM Ontology. This is because DG-AP supports only [Gakunin RDM](https://rdm.nii.ac.jp/) as a research data management platform for now. A project is base unit in Gakunin RDM and can exist without any files that is described by using Resource class. A instance of Project class in DG-AP indicates a single project of Gakunin RDM.

# Example

- [JSON-LD](./DG_AP_example.json).

# Term Definitions Overview

| prefix | Namespace                                                                   |
| ------ | --------------------------------------------------------------------------- |
| dgap   | https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl# |
| rdm    | https://purl.org/rdm/ontology/                                              |
| owl    | http://www.w3.org/2002/07/owl#                                              |
| rdf    | http://www.w3.org/1999/02/22-rdf-syntax-ns#                                 |
| rdfs   | http://www.w3.org/2000/01/rdf-schema#                                       |
| xsd    | http://www.w3.org/2001/XMLSchema#                                           |

## New Vocabulary

|                    | dgap:filePath                                                                       |
| ------------------ | ----------------------------------------------------------------------------------- |
| URI                | https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#filePath |
| rdf:type           | owl:DatatypeProperty                                                                |
| rdfs:subPropertyOf | [rdm:localIdentifier](https://purl.org/rdm/ontology/localIdentifier)                |
| rdfs:comment       | File path in Gakunin RDM.<br>Gakunin RDM におけるファイルパス                       |
| rdfs:domain        | [rdm:Resource](https://purl.org/rdm/ontology/Resource)                              |
| rdfs:range         | xsd:string                                                                          |

|              | dgap:runCrate                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| URI          | https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#runCrate                              |
| rdf:type     | owl:DatatypeProperty                                                                                             |
| rdfs:comment | URL of a run-crate file in a project of Gakunin RDM<br>Gakunin RDM プロジェクト内にある run-crate ファイルの URL |
| rdfs:domain  | [rdm:Project](https://purl.org/rdm/ontology/Project)                                                             |
| rdfs:range   | xsd:string                                                                                                       |

# Classes and Properties

## AccessRights

|              | rdm:AccessRights                           |
| ------------ | ------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/AccessRights |
| rdfs:comment | Access rights.<br>アクセス権関連情報       |

### Properties used with AccessRights Class

| Property                                                                           | rdfs:range                                                           | Cardinality | Definition                                                             | Usage Note                                                                                                                                                                   |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rdm:conditionOfAccess](https://purl.org/rdm/ontology/conditionOfAccess)           | [rdm:RightsStatement](https://purl.org/rdm/ontology/RightsStatement) | 0..1        | Access rights type.                                                    | Select from 4 named individuals of RightsStatement.                                                                                                                          |
| [rdm:dataAccessRequirements](https://purl.org/rdm/ontology/dataAccessRequirements) | xsd:string                                                           | 0..1        | Conditions and method of access to the data under access restrictions. | The value is required when rdm:conditionOfAccess is rdm:RestrictedAccess.                                                                                                    |
| [rdm:dateAvailable](https://purl.org/rdm/ontology/dateAvailable)                   | xsd:date or xsd:dateTime                                             | 0..1        | A date the data becomes rdm:OpenAccess status.                         | The value is required when [rdm:conditionOfAccess](https://purl.org/rdm/ontology/conditionOfAccess) is [rdm:EmbargoedAccess.](https://purl.org/rdm/ontology/EmbargoedAccess) |

## DataManagementPlan

|              | rdm:DataManagementPlan                               |
| ------------ | ---------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/DataManagementPlan     |
| rdfs:comment | A data management plan (DMP).<br>データ管理計画(DMP) |

### Properties used with DataManagementPlan Class

| Property                                                                                     | rdfs:range                                                     | Cardinality | Definition                                                                                                       | Usage Note                                                                                        |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [rdm:approximateSize](https://purl.org/rdm/ontology/approximateSize)                         | xsd:string                                                     | 0..1        | Approximate size of the data to which this DataManagementPlan refers.                                            |                                                                                                   |
| [rdm:contact](https://purl.org/rdm/ontology/contact)                                         | xsd:string                                                     | 0..1        | A contact information for data management organizations and managers to be described in this DataManagementPlan. |                                                                                                   |
| [rdm:dataAccessRightsInformation](https://purl.org/rdm/ontology/dataAccessRightsInformation) | [rdm:AccessRights](https://purl.org/rdm/ontology/AccessRights) | 0..1        | An information of access rights of the data to which this DataManagementPlan refers.                             |                                                                                                   |
| [rdm:dataCreator](https://purl.org/rdm/ontology/dataCreator)                                 | [rdm:Person](https://purl.org/rdm/ontology/Person)             | 0..\*       | A creator of the data to which this DataManagementPlan refers.                                                   |                                                                                                   |
| [rdm:dataDescription](https://purl.org/rdm/ontology/dataDescription)                         | xsd:string                                                     | 0..1        | A description of the data to which this DataManagementPlan refers.                                               | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O) |
| [rdm:dataEncodingFormat](https://purl.org/rdm/ontology/dataEncodingFormat)                   | xsd:string                                                     | 0..\*       | A MIME format of the data to which this DataManagementPlan refers.                                               |                                                                                                   |
| [rdm:dataLicenseInformation](https://purl.org/rdm/ontology/dataLicenseInformation)           | [rdm:License](https://purl.org/rdm/ontology/License)           | 0..1        | A license information of the data to which this DataManagementPlan refers.                                       |                                                                                                   |
| [rdm:dataManager](https://purl.org/rdm/ontology/dataManager)                                 | [rdm:Person](https://purl.org/rdm/ontology/Person)             | 0..\*       | A manager of the data to which this DataManagementPlan refers.                                                   |                                                                                                   |
| [rdm:dataNumber](https://purl.org/rdm/ontology/dataNumber)                                   | xsd:nonNegativeInteger                                         | 0..1        | The data number assigned to this DataManagementPlan.                                                             |                                                                                                   |
| [rdm:dmpFormat](https://purl.org/rdm/ontology/dmpFormat)                                     | xsd:string                                                     | 0..1        | A format name of this DataManagementPlan.                                                                        |                                                                                                   |
| [rdm:dmpFormatProvider](https://purl.org/rdm/ontology/dmpFormatProvider)                     | [rdm:Institution](https://purl.org/rdm/ontology/Institution)   | 0..1        | A institution which provides this DataManagementPlan format.                                                     |                                                                                                   |
| [rdm:hostingInstitution](https://purl.org/rdm/ontology/hostingInstitution)                   | [rdm:Institution](https://purl.org/rdm/ontology/Institution)   | 0..\*       | A hosting institution of the data to which this DataManagementPlan refers.                                       |                                                                                                   |
| [rdm:measurementTechnique](https://purl.org/rdm/ontology/measurementTechnique)               | xsd:string                                                     | 0..1        | A technique, method or technology used to create the data to which this DataManagementPlan refers.               |                                                                                                   |

## FundingAgency

|                 | rdm:FundingAgency                                                   |
| --------------- | ------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/FundingAgency                         |
| rdfs:subClassOf | [rdm:Institution](https://purl.org/rdm/ontology/Institution)        |
| rdfs:comment    | An organization that funds research activities.<br>研究資金提供機関 |

### Properties used with FundingAgency Class

| Property                                               | rdfs:range | Cardinality | Definition                        | Usage Note                                                                                                                                                                         |
| ------------------------------------------------------ | ---------- | ----------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rdm:address](https://purl.org/rdm/ontology/address)   | xsd:string | 0..\*       | An address of this FundingAgency. | The value MUST be either in Japanese or in English. When this property has multiple values, all values MUST be in the same language.<br>(additional usage notes compared to RDM-O) |
| [rdm:funderId](https://purl.org/rdm/ontology/funderId) | xsd:string | 0..1        | Funder ID of this FundingAgency.  |                                                                                                                                                                                    |
| [rdm:name](https://purl.org/rdm/ontology/name)         | xsd:string | 0..1        | A name of this FundingAgency.     | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)                                                                                  |
| [rdm:ror](https://purl.org/rdm/ontology/ror)           | xsd:anyURI | 0..1        | ROR ID of this FundingAgency.     |                                                                                                                                                                                    |

## Grant

|              | rdm:Grant                                              |
| ------------ | ------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/Grant                    |
| rdfs:comment | A grant for research activities.<br>研究資金プログラム |

### Properties used with Grant Class

| Property                                                               | rdfs:range        | Cardinality | Definition                                        | Usage Note                                                                                        |
| ---------------------------------------------------------------------- | ----------------- | ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [rdm:description](https://purl.org/rdm/ontology/description)           | xsd:string        | 0..1        | A description of this Grant.                      | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O) |
| [rdm:funder](https://purl.org/rdm/ontology/funder)                     | rdm:FundingAgency | 0..\*       | A funder of this Grant.                           |                                                                                                   |
| [rdm:japanGrantNumber](https://purl.org/rdm/ontology/japanGrantNumber) | xsd:string        | 0..1        | Japan grant number(体系的課題番号) of this Grant. |                                                                                                   |
| [rdm:name](https://purl.org/rdm/ontology/name)                         | xsd:string        | 0..1        | A name of this Grant.                             | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O) |
| [rdm:url](https://purl.org/rdm/ontology/url)                           | xsd:anyURI        | 0..1        | A url of this Grant.                              |                                                                                                   |

## Institution

|              | [rdm:Institution](https://purl.org/rdm/ontology/Institution)                            |
| ------------ | --------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/Institution                                               |
| rdfs:comment | A organization or institution Person belongs to.<br>Person の所属先である組織または機関 |

### Properties used with Institution Class

| Property                                             | rdfs:range | Cardinality | Definition                      | Usage Note                                                                                                                                                                         |
| ---------------------------------------------------- | ---------- | ----------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rdm:address](https://purl.org/rdm/ontology/address) | xsd:string | 0..\*       | An address of this Institution. | The value MUST be either in Japanese or in English. When this property has multiple values, all values MUST be in the same language.<br>(additional usage notes compared to RDM-O) |
| [rdm:name](https://purl.org/rdm/ontology/name)       | xsd:string | 0..1        | A name of Institution.          | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)                                                                                  |
| [rdm:ror](https://purl.org/rdm/ontology/ror)         | xsd:anyURI | 0..1        | ROR ID of this Institution.     |                                                                                                                                                                                    |

## License

|              | rdm:License                              |
| ------------ | ---------------------------------------- |
| URI          | https://purl.org/rdm/ontology/License    |
| rdfs:comment | A license of the data.<br>ライセンス情報 |

### Properties used with License Class

| Property                                                 | rdfs:range | Cardinality | Definition              | Usage Note                                                                                        |
| -------------------------------------------------------- | ---------- | ----------- | ----------------------- | ------------------------------------------------------------------------------------------------- |
| [rdm:copyright](https://purl.org/rdm/ontology/copyright) | xsd:string | 0..\*       | A copyright note.       |                                                                                                   |
| [rdm:name](https://purl.org/rdm/ontology/name)           | xsd:string | 0..1        | A name of this License. | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O) |
| [rdm:url](https://purl.org/rdm/ontology/url)             | xsd:anyURI | 0..1        | A url of this License.  |                                                                                                   |

## Person

|              | rdm:Person                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/Person                                                                                   |
| rdfs:comment | A user of Gakunin RDM or any other person related to a research project.<br>GRDM の 1 ユーザーもしくはその他研究関係者 |

### Properties used with Person Class

| Property                                                                       | rdfs:range                                                   | Cardinality | Definition                                                 | Usage Note                                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [rdm:affiliation](https://purl.org/rdm/ontology/affiliation)                   | [rdm:Institution](https://purl.org/rdm/ontology/Institution) | 0..\*       | An affiliation of this Person.                             |                                                                                                   |
| [rdm:email](https://purl.org/rdm/ontology/email)                               | xsd:string                                                   | 0..\*       | An e-mail address of this Person.                          |                                                                                                   |
| [rdm:eradResearcherNumber](https://purl.org/rdm/ontology/eradResearcherNumber) | xsd:string                                                   | 0..1        | e-rad Researcher Number (e-Rad 研究者番号) of this Person. |                                                                                                   |
| [rdm:name](https://purl.org/rdm/ontology/name)                                 | xsd:string                                                   | 0..1        | Person's full name.                                        | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O) |
| [rdm:orcid](https://purl.org/rdm/ontology/orcid)                               | xsd:anyURI                                                   | 0..1        | ORCID iD of this Person.                                   |                                                                                                   |

## Project

|              | rdm:Project                                      |
| ------------ | ------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/Project            |
| rdfs:comment | A Gakunin RDM project.<br>GRDM の 1 プロジェクト |

### Properties used with Project Class

| Property                                                                                             | rdfs:range                                                                 | Cardinality | Definition                                                           | Usage Note                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [rdm:accessRightsInformation](https://purl.org/rdm/ontology/accessRightsInformation)                 | [rdm:AccessRights](https://purl.org/rdm/ontology/AccessRights)             | 0..1        | An information of access rights of this Project and Resources in it. |                                                                                                                                              |
| [rdm:dateStarted](https://purl.org/rdm/ontology/dateStarted)                                         | xsd:date or xsd:dateTime                                                   | 0..1        | A date this Project is created on GRDM.                              |                                                                                                                                              |
| [rdm:description](https://purl.org/rdm/ontology/description)                                         | xsd:string                                                                 | 0..1        | A description of this Project.                                       | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)                                            |
| [rdm:dmp](https://purl.org/rdm/ontology/dmp)                                                         | [rdm:DataManagementPlan](https://purl.org/rdm/ontology/DataManagementPlan) | 0..\*       | A data management plan of this Project and Resources in it.          |                                                                                                                                              |
| [rdm:field](https://purl.org/rdm/ontology/field)                                                     | xsd:string                                                                 | 0..1        | A field of this Project.                                             | The value MUST be selected from filed value list.                                                                                            |
| [rdm:funder](https://purl.org/rdm/ontology/funder)                                                   | [rdm:FundingAgency](https://purl.org/rdm/ontology/fundingAgency)           | 0..\*       | A funder of this Project.                                            |                                                                                                                                              |
| [rdm:funding](https://purl.org/rdm/ontology/funding)                                                 | [rdm:Grant](https://purl.org/rdm/ontology/Grant)                           | 0..\*       | A funding program and grant of this Project.                         |                                                                                                                                              |
| [rdm:licenseInformation](https://purl.org/rdm/ontology/licenseInformation)                           | [rdm:License](https://purl.org/rdm/ontology/License)                       | 0..1        | A license information of this Project and Resources in it.           |                                                                                                                                              |
| [rdm:name](https://purl.org/rdm/ontology/name)                                                       | xsd:string                                                                 | 1           | A name of this Project.                                              | The value MUST be either in Japanese or in English ans is mandatory.<br>(additional usage notes compared to RDM-O)                           |
| [rdm:projectItem](https://purl.org/rdm/ontology/projectItem)                                         | [rdm:Resource](https://purl.org/rdm/ontology/Resource)                     | 0..\*       | A Resource managed in this Project.                                  |                                                                                                                                              |
| [rdm:raid](https://purl.org/rdm/ontology/raid)                                                       | xsd:string                                                                 | 0..1        | RAiD of this Project.                                                |                                                                                                                                              |
| [rdm:researcher](https://purl.org/rdm/ontology/researcher)                                           | [rdm:Person](https://purl.org/rdm/ontology/Person)                         | 0..\*       | A researcher or participant of this Project.                         |                                                                                                                                              |
| [dgap:runCrate](https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#runCrate) | xsd:string                                                                 | 0..\*       | A run-crate file in this Project.                                    |                                                                                                                                              |
| [rdm:url](https://purl.org/rdm/ontology/url)                                                         | xsd:anyURI                                                                 | 1           | URL of this Project.                                                 | This value MUST be a URL of GRDM, e.g. `https://rdm.nii.ac.jp/{project_id}`, and is mandatory.<br>(additional usage notes compared to RDM-O) |

## Resource

|              | rdm:Resource                                                       |
| ------------ | ------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/Resource                             |
| rdfs:comment | A file managed in Gakunin RDM.<br>GRDM で管理されている 1 ファイル |

### Properties used with Resource Class

| Property                                                                                             | rdfs:range                                                                 | Cardinality | Definition                                     | Usage Note                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rdm:creator](https://purl.org/rdm/ontology/creator)                                                 | [rdm:Person](https://purl.org/rdm/ontology/Person)                         | 0..\*       | A creator of this Resource.                    |                                                                                                                                                               |
| [rdm:dateCreated](https://purl.org/rdm/ontology/dateCreated)                                         | xsd:date or xsd:dateTime                                                   | 1           | A date this Resource is created.               | This value is mandatory<br>(additional usage notes compared to RDM-O)                                                                                         |
| [rdm:dateModified](https://purl.org/rdm/ontology/dateModified)                                       | xsd:date or xsd:dateTime                                                   | 0..1        | A date this Resource is recently modified.     |                                                                                                                                                               |
| [rdm:description](https://purl.org/rdm/ontology/description)                                         | xsd:string                                                                 | 0..1        | A description of this Resource.                | The value MUST be either in Japanese or in English.<br>(additional usage notes compared to RDM-O)                                                             |
| [rdm:dmp](https://purl.org/rdm/ontology/dmp)                                                         | [rdm:DataManagementPlan](https://purl.org/rdm/ontology/DataManagementPlan) | 0..1        | A data management plan of this Resources.      |                                                                                                                                                               |
| [rdm:doi](https://purl.org/rdm/ontology/doi)                                                         | xsd:anyURI                                                                 | 0..1        | DOI of this Resource.                          |                                                                                                                                                               |
| [rdm:encodingFormat](https://purl.org/rdm/ontology/encodingFormat)                                   | xsd:string                                                                 | 0..1        | A MIME format of this Resource.                |                                                                                                                                                               |
| [dgap:filePath](https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#filePath) | xsd:string                                                                 | 0..1        | A relative file path of this Resource in GRDM. |                                                                                                                                                               |
| [rdm:field](https://purl.org/rdm/ontology/field)                                                     | xsd:string                                                                 | 0..1        | A field of this Resource.                      | The value MUST be selected from filed value list.                                                                                                             |
| [rdm:name](https://purl.org/rdm/ontology/name)                                                       | xsd:string                                                                 | 0..1        | A file name.                                   | The value can contain a file extension as well as the filename obtained from GRDM's API.<br>(additional usage notes compared to RDM-O)                        |
| [rdm:sha256](https://purl.org/rdm/ontology/sha256)                                                   | xsd:string                                                                 | 0..1        | A sha256 hash value.                           |                                                                                                                                                               |
| [rdm:size](https://purl.org/rdm/ontology/size)                                                       | xsd:string or xsd:nonNegativeInteger                                       | 0..1        | A file size of this Resource.                  | When the value is in xsd:nonNegativeInteger, the unit is `B` as well as the file size obtained from GRDM's API.<br>(additional usage notes compared to RDM-O) |
| [rdm:url](https://purl.org/rdm/ontology/url)                                                         | xsd:anyURI                                                                 | 1           | URL of this Resource.                          | This value MUST be a URL of GRDM, e.g. `https://rdm.nii.ac.jp/{project_id}/files/{path}`, and is mandatory.<br>(additional usage notes compared to RDM-O)     |
| [rdm:version](https://purl.org/rdm/ontology/version)                                                 | xsd:string                                                                 | 1           | A version of this Resource.                    | This value MUST be in xsd:string (not in xsd:nonNegativeInteger) and is mandatory.<br>(DG-AP specific extension)                                              |
