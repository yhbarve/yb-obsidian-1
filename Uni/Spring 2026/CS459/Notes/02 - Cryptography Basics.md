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
- 