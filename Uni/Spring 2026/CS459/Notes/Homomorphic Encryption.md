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
- This function g is a homomorphic function on the ciphertexts $c$ and $d$