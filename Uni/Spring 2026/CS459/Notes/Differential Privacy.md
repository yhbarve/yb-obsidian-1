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
	- Assume **D** includes an individual, Lily, and **D'** does not.
	- **M** is a mechanism or a function applied to the data sets to inject some noise to protect individual privacy.
	- If an analyst learns similar things about Lilly from both **D** and **D'**, then the mechanism M does not provide enough privacy.
	- Given $R = M(D)$, the adversary should be unable to distinguish whether Lilly was in the data set.
	- This means that $M(D)$ has to be randomized, which can be done by adding some noise. But how much noise do we add?
- A database **x** is a collection of records from a universe **X**. A convenient way to represent databases is by their histograms, in which each entry represents the number of elements of that type.
- The **L1 distance** or **L1 norm** of a database is defined as: $$||x||_1 = \sum_{i=1}^{|X|}|x_i|$$
- L1 distance between two databases represents the sum of the absolute differences in frequencies across corresponding elements. $$||x-y||_1 = \sum_{i=1}^{|X| (or |Y|)}|x_i-y_i|$$
- We define neighbouring data sets as those that differ on one single record. The L1 distances between such data sets could be 1 or 2, depending on how the difference is created.
	- If the data sets differ because of **one missing value, the L1 distance is 1.** This is called **unbounded DP**.
	- If the data sets differ because of **one changed value, the L1 distance is 2.** This is called **bounded DP**.
- Our goal is to have the mechanism **M** behave nearly identically for both these data sets. If this happens, an attacker cannot tell whether **D** or **D'** was used.
## p-Privacy
- A mechanism **M** is defined as **p-private** if for every possible output $R$ and all neighbouring datasets $D$ and $D'$:
$$\text{Pr}(M(D') = R) - p < \text{Pr}(M(D) = R) < \text{Pr}(M(D') = R) + p$$
- In simple terms, **p-privacy** means that no matter what output your algorithm gives, an observer shouldn't be able to tell whether a specific person's data was in the dataset or not, because the odds of getting that output only change by a tiny amount **p** either way.
- A smaller **p** means stronger privacy because the allowed difference between the two distributions is tighter.
- An additive difference fails when the probability is close to zero. A tiny absolute change can completely break privacy.
- Therefore, we use a multiplicative factor which scales naturally with probability. This ensures that the privacy guarantees hold uniformly across rare and common outputs alike.

