# Recap on Group Privacy
- If a mechanism provides $\epsilon$-DP for a pair of neighbouring datasets that differ in **1** entry, then it provides $k\epsilon$-DP for datasets that differ in **k** entries.
- If a mechanism provides $(\epsilon, \delta)$-DP for a pair of neighbouring datasets that differ in **1** entry, then it provides $(k\epsilon, ke^{(k-1)\epsilon}\delta$-DP for datasets that differ in **k** entries.
## Naive Sequential Composition
- When running k mechanisms on the same sensitive data set and publishing all k results, the $\epsilon$s and $\delta$s linearly add up.
- Let $M = (M_1, M_2, ..., M_k)$ be a sequence of mechanisms, where $M_i$ is $(\epsilon_i, \delta_i)$-DP. Then $M$ is $(\sum_{i=1}^k \epsilon_i, \sum_{i=1}^k \delta_i)$-DP.
- Privacy decreases as we publish more results. More queries mean more leakage of privacy.
## Advanced Sequential Composition
- Advanced composition lets you trade a tiny increase in $\delta$ to dramatically shrink the growth of $\epsilon$.
- Let $M = (M_1, M_2, ..., M_k)$ be a sequence of mechanisms, where $M_i$ is $(\epsilon, \delta)$-DP. Then $M$ is $\left(\epsilon \sqrt{2k \cdot \ln\left(\frac{1}{\delta'}\right)} + \frac{k\epsilon(e^\epsilon - 1)}{e^\epsilon + 1}, k\delta + \delta'\right)$-DP.
- This assumes that the worst-case privacy breach is very unlikely to happen in every single query simultaneously.
- The probability of a privacy breach goes up slightly, but the average privacy loss reduces to a much lower square root scale.
- $N$ is the total number of individuals in your dataset. Guessing someone at random gives a probability of $\frac{1}{N}$.
- The total failure probability ($k\delta + \delta'$ cryptographic risk) should be kept even smaller than that baseline random guess, making it practically negligible.
- If your system's total failure probability ($k\delta + \delta'$) is smaller than $1/N$, it means the algorithm itself isn't adding any meaningful risk beyond what an attacker could already achieve by blindly guessing.
- Because $\delta'$ is a knob you control, you can increase it slightly to make $\epsilon$ smaller (giving you better data accuracy/utility), as long as it stays below that $1/N$ safety ceiling.
## Parallel Composition
- Let $M = (M_1, M_2, ..., M_k)$ be sequence of mechanisms, where $M_i$ is $\epsilon_i$-DP. Let $D_1, D_2, ..., D_k$ be a deterministic partition of $D$. Publishing $M_1(D_1), M_2(D_2), ..., M_k(D_k)$ satisfies $\left(\max_{i \in [1,...,k]} \epsilon_i\right)$-DP.
- In parallel composition, you run separate queries on disjoint parts of the data set at the same time.
- The total privacy loss is simply the maximum $\epsilon$ of the individual queries.
- - -
# Gaussian Mechanism: A Noise Mechanism for $(\epsilon, \delta)$-DP
- The L2 sensitivity can be defined as $$\Delta_2 \doteq \max_{D, D'} \vert{}\vert{}f(D) - f(D')\vert{}\vert{}_2$$
- The formula for $\ell_2 \text{ norm is: } \vert{}\vert{}x\vert{}\vert{}_2 = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$
- The Gaussian mechanism is very similar to the Laplace mechanism. The key difference is that the Gaussian mechanism uses L2 sensitivity instead of L1 sensitivity.
- $f: \mathcal{D} \to \mathbb{R}^k$ with $\ell_2$-sensitivity $\Delta_2$, the **Gaussian mechanism** is defined as $$M(D) = f(D) + (Y_1, Y_2, ..., Y_k)$$
- Each $Y_i$ is random noise independently distributed as $$Y_i \sim N(0, \sigma^2),\text{ with } \sigma^2 = 2 \ln\left(\frac{1.25}{\delta}\right) \Delta_2^2 / \epsilon^2$$
- 