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
	- **Identifiers:** Uniquely identify an individual
	- **Quasi-identifiers:** In combination with external data, can identify an individual
	- **Confidential:** Contain privacy-sensitive information
	- **Non-confidential:** Are not considered sensitive
- We will always remove identifiers and focus on confidential attributes.
- - -
# System Model
- Each user contributes to a row in the database.
- A data curator releases a sanitized / cleaned version of the database.
- The attacker / adversary sees this sanitized database.
- The properties that we want to enforce:
	- k-anonymity
	- l-diversity
	- t-closeness
- - -
# k-Anonymity
- **Definition: For each published record, there exists at least $k-1$ other records with the same quasi-identifiers.**
- To compute:
	- Group the rows with the same quasi-identifiers. Each group forms an **equivalence class** or **equi-class.**
	- Count the smallest size of a group. That's the k-anonymity.
- To provide k-anonymity:
	- **Remove** a quasi-identifier.
	- **Reduce the granularity** or a quasi-identifier (eg: hiding last character of the ZIP code)
	- **Group** quasi-identifiers (eg: report age as a range instead of actual numbers)
- - -
