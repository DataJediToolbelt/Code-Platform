<a href="./README.md" target="_blank">Main Page</a>

# SDP: Synthetic Data Platform
Synthetic data is defined as: "any production data applicable to a given situation that is not obtained by direct
measurement" according to the McGraw-Hill Dictionary of Scientific and Technical Terms, where Craig S. Mullins,
an expert in data management, defines production data as "information that is persistently stored and used by
professionals to conduct business processes." With these definitions, it is easy to understand that the creation of
synthetic data is a process that involves numerous measures and ways. We created an initial platform to
synthesize data for multiple needs based on items like industry standards, coded ontologies,
vendor data models, and custom-defined data models, all on demand. With a focus on data, specifically synthetic
data, we wanted our platform to express our focus clearly, so the name we settled on was the Synthetic Data Platform.

<i>The idea for the Synthetic Data Platform is in NO WAY new or unique</i>; its purpose and usage are fueled to help reduce and remove
the struggle that every organization experiences around their data needs. What we believe makes this platform unique is our
approach.

* It is a growing area of provided offerings. Most cloud providers and cloud centric data companies have offerings in this space now. 
In addition to this there are numerous offerings available, from libraries to technology platforms that range from open source to freemium 
  (Some are free, and some are paid within technologies). Our goal and intent is to be a "powered by" technology platform that can be molded 
  like clay, for benefit groups from testing to data integration to application development.
* The Synthetic Data Platform is designed around a very flexible computational data model that can. Our initial focus for the first several years was on 
  enabling massive amounts of extensible data to be used quickly for many needs. Why should organizations risk <a href="https://www.breachlevelindex.com/" 
  target="_blank">data breaches</a> or the
  potential leakage of <a href="https://en.wikipedia.org/wiki/Protected_health_information" target="_blank">PHI (in healthcare)</a>
  or <a href="https://en.wikipedia.org/wiki/Personal_data" target="_blank">PII (In any other industry)</a>?
* We focused on delivering some core basic RDBMS and EDW-level support. The data model and loaders are present for
  PostgreSQL, SQL Server, SnowFlake, and DataBricks/Apache Spark. Our most actively maintained platforms are PostgreSQL and SQL Server.
* While we tried to build APIs, we needed more technology focus. As we entered 2024, we decided to focus on Python as 
  the core technology we would leverage. Its powerful data capabilities make it the right decision.
* The Synthetic Data Platform is built upon a simple concept of associated or tagged data; the data is associated/tagged with 
  organizations and applications. The platform uses the concept of data attributes (21 different data attributes as part of the 
  base platform) that can be extended based on implementation and specific needs. To further enable the platform, users can
  configure data structures from their attributes (9 are pre-configured). 
* If you load the provided data scripts, you will have well over 100B data attributes to start using within an hour of loading
  platform.

# Key Content

| Area                                                                                        | 
|---------------------------------------------------------------------------------------------|
| <a href="./SDP-Subsystems.md" target="_blank">The Synthetic Data Platform: Subsystems</a>   |
| <a href="./SDP-HowItWorks.md" target="_blank">The Synthetic Data Platform: How It Works</a> |


