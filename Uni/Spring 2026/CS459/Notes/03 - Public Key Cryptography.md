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
