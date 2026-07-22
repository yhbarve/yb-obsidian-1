#uni #s26 #cs459
# Lecture 02: Cryptography Basics
---
## Learning Outcomes
- Identify attack techniques and apply them.
- Explain the building blocks of modern cryptography.
- Explain how modern cryptography properties arose.
- - -
## Cryptography vs Steganography
- Cryptography protects the confidentiality of the content. An eavesdropper would know that communication is happening, but wouldn't be able to read what is inside the message.
- Steganography, on the other hand, protects the existence of the communication. An eavesdropper wouldn't even realize a secret message is being passed.
- - -
## CIA For Cryptography
1. **Confidentiality**
	- Confidentiality ensures that message content remains secret and accessible only to authorized parties, preventing passive adversaries from reading the plain text.
2. **Integrity**
	- Integrity guarantees that a message has not been altered, tampered with, or corrupted during transit, preventing active adversaries from changing the data undetected.
3. **Authenticity**
	- Authenticity verifies the true identity of the sender. It ensures that a message actually originates from the claimed party and prevents adversaries from impersonating someone else.
- - -
## Ciphers
- A cipher is simply an algorithm used to perform encryption and decryption.
	- Plain text is encrypted using a key and gets converted into ciphertext.
	- The ciphertext is then transported along the insecure channel to the end user. The end user decrypts the ciphertext using the same key and converts it into the plaintext again.
	- The key is transported to the end user over a secure channel.
- Some examples of ciphers:
	1. **Shift Ciphers (Caesar Cipher)**
		- Replace each character in a message by another character that is N steps ahead in the set of alphabets or characters.
		- For example, in ROT13, A would be replaced by N, B would be replaced by O, C would be replaced by P, and so on.
	2. **Substitution Ciphers**
		- Replaces each letter of the alphabet with a corresponding letter mapped out in a lookup table.
		- Natural languages have predictable letter frequencies. Because a fixed key map preserves these relative letter frequencies in the ciphertext, an attacker can break the cipher by analyzing character counts.
	3. **Transposition Ciphers**
		- Does not change the letters themselves. Instead, it rearranges their order based on a geometric pattern or a rule.
		- For example, writing a message across rows of a grid and then reading it out column by column.
		- The original letter frequencies remain unchanged, revealing clues about the message length and the grid structure.
- **Kerckhoff's Principle:**
	- The security of a crypto system should solely depend on the secrecy of the key, but never on the secrecy of the algorithm.
- **Shannon's Maxim:**
	- You must design systems assuming the adversary will eventually learn the exact algorithm being used.
- Both the above principles state that a cryptosystem's security must depend only on keeping the key secret and not on keeping the encryption algorithm secret.
	- Hiding how an algorithm works is a bad strategy because **algorithms can be reverse-engineered, leaked, or stolen.**
	- When algorithms are public, thousands of security experts and cryptanalysts test them for weaknesses. **If an algorithm survives years of public scrutiny, we can trust it.**
	- Keys are easy to replace. It is infinitely **easier to change a short-lived key** than it is to replace an entire proprietary encryption algorithm built into your software infrastructure.
- - -
## One-Time Pad
- The one-time pad is the only mathematically unconditionally secure cipher.
- **How it works:**
	- It works by performing a bitwise XOR between the plaintext and a random key of the exact same length.
	- **Encryption:** $Y_{i} = X_{i} \oplus K_{i}$ or $y_{i} = x_{i} + k_{i} (\text{mod}\ 2)$
	- **Decryption:** $X_{i} = Y_{i} \oplus K_{i}$ or $x_{i} = y_{i} + k_{i} (\text{mod}\ 2)$
- Because every key bit $K_{i}$ is generated randomly with a 50% probability of being 0 or 1, every bit of the resulting ciphertext $Y{i}$ also has an exact 50% probability of being 0 or 1.
- This means the ciphertext is uniformly distributed and completely independent of the plaintext distribution. An attacker with infinite computing power learns zero information about the original message from the ciphertext.
- Encryption is also deniable. Given any ciphertext, there exists a valid key that can decrypt it into any arbitrary plaintext of the same length.
- **The three strict rules of OTP:**
	1. The secret key must be at least as long as the message.
	2. The key bits must be uniformly random.
	3. The key must never be reused.
- Because the secret key must be as long as the message, OTP is not practical in the real world. You first need a secure channel to deliver the key, but if you have that channel, you might as well just send the message itself over that channel.
- So far, all the cryptographic methods that we have seen are inefficient either computationally or practically. But when we combine these methods, we get something that's the backbone of modern-day cryptography.
- - -
## Stream Ciphers
- Stream cipher encrypts plain text continuously bit by bit by XORing it with a pseudo-random key stream generated from a secret key.
- **How it works:**
	- Instead of needing a massive, truly random key, a stream cipher takes a short fixed secret key and feeds it into a pseudo-random key generator.
	- The generator expands that short key into an arbitrarily long deterministic sequence of pseudo-random bits called a key stream.
	- The key stream is XORed bit by bit with the plaintext to create ciphertext. Decryption XORs the ciphertext with the same exact key stream to recover the plaintext.
