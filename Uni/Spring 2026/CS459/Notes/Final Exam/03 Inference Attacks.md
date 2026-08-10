# Inference Attacks
- The goal is to learn something non-trivial and privacy-sensitive from the system.
- Attacks generally rely on information leakage.
- The leakage can be intentional.
	- Sending usage statistics to a service provider
	- Reporting our location to Google Maps
	- Publishing Census Data
- Some leakage is unintentional.
- Attacks combine all leaked information with auxiliary information to infer non-trivial sensitive data.
- Adversarial thinking helps us to think like an adversary to understand the vulnerabilities of a system and develop protection techniques.
- With inference attacks, we also apply Kerckhoff's principle.
- Assume the adversary knows how the system works:
	- There are no hidden parameters other than the user's data.
	- The adversary can even know some rough distribution that the user's data follows.
- - -
# Designing a System Aware of Inference Attacks
- For any system that relies on user's data, there are two goals:
	- **Utility:** Design a system that provides benefits to its users and the service provider.
	- **Privacy:** Design a system that provides protection against inference attacks.
- How we measure utility and privacy is very complicated.
- Recall what privacy means. It is the right of the individual to decide what information about himself should be communicated to others and under what circumstances.
- Privacy basically means having control over:
	- Who we share our data with?
	- Who they can share it with?
	- For what purpose do they use it?
	- Etc.
## Quantifying Privacy
- **Syntactic notions of privacy:** These are computed on the leaked or released data and are **data dependent**.
- **Semantic notions of privacy:** These are computed on the data release mechanism itself, and they hold regardless of the data **(data independent)**.
## Utility vs Privacy
- Utility is the benefit that users and the provider get from using the system.
- For example, in a communications system, the utility for users is to be able to communicate with each other from the comforts of their house.
	- To quantify, we could think about:
		- the number of packets dropped
		- the network bandwidth or throughput
		- the network latency or delay
- In a machine learning setting, the utility for the data owner could be that it can sell access to the trained model for revenue.
	- To quantify, we could think about:
		- test accuracy
		- biasedness of the model
		- computational requirements to build the model
		- the training time required for the model
- When designing a system, you always have to face the **privacy-utility trade-off**. How do you design a system that provides maximum utility while providing maximum privacy?
- Designing a system that provides a good privacy utility trade-off is hard.
- - -
# Inference Attack Examples
## Census Reconstruction
- A census reconstruction attack uses published aggregate statistics and auxiliary background data to infer individual-level private records.
- A census involves collecting lots of privacy-sensitive data. Some useful aggregate statistics are released.
## SQL Inference Attacks
- A data collector creates a relational database with data from different clients.
- An adversary can issue SQL queries to gather data from the table.
- Even if the result of a query is harmless, the combination of two or more queries can be very dangerous.
- Placing restrictions on individual queries while still reporting exact values does not work.
## Database Reconstruction Attacks
- Even if the database adds noise to the query responses, a combination of queries can still be sufficient to reconstruct at least a part of the database.
## Statistical Inference Attacks
- $\Pr(x)$ is the **prior** probability distribution of the secret value.
    - $\Pr(y\vert{}x)$ is the **mechanism** or **likelihood** modelling leakage given the secret.
    - $\Pr(x\vert{}y)$ is the **posterior** probability distribution after observing leakage $y$.
- **Core Formulas:**
    - **Bayes' Theorem:** $\Pr(x\vert{}y) = \frac{\Pr(y\vert{}x) \cdot \Pr(x)}{\Pr(y)}$
    - **Law of Total Probability:** $\Pr(y) = \sum_{x} \Pr(x) \Pr(y\vert{}x)$
- **Expected Value Recap:** The expected value of a random variable is defined as $E\{x\} = \sum_{x} x \cdot \Pr(x)$.
- **Conditional Expectation:** Upon observing leakage $y$, the adversary computes the conditional expectation $E\{x\vert{}Y = y\} = \sum_{x} x \cdot \Pr(x\vert{}y)$.
- **Maximum Likelihood (ML) Attack:** The adversary estimates $\hat{x}$ by finding the value of $x$ that maximizes the likelihood of generating the observed leakage $y$: $\hat{x} = \operatorname*{argmax}_{x} \Pr(y\vert{}x)$.
- **MAP Definition:** Chooses the estimate $\hat{x}$ that maximizes the posterior probability: $\hat{x} = \operatorname*{argmax}_{x} \Pr(x\vert{}y)$.
- **Simplified Expression:** By expanding via Bayes' theorem, this is equivalent to maximizing the product of the prior and likelihood: $\hat{x} = \operatorname*{argmax}_{x} \operatorname{Pr}(x) \cdot \operatorname{Pr}(y\vert{}x)$.
- **Computation Note:** Computing $\Pr(y)$ is unnecessary for the argmax operation.
- **Equivalence with ML:** MAP and Maximum Likelihood (ML) yield identical results when the prior probability distribution is uniform (meaning every secret value $x$ is equally likely).
## ML Inference Attacks
- Some examples of inference attacks include:
	- Membership Inference
	- Attribute Inference (parts of a data sample)
	- Property Inference (property of the whole training set)
	- Reconstruction attack (infer a whole training set)
- The idea is to use the fact that the model is more confident on samples it has trained on. 
- We can use the confidence score, we can use thresholding techniques, or train an ML model as an attack.
## Linking Attacks
- Linking attacks find connections between two different sources of leakage that alone seem harmless.