# Mapping Summary
This document is a summary of mapping from the RDM Ontology to schema.org and JPCOAR.

## Used Namespace
|Prefix|Namespace URI|
|--|--|
|rdm|https://purl.org/rdm/ontology#|
|schema|https://schema.org/|
|jpcoar|https://github.com/JPCOAR/schema/blob/master/2.0/#|

## Alignment to Schema.org
A recommended mapping from the RDM Ontology to [schema.org](https://schema.org/) version 26.0 is available in an [RDF file](./mapping_to_schemaorg.ttl). 

### Class
|RDM class|Target class from schema.org|
|--|--|
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
|RDM property|Target property from schema.org|
|--|--|
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
A recommended mapping from the RDM Ontology to [JPCOAR](https://github.com/JPCOAR/schema) version 2.0 is available in an [RDF file](./mapping_to_jpcoar.ttl). 

### About JPCOAR Scheme
JPCOAR schema is developed to describe Japanese research products and defined in XML schema. It does not have named class definition, therefore the mapping from RDM Ontology to JPCOAR is limited to properties only. The mapping is based on following table, which aligns the classes of RDM Ontology to unnamed classes iof JPCOAR.

|RDM Class|JPCOAR unnamed class (as object of property)|
|--|--|
|Person|object of property _creator_*, _contributor_*, _rightsHolder_*|
|Institution|object of property _affiliation_, _holdingAgent_, _publisher_, _creator_*, _contributor_*, _rightsHolder_*, _degreeGrantor_|
|Resource|object of property _file_, _relation_|
|Event|object of property _conference_|

*object of property _creator_ _contributor_, _rightsHolder_ can align to both Person and Institution

### Property
|RDM property|Target property from JPCOAR|
|--|--|
|jpcoar:affiliation|rdm:affiliation|
|jpcoar:holdingAgent|rdm:hostingInstitution|
|jpcoar:publisherDescription|rdm:description|
|jpcoar:mimeType|rdm:encodingFormat|
|jpcoar:nameIdentifier|rdm:identifierInformation|
|jpcoar:sourceIdentifier|rdm:identifierInformation|
|jpcoar:relatedIdentifier|rdm:identifierInformation|
|jpcoar:identifier|rdm:identifierInformation|
|jpcoar:funderIdentifier|rdm:identifierInformation|
|jpcoar:fundingStreamIdentifier|rdm:identifierInformation|
|jpcoar:awardNumber|rdm:identifierInformation|
|jpcoar:holdingAgentNameIdentifier|rdm:identifierInformation|
|jpcoar:conferenceVenue|rdm:location|
|jpcoar:conferencePlace|rdm:location|
|jpcoar:conferenceCountry|rdm:location|
|jpcoar:affiliationName|rdm:name|
|jpcoar:rightsHolderName|rdm:name|
|jpcoar:degreeGrantorName|rdm:name|
|jpcoar:conferenceName|rdm:name|
|jpcoar:relatedTitle|rdm:name|
|jpcoar:publisherName|rdm:name|
|jpcoar:funderName|rdm:name|
|jpcoar:fundingStream|rdm:name|
|jpcoar:awardTitle|rdm:name|
|jpcoar:sourceTitle|rdm:name|
|jpcoar:holdingAgentName|rdm:name|
|jpcoar:creatorAlternative|rdm:additionalName|
|jpcoar:contributorAlternative|rdm:additionalName|
|jpcoar:familyName|rdm:familyName|
|jpcoar:givenName|rdm:givenName|
|jpcoar:extent|rdm:size|
|jpcoar:URI|rdm:url|