- Because stream ciphers mimic a one-time pad, reusing a key stream is fatal. If two messages are encrypted with the same key stream, an attacker can XOR the two ciphertexts to eliminate the key stream and expose $M_{1} \oplus M_{2}$.
	- The fix is to combine the secret key with a nonce, which is a unique number used only once.
	- $\text{Keystream} = \text{Generator}(\text{Key}\ ||\ \text{Nonce})$ (|| = Concatenation)
	- Every time a new message is sent, a fresh nonce is picked. This ensures that even though the secret key remains the same, the generated key stream is completely different every single time.
- The nonce is usually smaller than or comparable to the key, depending on the cipher design.
- Because the nonce is sent alongside the cipher text in plain text, it doesn't need to be kept secret. Its sole job is to guarantee that the input **(Key, Nonce)** passed into the generator never repeats.
- **Aside:**
	- It may feel tempting to protect the nonce also. This would basically generate two breaking points. So an attacker with access to the key would still not be able to decrypt the message because the nonce is also required to generate the key stream.
	- However, in practical life, this is slightly stupid because if we find a way to pass the secret nouns for each message, we may as well just pass the message over that channel.
- - -
## Block Ciphers
- Blocks are first split plain text into fixed-sized chunks called blocks and encrypted each block individually using round-based operations.
- To make a block cipher secure against cryptanalysis, it relies on repeating two main operations over multiple rounds:
	1. **Confusion:** Obscures the relationship between the key and the ciphertext. Changing a single key bit complexly alters many ciphertext bits.
	2. **Diffusion:** Spreads the statistics of the plain text across the entire ciphertext block. Flipping a single plain text bit flips roughly 50% of the output bits.
- Two catches with block ciphers:
	- If the message is shorter than one block, use padding.
	- If the message is longer than a block, use modes of operation.
- - -
## AES - The Current Standard
- Advanced Encryption Standard (AES) is the industry-standard symmetric block cipher that encrypts data in fixed 128-bit blocks using a secret key through a series of repeating mathematical transformation rounds.
- AES takes a 128-bit chunk of unencrypted data and arranges it into a 4-by-4 grid of bytes called the state matrix.
- It then passes this matrix through multiple iterative rounds of transformation using keys derived from your main secret key.
- What happens in each round:
	1. **SubBytes (Substitution):** Every byte in the 4x4 matrix is swapped with a different byte using a lookup table to create **confusion**.
	2. **ShiftRows (Transposition):** The rows of the matrix are cyclically shifted to the left by different offsets to start spreading the bits around.
	3. **MixColumns (Mixing):** High-level linear algebra is applied to combine the bytes within each column, spreading single-byte changes across the whole column to create **diffusion**.
	4. **AddRoundKey (Key Addition):** The current state matrix is XORed with a unique round key derived from the master key.
- To decrypt the message, the process is simply to run in exact reverse.
- All the specifications and what happens exactly in each round are publicly available, which aligns directly with Kerckhoff's principle.
- - -
## Modes of Operation
- ECB = Electronic Code Block
- This is the simplest and most insecure mode. Each block of plain text is encrypted independently using the exact same key.
	- A major flaw is that if two plain text blocks are identical, their ciphertexts are also identical.
- **ECB1: Fixing ECB**
	- Try to hide repeating patterns by adding feedback. Instead of leaving ciphertext as is, you XOR the encrypted output of block i with the previous block's ciphertext.
	- We can undo the XOR if we get all the ciphertexts. This basically does not improve the security compared to ECB.
- **ECB2: Making it more secure**
	- Shift the feedback to happen before encryption. XOR the current plain text with the previous cipher text block before running it through $E_{K}$.
	- This successfully breaks identical plaintext patterns within a single message because every block now depends on $C_{i-1}$.
	- The first plain text block does not have a previous ciphertext block. Therefore, two different messages that start with the same first block will still output the same first ciphertext block, leaking cross-message patterns.
- **Final Fix: CBC**
	- CBC = Cipher Block Chaining
	- Take ECB2's design and introduce a random initialization vector (IV) to act as $C_0$ for the very first block.
	- Because every new encryption generates a fresh random IV, sending the exact same message twice now yields entirely different ciphertexts from the first block onward.
	- The initialization vector serves as a nonce. They ensure that encrypting the exact same plaintext multiple times yields completely different ciphertexts.
	- CBC mode strictly requires IVs to be generated using a cryptographically secure pseudo-random number generator rather than a simple incrementing counter-nonce. The attacker should not be able to predict what the next IV will be.
- Other modes of operation, like Counter (CTR) and Galois Counter (GCM), exist. Patterns in the plaintext are no longer exposed because these modes involve some kind of feedback among different blocks, but you need an IV.
- The only question remaining to be answered is: how do Alice and Bob share the secret by the way? Do they meet in person or through a diplomatic courier?
- This will be answered in the next lecture.
- - -
## Videos About the Content
1. AES: https://youtu.be/O4xNJsjtN6E?si=fmW8eW023_pBg-xx
2. Modes of Operation: https://youtu.be/Rk0NIQfEXBA?si=NaXZxgmtUvjqnhbx
3. 