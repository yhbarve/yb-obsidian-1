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
- 