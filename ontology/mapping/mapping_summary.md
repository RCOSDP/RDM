# Mapping Summary
This document is a summary of mapping from the RDM Ontology to schema.org and JPCOAR.

## Used Namespace
|Prefix|Namespace URI|
|--|--|
|rdm||
|schema||
|jpcoar||

## Alignment to Schema.org
A recommended mapping from the RDM Ontology to [schema.org](https://schema.org/) version 26.0 is available in an [RDF file](). 

### Class
|RDM class|Target class from schema.org|comment|
|--|--|--|
|rdm:Person|schema:Person|
|rdm:Institution|schema:Organization|
|rdm:FundingAgency|schema:FundingAgency|
|rdm:SoftwareApplication|schema:SoftwareApplication|
|rdm:Resource|schema:MediaObject|
|rdm:Grant|schema:Grant|
|rdm:Repository|schema:CreativeWork|
|rdm:Project|schema:ResearchProject|
|rdm:DataManagementPlan|schema:CreativeWork|
|rdm:Collection|schema:Collection|
|rdm:Event|schema:Event|
|rdm:AccessRights|schema:DigitalDocumentPermission|
|rdm:License|schema:CreativeWork|
|rdm:Identifier|schema:PropertyValue|
|rdm:Audio|schema:AudioObject|
|rdm:Book|schema:Book|
|rdm:Dataset|schema:Dataset|
|rdm:Image|schema:ImageObject|
|rdm:JournalArticle|schema:ScholarlyArticle|
|rdm:Journal|schema:Periodical|
|rdm:Preprint|schema:ScholarlyArticle|
|rdm:Report|schema:Report|
|rdm:Thesis|schema:Thesis|
|rdm:Video|schema:VideoObject|
|rdm:Activity|schema:Action|
|rdm:Accept|schema:AcceptAction|
|rdm:Add|schema:AddAction|
|rdm:Ask|schema:AskAction|
|rdm:Assign|schema:AssignAction|
|rdm:Authorize|schema:AuthorizeAction|
|rdm:Check|schema:CheckAction|
|rdm:Comment|schema:CommentAction|
|rdm:Create|schema:CreateAction|
|rdm:Download|schema:DownloadAction|
|rdm:Inform|schema:InformAction|
|rdm:Register|schema:RegisterAction|
|rdm:Reject|schema:RejectAction|
|rdm:Schedule|schema:ScheduleAction|
|rdm:Search|schema:SearchAction|
|rdm:Select|schema:ChooseAction|
|rdm:Send|schema:SendAction|
|rdm:Update|schema:UpdateAction|
|rdm:Enumeration|schema:DefinedTerm|

### Property
|RDM property|Target property from schema.org|comment|
|--|--|--|
|rdm:address|schema:address|
|rdm:affiliation|schema:affiliation|
|rdm:agent|schema:agent|
|rdm:contributor|schema:contributor|
|rdm:creator|schema:creator|
|rdm:organizer|schema:organizer|
|rdm:copyright|schema:copyrightNotice|
|rdm:dateCreated|schema:dateCreated|
|rdm:dateEnded|schema:startDate|
|rdm:dateModified|schema:dateModified|
|rdm:datePublished|schema:datePublished|
|rdm:dateStarted|schema:endDate|
|rdm:sdDatePublished|schema:sdDatePublished|
|rdm:description|schema:description|
|rdm:operatingSystem|schema:operatingSystem|
|rdm:processorRequirements|schema:processorRequirements|
|rdm:softwareRequirements|schema:softwareRequirements|
|rdm:storageRequirements|schema:storageRequirements|
|rdm:detailedRole|schema:jobTitle|
|rdm:email|schema:email|
|rdm:encodingFormat|schema:encodingFormat|
|rdm:funder|schema:funder|
|rdm:funding|schema:funding|
|rdm:identifierInformation|schema:identifier|
|rdm:hasPart|schema:hasPart|
|rdm:isPartOf|schema:isPartOf|
|rdm:instrument|schema:instrument|
|rdm:keywords|schema:keywords|
|rdm:language|schema:inLanguage|
|rdm:licenseInformation|schema:license|
|rdm:name|schema:name|
|rdm:additionalName|schema:additionalName|
|rdm:familyName|schema:familyName|
|rdm:givenName|schema:givenName|
|rdm:rdm:object|schema:object|
|rdm:result|schema:result|
|rdm:size|schema:size|
|rdm:collectionSize|schema:collectionSize|
|rdm:thumbnail|schema:thumbnail|
|rdm:url|schema:url|
|rdm:value|schema:value|
|rdm:sha256|schema:sha256|
|rdm:version|schema:version|

## Alignment to JPCOAR
A recommended mapping from the RDM Ontology to [JPCOAR]() version 2.0 is available in an [RDF file](). 

### About JPCOAR Scheme

### Class
|RDM class|Target class from JPCOAR|comment|
|--|--|--|
||||


### Property
|RDM property|Target property from JPCOAR|comment|
|--|--|--|
||||
