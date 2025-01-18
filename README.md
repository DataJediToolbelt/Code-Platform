# Application and Web Tier Platform
As we discussed on the main platform's repository README.md the main focus of our 
efforts was on data and supporting it with an extensible data tier for a very long time. As 
we built development assets to showcase the tremendous data model extensibilities and 
capabilities we were always underwhelmed overall. In the end it seems to have a combination
of lack of focus and potentially wrong technology for our overall vision. We are notI slighting 
any technology as used previously. SpringBoot and Node have a very important 
place in hundreds of widely adopted platforms. While we did some cool things with them 
and we did some cool things with the technologies we felt there could be much more we 
could do.

So, how and why did we choose Python? While other programming languages that we have
used have adoption and established communities behind them there was something always 
nagging us, this is intended to be a very large data driven platform and are we using the 
right technologies. For us, the simple answer was no. What would help us drive better 
technology from our data driven platform than a powerful development technology that is 
a data enabler. Python was the easy choice with this as our core need. Python is the widest 
adopted development technologists when working with data, hands down. There is 
no other technology in the data engineering space with close to the capabilities it provides. 
Whether it is AI, or data focused whether that is EDW (Spark/DataBricks/ Snowflake), 
RDBMS data usage it is a foundational enabler. But well beyond the massive community, 
supported assets being maintained it also has a vast amount of other industry leading 
capabilities whether it is command line, websites, APIs, or automation Python has a large 
extensible offering.

## Technology - Legacy
As we mentioned above we talked about how we did nor really have a consistent approach 
to technologies used that would help us better enable capabilities. Here is the [Legacy Code Details](platform_documentation/Platform-Legacy.md)

## Technology - Future (Python)
We currently are working to implement all platform technology based capabilities with 
Python. We have used Python v3.9 through various dot releases in 3.12 successfully on 
multiple operating systems. To install Python we have only leveraged installers from python.org 
or simply installed Anacoda. Here is the [Platform future overview](Platform-Python.md).

# Platform
This initial section covers basic areas of the system.

| Area                        | Link                                      |
|-----------------------------|-------------------------------------------|
| General Basics Details of Platform | [Platform Basics](platform_documentation/Platform-Usage-Basics.md) |  
| Web Tier Platform Usage     | [Web Tier](platform_documentation/Platform-Usage-WebTier.md)     |

## Platform Modules
In order to best explain how the Platform works we have created content that explains it. 

| Area                  | Link                                                            |
|-----------------------|-----------------------------------------------------------------|
| Synthetic Data        | [Base Content](platform_documentation/Data-SynthethicData.md)   |  
| Data Anonymization    | [Base Content](platform_documentation/Data-Anonymization.md)    |
| Data Deidentification | [Base Content](platform_documentation/Data-Deidentification.md) |
| Data Tagging          | [Base Content](platform_documentation/Data-Tagging.md)          |
| Data Tokenization     | [Base Content](platform_documentation/Data-Tokenization.md)     |