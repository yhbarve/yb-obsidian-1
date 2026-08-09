# Homomorphic Encryption
- Homomorphic encryption is a cryptographic technique that allows computations to be performed on encrypted data without requiring decryption.
- Raw data can remain fully encrypted while it is being processed, manipulated, and run through various algorithms.
- An example is Microsoft's ElectionGuard
	- It's a way of checking that election results are accurate and that the votes have not been altered, suppressed, or tampered with in any way.
	- Individual voters can see that their vote has been accurately recorded and their choice has been correctly added to the final tally.
- - -
# Let's get more technical
- Consider two cipher texts that use the same key. $$c = E_K(x), d = E_K(y)$$
- Let $f$ be a function that operates over plain text $x$ and $y$.
- We need to find a function $g$ such that $$g(c, d) = E_K(f(x, y))$$
- This function $g$ is a homomorphic function on the ciphertexts $c$ and $d$.
- Four types of homomorphic encryptions:
	1. **Partial:**
		- Supports **only one type** of algebraic operation on ciphertexts: either unlimited additions or unlimited multiplications.
		- Used in RSA.
	2. **Somewhat:**
		- The **number of operations** that can be performed is **bounded**, and the **accuracy** of the computation may **degrade** as more operations are performed.
		- Used in BGN.
	3. **Levelled Fully:**
		- Can perform an arbitrary number of computations on encrypted data if it has a pre-defined set of computations specified ahead of time.
		- Used in BFV, CKKS
	4. **Fully:**
		- Enables any number of computations to be performed on encrypted data without a predefined sequence or limit.
		- Computationally expensive.
		- Used in BGV, DGHV
- **Fully homomorphic encryption** supports **both addition and multiplication simultaneously**, allowing you to evaluate arbitrary complex functions on encrypted data without ever decrypting it.
- In **somewhat homomorphic encryption**, the **number of operations** that can be performed is **bounded**, and the **accuracy** of the computation may **degrade** as more operations are performed.
- - -
