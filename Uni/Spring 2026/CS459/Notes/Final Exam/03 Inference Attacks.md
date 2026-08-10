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
- In a machine learning setting, the utility for the data owner could be that it can sell access to the trained model for revenue.
- 