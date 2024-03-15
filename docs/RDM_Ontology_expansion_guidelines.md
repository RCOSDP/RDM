# Expanding RDM Ontology as an Application Profile
This document presents a policy for extending the RDM ontology as an application profile. The RDM Ontology includes both abstract concepts and specific concepts based on abstract one. Application profiles become easy to understand and use by defining application profiles in compliance with a policy that extends specific concepts from the abstract concepts in the RDM ontology.

## To Add Subproperty of rdm:contributor
Some properties such as _rdm:creator_, are already defined as subproperties of rdm:contributor in RDM Ontology. To add a property which means specific role of rdm:Person or rdm:Institution entity, rdm:contributor property MUST be inherited as super-property as well as these properties. 

## To Add Subproperty of rdm:identifierValue
Some properties such as _rdm:doi_, are already defined as subproperties of rdm:identifierValue in RDM Ontology. (see details in [User Guide](./RDM_Ontology_usage_guidelineds.md)) To add a property which means the value of specific identifier system, rdm:identifierValue property MUST be inherited as super-property and the correspondence between the property and the description by using rdm:Identifier class MUST be shown. 

## To Add an Enumeration
Enumeration can be defined by inheriting rdm:Enumeration. Each item in enumeration MUST be a subproperty of  both specific enumeration class and owl:NamedIndividual. (see rdm:ConditionOfAccessEnumeration) A new item can be added to existing enumeration by defining owl:NamedIndividual class which is also a subproperty of the enumeration class.