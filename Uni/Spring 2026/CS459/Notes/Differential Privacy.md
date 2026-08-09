# From Symmetric to Syntactic Privacy
- We know that syntactic privacy imposes structural conditions on the released data set.
- The main question to ask is if the release dataset satisfies a required structural pattern.
- However, a release can satisfy a syntactic rule and still reveal sensitive information.
- This motivates semantic privacy and, in particular, differential privacy.
- A great analogy is: in language, semantics ask what a sentence means. In privacy, semantics ask what the release lets an adversary learn.
- So the goal of curating a data set is to protect privacy while providing useful information (utility).
- Access to a statistical database should not enable the adversary to learn anything about an individual that could not be learned without access.
- You also have to acknowledge that you **cannot fully prevent auxiliary information**. An adversary with access to other statistical databases can still infer some information about an individual from our curated database.
- The only way to achieve the perfect notion of privacy is by providing no statistics at all. This completely defeats the purpose. 
- - -
# Differential Privacy
- We want to capture the contribution of an individual to the database and its statistics.
	- Assume D includes an individual, Lily, and D' does not.
	- M is a mechanism or a function applied to the data sets to inject some noise to protect individual privacy.
	- If an analyst learns similar things about Lilly from both D and D', then the mechanism M does not provide enough privacy.
	- Given $R = M(D)$, the adversary should be unable to distinguish whether Lilly was in the data set.
	- This means that $M(D)$ has to be randomized, which can be done by adding some noise. But how much noise do we add?
- A database **x** is a collection of records from a universe **X**.  