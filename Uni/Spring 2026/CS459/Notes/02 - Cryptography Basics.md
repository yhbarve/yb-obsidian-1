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
1. Confidentiality
	- Confidentiality ensures that message content remains secret and accessible only to authorized parties, preventing passive adversaries from reading the plain text.
2. Integrity
	- Integrity guarantees that a message has not been altered, tampered with, or corrupted during transit, preventing active adversaries from changing the data undetected.
3. Authenticity
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
	- Encryption: $Y_{i} = X_{i} \oplus K_{i}$ or $y_{i} = x_{i} + k_{i} (\text{mod}\ 2)$
	- Decryption: $X_{i} = Y_{i} \oplus K_{i}$ or $x_{i} = y_{i} + k_{i} (\text{mod}\ 2)$
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
	- $\text{Keystream} = \text{Generator}(\text{Key}\ ||\ \text{Nonce})$ (|| = Concatination)
	- Every time a new message is sent, a fresh nonce is picked. This ensures that even though the secret key remains the same, the generated key stream is completely different every single time.
- The nonce is usually smaller than or comparable to the key, depending on the cipher design.
- Because the nonce is sent alongside the cipher text in plain text, it doesn't need to be kept secret. Its sole job is to guarantee that the input **(Key, Nonce)** passed into the generator never repeats.
