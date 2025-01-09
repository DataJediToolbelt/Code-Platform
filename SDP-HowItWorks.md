<a href="./Data-SyntheticData.md" target="_blank">Synthetic Data Main Page</a></br>
<a href="./README.md" target="_blank">Main Page</a>

# The Synthetic Data Platform: How It Works
To leverage the platform, the following core steps should be completed:
- The DDL for the supported data technology that is needed is implemented
- The data technologies data structure is seeded with data for the Synthetic Data Platform

# Core Platform Activities - Data Powered
Overall, the platform design is focused on a series of automatic methods that provide very 
specific capabilities that can be invoked in a variety of ways.

## Supporting Activities
Supporting activities for the platform deal with customizing referential data activities for 
referencing or tagging data within the platform for the implementation needs.

## Data
The following is a specific list based on the particular data attributes that are provided by the 
platform.

### Data Attributes
The following are data attributes the platform is pre-seeded with, including the ability to 
upsert (insert/update) records. You can just add to these based on what you need.

| Attribute              | Type of Data |Purpose | 
|------------------------|--------------|--------|
| Account Numbers        | Generated        |Basic Generic Account Number - Built on RegEx|
| Addresses              | Generated        |US Address generator that generates addresses in a few formats| 
| Area Codes             | Pre-Existing      |Valid US Area Codes|
| Bank Accounts          | Generated      |Generate bank account numbers|
| Bank Routing           | Pre-Existing        |Valid Bank Routing numbers|
| Credit Cards           | Generated        |Generate valid credit card numbers|
| Drivers License Number | Generated        |Generate valid US driver's licenses in all 50 states; if the states support multiple formats, we ONLY implemented one single format|
| Date of Birth          | Generated        |Valid dates of birth|
| Generic Reg Exp        | Generated        |General regular expression type|
| Names - First          | Pre-Existing | Valid first names based on a variety of data sources with gender associated|
| Names - Last           | Pre-Existing |Valid last names based on a variety of data sources|
| Phone Numbers - US     | Generated        |Generate valid us phone numbers|
| Serial Numbers         | Generated        |Generate serial numbers for products/devices|
| SSN                    | Generated        |Generate valid social security numbers|
| UPC Codes              | Pre-Existing|A pre-existing list of UPC Codes (products)|
| User Identities        | Generated         |Generated User Identity|
| Zipcodes - US          | Pre-Existing|Valid US Zipcode list from public source|

There are also a few specific data attributes that are established but have not been tested as there 
has been no use cases for their usage.

| Attribute           | Genrated |Purpose | 
|---------------------|---------|---------|
| Phone Numbers - Intl |Generated| Usage would be for any international phone number        |
| Addresses - Intl     |Generated|Usage would be for any international address |

### Data Structures
The following data structures are implemented with the core platform.

| Structure           | Purpose                                                  | 
|---------------------|----------------------------------------------------------|
| Person Demographics | Includes attributes: name (first and last), address, ssn |
| Bank Account        | Bank Routing and Bank Account Number                     |
| US Phone Number     | Area Code and Phone Number                               |
| Complete Name       | First and Last Name                                      |
| US Address          | Address which includes city. state, zip                  |

# Core Platform Activities - Configuring/Managing the Platform
Understanding or awareness of key aspects of the data model is critical as they lay the groundwork for how you would use the platform.