$$\frac{\Pr(M(D') = R)}{p} < \Pr(M(D) = R) < \Pr(M(D') = R) \cdot p$$
- Okay, so the final change we make is we switch to $e^\epsilon$ instead of a raw parameter. This is because exponential scaling makes mathematical proofs much cleaner and easier to handle. 
- **Formal Definition:** A mechanism $M: \mathcal{D} \to \mathcal{R}$ is $\epsilon$-differentially private if for all possible outputs $R \in \mathcal{R}$ and all pairs of neighbouring datasets $D, D' \in \mathcal{D}$, the inequality holds. $$\Pr(M(D) = R) \le \Pr(M(D') = R) e^\epsilon$$
- Smaller $\epsilon$ means more privacy, and larger means less privacy.
- - -
# Sensitivity
- M needs to be a randomized algorithm. M also adds noise to the true output value to provide differential privacy.
- But how much noise to add? This is calculated by measuring the **sensitivity**.
- L1 sensitivity (L1 norm), which is the maximum change that replacing **D** for **D'** can cause in the output. $$\Delta_1 \doteq \max_{D, D'} \vert{}\vert{}f(D) - f(D')\vert{}\vert{}_1$$
- The L1 norm captures the magnitude by which a single individual's data can change the function **f** in the worst case.
- - -
# DP Mechanisms
- Multiple mechanisms provide differential privacy and can be applied to various systems.
- A few examples are:
	- The Laplace Mechanism (DP, continuous outputs)
	- The Randomized Response Mechanism (DP, binary inputs/outputs)
	- The Exponential Mechanism (DP, discrete outputs)
	- The Gaussian Mechanism (approximate DP, continuous outputs)
- - -
# The Laplace Mechanism
- Laplace Probability Density Function: $$p(x) = \frac{1}{2b} e^{-\frac{\vert{}x-\mu\vert{}}{b}}$$
- Variance Formula: $$\text{Var} = 2b^2$$
- Given any function f and its L1 sensitivity, we can turn it into a DP mechanism if we add Laplacian noise to its output.
- **The core mechanism:** $$M(D) = f(D) + (Y_1, Y_2, \dots, Y_k), \text{where } Y_1, Y_2,...Y_k \text{ where} \quad Y \sim \text{Lap}(0, b)$$
- Each $Y_i$ is independently drawn from a Laplace distribution $Y \sim \text{Lap}(b)$ where the scale parameter is: $$b = \frac{\Delta_1}{\epsilon}$$
## Compositional Privacy
- **Given Mechanisms:** $$M_1: D \to R_1 \text{ is } \epsilon_1\text{-DP}$$ and
$$M_2: D \to R_2 \text{ is } \epsilon_2\text{-DP}$$
    
- **Combined Mechanism:** $$M: D \to R_1 \times R_2 \quad \text{where} \quad M(D) = (M_1(D), M_2(D))$$
- **Composition Theorem Result:** $$M \text{ is } (\epsilon_1 + \epsilon_2)\text{-DP}$$
- **Total Privacy Loss Budget Formula:** $$\epsilon = \epsilon_1 + \epsilon_2 + \dots + \epsilon_n$$
## Group Privacy
- Suppose mechanism $M: \mathcal{D} \to \mathcal{R}$ is $\epsilon$-differentially private, and datasets $D, D' \in \mathcal{D}$ differ in exactly $k$ positions. Then:
$$\Pr(M(D) = R) \le \Pr(M(D') = R) e^{k\epsilon}$$
- The privacy guarantee drops linearly with the size of the group.
## Approximate DP
- Differential privacy is very strict. Pure differential privacy requires the inequality to hold strictly for every single possible output. This makes it extremely brittle against tiny implementation changes like truncating noise.
- So we add an extra variable $\delta$ to allow rare catastrophic edge cases where the privacy bounds might technically be broken.
- A mechanism $M: \mathcal{D} \to \mathcal{R}$ is $(\epsilon, \delta)$-differentially private if for all sets of possible outputs $S \subset \mathcal{R}$ and all pairs of neighbouring datasets $D, D' \in \mathcal{D}$:
$$\Pr(M(D) \in S) \le \Pr(M(D') \in S) e^\epsilon + \delta$$
- When $\delta = 0$, it becomes standard $\epsilon$-DP (also called pure DP).
- This definition allows us to add less noise ($\epsilon$) if we are comfortable with the probability of bad outcomes ($\delta$).
- - -
# Differential Privacy Settings
- Depending on who runs the mechanism, there are two broad models for differential privacy.
- Central DP uses a trusted aggregator who collects raw data into a database before adding the noise.
	- A mechanism $M: \mathcal{D} \to \mathcal{R}$ is $\epsilon$-differentially private if for all possible sets of outputs $R \subset \mathcal{R}$ and all pairs of neighbouring **datasets** $D, D' \in \mathcal{D}$:
$$\Pr(M(D) \in R) \le \Pr(M(D') \in R) e^\epsilon$$
- Local DP has each user add noise to their own data locally before sending it to an untrusted analyst.
	- A mechanism $M: \mathcal{D} \to \mathcal{R}$ is $\epsilon$-differentially private if for all possible sets of outputs $R \subset \mathcal{R}$ and all pairs of neighbouring **inputs** $x, x' \in \mathcal{D}$:
$$\Pr(M(x) \in R) \le \Pr(M(x') \in R) e^\epsilon$$
- They use the exact same mathematical structure, but Central DP protects entire datasets against changes in a single record. Local DP protects individual user inputs because the data is randomized right on the user's device before anyone else sees it.
- - -
1. HAMILTON
2. SCHUMACHER
3. VERSTAPPEN
4. SENNA
5. VETTEL
6. PROST
7. ROSBERG
8. HAMILTON
9. HAKKINNEN
10. FANGIO
