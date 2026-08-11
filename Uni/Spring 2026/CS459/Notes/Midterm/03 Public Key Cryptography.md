---
tags:
  - uni
  - s26
  - cs459
---
# Lecture 03: Public-Key Cryptography
- - -
# Public Key Encryption (PKE)
- A public key encryption was invented in the 1970s, and it is also called asymmetric encryption.
- Unlike symmetric schemes where both parties share a single key, PKE uses two distinct keys.
	- A public key $e_k$ which is published to a directory for encryption
	- And a private key $d_k$ kept secret for decryption 
- The core advantage of PKE is that Alice can send an encrypted message to Bob without ever meeting or exchanging a secret before hand.
- Some examples include RSA, ElGamal, ECC, NTRU, and McEliece.
## How It Works
- Public key encryption operates across five distinct phases:
	1. Key generation
	2. Public key distribution
	3. Message encryption
	4. Cipher text transmission
	5. Message decryption
- The mathematical structure guarantees that only the holder of the private trapdoor can reverse the encryption. 
- Here are the steps discussed in detail:
	1. **Key Generation:** Bob generates a complementary pair of mathematical keys: a public encryption key $e_k$ and a private decryption key $d_k$.
	2. **Public Key Distribution:** Bob keeps $d_k$ strictly confidential and publishes $e_k$EK to a publicly accessible directory or cloud repository.
	3. **Message Encryption:** Alice wants to send a plain text message $M$ to Bob. She retrieves Bob's public key $e_k$ from the public directory and passes both $M$ and $e_k$ into an encryption function to create ciphertext $C = \text{Encrypt}(M, e_k)$.
	4. **Ciphertext Transmission:** Alice transmits $C$ to Bob over an insecure public channel.
	5. **Message Decryption:** Bob receives $C$ and applies his private key $d_k$ to the decryption algorithm to recover the original message $M = \text{Decrypt}(C, d_k)$.
- Eavesdroppers cannot decrypt $C$ or derive $d_k$ because deriving $d_k$ from $e_k$ is an intractable computational problem without the secret trapdoor $t$.
## Steps for PKE
1. Bob creates a key pair.
2. Bob gives everyone the public key.
3. Alice encrypts the message using Bob's public key and sends it.
4. Bob decrypts the message using his private key.
5. Eve and Alice cannot decrypt the message because they only have the encryption key.
## Requirements for PKE
1. Easy Forward Computation: The encryption function must be easy (computationally efficient) to evaluate for any input.
2. Hard inversion: Reversing the function without special information must be computationally hard.
3. Trapdoor Mechanism: A mathematical trapdoor, (in this case the secret key), must exist such that computing the inverse function becomes easy only when the trapdoor is known. 
- - -
# Textbook RSA
- Textbook REC uses modular arithmetic and prime factorization to build a trapdoor one-way function.
- RSA security relies on the practical impossibility of factoring a large composite number $n$ back into its constituent prime factors $p$ and $q$.
- It also relies on modular arithmetic, which is math performed on integers that wrap around when reaching a modulus.
	- If $7\ \text{mod}\ 5 = 2$ and $12\ \text{mod}\ 5 = 2$, then $7 \equiv 12 (\text{mod}\ 5)$
	- This means 7 and 12 are congruent modulo 5 because they yield the same remainder when divided by 5.
- To recap, prime numbers are natural numbers greater than one, divisible only by one and itself. Every integer can be written as a unique product of prime numbers.
- Fast algorithms exist to check if a number is prime without finding its factors. However, finding the prime factors of a composite number is computationally hard for large numbers.
## The High-Level RSA Concept
- The goal is to find large integers $e$, $d$, and $n$ such that $m^{ed} \equiv m (\text{mod}\ n)$ for any message $m$.
- The creator easily selects $e$, $d$, and $n = pq$, where $p$ and $q$ are large primes.
- An adversary knowing $e$, $n$, and ciphertext $C$ finds it extremely hard to calculate $d$ without factoring $n$.
## Encryption
- $C = m^{e}(\text{mod}\ n)$
- The ciphertext is equal to the message multiplied by itself $e$ times modulo $n$.
- The public key is $(e, n)$.
## Decryption
- $m = C^d(\text{mod}\ n) = m^{ed}(\text{mod}\ n)$
- Decryptions rely on the number $d$ satisfying $ed = 1(\text{mod}\ \phi(n)$), such that $m^{ed}(\text{mod}\ n) = m(\text{mod}\ n) = m$.
- In other words, $d$ is the multiplicative inverse of $e(\text{mod}\ \phi(n)$.
- $\phi(n) = (p-1)(q-1)$, where $p$ & $q$ are random primes.
- The private key is just $d$. Once calculated, other numbers can be discarded.
## Key Generation
- Pick two random primes $p$ and $q$ such that $pq = n$.
- 