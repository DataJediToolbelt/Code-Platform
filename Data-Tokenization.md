<a href="./README.md" target="_blank">Main Page</a>

# Tokenizing Data 
McKinsey defines tokenization as: "Tokenization is the process of creating a digital representation 
of a real thing. Tokenization can also be used to protect sensitive data or to efficiently process 
large amounts of data." Our history for almost everything you will read is based on experience of working with 
data and databases directly. Several of the contributors and even potential contributors talked
about the topic of tokenization and why we never included anything around this topic in our repositories.
Because we leverage tokenization internally we decided to make it a more formalized capability 
versus just some code that we potentially leverage.

# Our Tokenization Guiding Principles 
- Our efforts are focused around providing a consistent means to process data and produce a consistent result.
- Tokenization is configurable and tunable. Our initial work will be focused on creating SHA512 tokens, which are 128 bytes each.
in future releases in 2025 e plan on enabling users to determine the cryptography level they wish to implement and use.
-  Any data that is tokenized will ALWAYS be associated with applications and organizations and sources as defined within the platform. This is
intended to support consistency and extensibility for business or user needs.
- These capabilities can be used from the platform as an API or part of the application capabilities.
- We have enhanced our data model to support the storage of what reference data was used 
and the tokens it built. *We will not store all the metadata that was used to generate a specific token.*

# Key Content

| Area                                                            | 
|-----------------------------------------------------------------|
| <a href="./TBD.md" target="_blank">Tokenization: Subsystems</a> |


