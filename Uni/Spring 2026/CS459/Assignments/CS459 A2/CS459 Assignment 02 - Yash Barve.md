---
tags:
  - cs459
  - uni
  - s26
---
Name: **Yash Harshal Barve**
Email: yhbarve@uwaterloo.ca
Student ID: **20930353**
- - -
**Q3 (a): Replay Attack**
- Countered using nonces during the handshake, and sequence numbers.
- Nonces:
	- When a client connects, the exchange requires both endpoints to generate random time-independent parameters (`client-nonce` & `server-nonce`)
	- If an attacker tries to replay an earlier handshake message, the server generates a new nonce for the new session. A new 
	- This renders any historical keys obsolete and causes the attacker's handshake confirmation to fail.