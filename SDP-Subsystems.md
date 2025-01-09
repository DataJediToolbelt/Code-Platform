<a href="./Data-SyntheticData.md" target="_blank">Synthetic Data Main Page</a></br>
<a href="./README.md" target="_blank">Main Page</a>

# Subsystems
Within the data tier there are several specific subsystems that we have logically separated by a naming convention of <tier>_<capability>

## refdata - The Place To Start
Reference data is intended to be used to provide the users and the platform extensibility while working
to keep potentially complex actions data driven.

| Table            | Purpose                                                                                                                                                                                   | 
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status           | Platform uses status as a core measure of active and accurate records. The platform defaults all data to an active status and users can simply make records any other status if they wish | 
| Vendors          | Companies that have systems (applications) where data is being used in some form |
| IndustryStds     | Intended to be where standards bodies data is relevant to the platform|
| SensitivityFlags | Enables the platform to categorize information types|
| Codesets         | Are intended to align to either custom or industry-specific supporting data needs  |
| Industries       | Is about thinking ahead, and as we add functionality or capabilities, specific industries might benefit from these specifically |
| Applications     | Within the platform it is intended to define ANY asset that it interacts with|
| Legal Entities   | Intended to help define complex organizational relationships. Specifically, it is intended to be the incorporated entity that the organization(s) would be a part of|
| Organizations    | Companies that have data represented in the platform |

## datamodel
To help try and keep the platform's core data model understandable we decided long ago to document it
within the existing platforms datamodel.

| Table      | Purpose                                                               | 
|------------|-----------------------------------------------------------------------|
| Domain     | Main key areas of the platform                                        
| Datatables | All the tables within the platform                                    |
| APIs       | This will be renamed to assets to support wider information and needs |

## datatier
This is where all generated or constructed data is stored within the platform

| Table      | Purpose                                                               | 
|------------|-----------------------------------------------------------------------|
| datatier     | All the generated and existing data within the platform  |                     
| datatier_datastructures | All the data structures the platform generates or leverages are stored here |

## platform
The core configurable and tunable platform components.

| Table                  | Purpose                                                                                                | 
|------------------------|--------------------------------------------------------------------------------------------------------|
| dataattributes         | The core items that the platform uses and can grow and extend based on implementation needs.           |
| datageneration         | This is where the platform can be configured to generate or build data as needed.                      |
| datastructures         | This is what we want to know the data structure as, its name                                           |
| datastructures_details | This is the configurable structure which includes the dataattributes being used and supporting details |

## terms
The platforms ability to manage some level of reference data from applications run within organizations.

| Table          | Purpose                      | 
|----------------|------------------------------|
| termstocodeset | Core data that is referenced |



