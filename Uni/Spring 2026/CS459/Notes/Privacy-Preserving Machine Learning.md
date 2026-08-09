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
- The Gaussian mechanism provides $(\epsilon,\delta)$-DP, whereas the Laplace mechanism only provides $\epsilon$-DP.
- $\sigma^2$ represents the noise variance. To provide more privacy, we need more noise (achieved by lowering $\epsilon$.
- - -
# Primer on Machine Learning
- For simplicity, we will focus on a classification problem with supervised learning.
	- The other types of machine learning are unsupervised and reinforcement learning.
- We have a training set with $n$ samples. Given a sample $(x_i, y_i)$, $x_i$ are the features and $y_i$ is the label.
- We want to produce a function that can predict a sample's label from its features.
- We use a training set to train such a function. Ideally, it should correctly predict labels for unseen samples.
- A model **generalizes** well if it has a high accuracy on unseen samples.
- A model **overfits** if it works perfectly for samples in the training set but does not generalize well.
- There are many architectures for machine learning models. One of the most popular ones is a **neural network**.
	- We define a loss function that we want to minimize: $l(\theta, x, y)$, where $\theta$ are the parameters $w$ and $b$.
	- In a classification task, the model assigns probabilities for each class.
	- A model is said to have **low cross-entropy** when it assigns a high probability to the true class. Otherwise, the model is considered to have a **higher cross-entropy.**
- Since we have the training set, it makes sense to minimize the empirical loss in the training set. In practice, the minimization is done using **Stochastic Gradient Descent (SGD)**.
	- The gradient of the loss evaluated at a particular sample is the derivative with respect to each parameter.
	- It tells us the direction in which $\theta$ should go to minimize the loss for that sample.
- We can minimize the loss by running several steps or **epochs** of gradient descent.
- However, this is expensive, so we usually do the iterations over a subset of the training sets called **batches**.
- - -
# Inference Attacks in ML
- There are many types of attacks against machine learning.
- The three main types of attacks are:
	1. **Inference Attacks**
		- Occur during the _deployment phase_, where an adversary queries a trained model to extract sensitive information about whether specific individuals were part of the private training dataset.
	2. **Poisoning Attacks**
		- Occur during the _training phase_, where an attacker injects malicious or tampered data into the training set to manipulate the model's behavior or create backdoors.
	3. **Evasion Attacks**
		- Occur during the _testing/inference phase_, where an attacker subtly modifies inputs (like adding imperceptible noise to an image) to trick a fully trained model into making a wrong classification.
- - -
