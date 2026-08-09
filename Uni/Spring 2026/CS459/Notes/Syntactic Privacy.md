# Inference Across Multiple Sources
- Inference problem is more severe if the adversary has access to multiple data sources, as long as they can aggregate information across sources.
- External data can be from:
	- Publicly available datasets
	- Purchased datasets
	- Govt. revealed data
	- Large companies collect data which can be hacked into (data leak/breach)
- If datasets contain **veronyms** or **persistent pseudonyms**, one can link data records across these datasets & learn more about an individual or an entity.
	- **Veronyms**: Unique identifiers that explicitly reveal a person's identity (eg: name, ID)
	- **Pseudonyms**: False or fictitious identifiers (eg: username)
- Removing all identifiers from a dataset does not necessarily protect the privacy of individuals. We'll see how in this chapter.
- Simply replacing identifiers with random numbers does not always work. (AOL example)
- Hashing does not make data completely anonymous. For small input spaces, dictionary attacks are pretty easy. (NYC Taxi example)
- Background knowledge relating to the primary data can be used to further de-anonymize records.
- - -
# Measuring Privacy
- **Empirically:** Measure the performance of an attack.
- **Theoretically:**
	- **Syntactic:** Measuring a property on the released data **(OUR FOCUS)**
	- **Semantic:** Ensure that the data-release mechanism itself has a property
- - -
# Syntactic Privacy in Relational Databases
- Syntactic notions of privacy define certain properties that the released dataset must satisfy.
- In a relational database / table, the rows are **SAMPLES**, and the columns are **ATTRIBUTES**.
- Attributes can be:
	- Identifiers: Uniquely identify an i
	- Quasi-identifiers: 
	- Confidential: Contain privacy-sensitive information
	- Non-confidential: Are not considered sensitive