# What's Multi-Party Computation?
- MPC lets multiple participants calculate an output together while keeping their individual inputs completely private.
- For example, using MPC, a user wanting to analyze a sentence using NLP could interact with another user with model parameters, but wanting to keep those a secret.
- Types of MPC based on number of participants:
	- Two-Party
	- Multi-Party
- - -
# MPC Server Model
- Assume more than three clients with an input.
- Dedicate two or three parties as computation nodes or servers.
- The clients send encrypted versions of their inputs to the servers.
- The servers perform multi-party computation and return partial results to clients.
- Clients decrypt by combing results.
- Types of MPC based on functionality:
	- **Generic functions:** A multi-party computation protocol that can be used for any function.
	- **Specific functions:** A multi-party computation protocol that can only be used for a specific function.
- - -
# Private Set Interactions
- **Private Set Intersection (PSI)** lets different parties find out which items they have in common without revealing any of their non-matching data.
- **2-Party, One-Way PSI ($A \rightarrow B$):** Only one party (typically B) learns the intersection items, while A learns nothing about B's unique set.
- **2-Party, Two-Way PSI ($A \leftrightarrow B$):** Both parties learn the shared items in the intersection securely.
- **n-Party PSI:** Expands the concept to three or more parties (A, B, C...) finding a joint intersection while keeping everyone's individual sets private.
- - -
# Strawman Protocol for PSI
- The Strawman PSI protocol uses homomorphic encryption to compare every element of Alice's set **X** with every element of Bob's set **Y** in a nested loop.
- Step-by-step breakdown:
	- **Initialization:** Alice randomly permutes her set $X$, and Bob randomly permutes his set $Y$ to hide access patterns and element order.
	- **Nested Comparison Loop:** For every element $x \in X$ and every element $y \in Y$, they execute a secure equality test ($x =? y$).
	- **Step 1 (Alice $\rightarrow$ Bob):** Alice sends her encrypted element, $E_A(x)$, to Bob.
	- **Step 2 (Bob's Computation):** Bob chooses a random blinding factor $r$ and computes a combined ciphertext $c = (E_A(x) \cdot E_A(-y))^r$, which homomorphically equates to $E_A((x - y) \cdot r)$.
	- **Step 3 (Bob $\rightarrow$ Alice):** Bob sends the randomized ciphertext $c$ back to Alice; because of the blinding factor $r$, Bob learns nothing about what $x$ was.
	- **Step 4 (Alice's Decryption):** Alice decrypts $c$ using her private key ($D_A(c)$); if the result is $0$, then $x = y$, otherwise the items do not match.
- - -
# Security
- There are two types of MPCs based on security:
	1. **Passive Security:** Each party follows the protocol but keeps a record of all messages after the protocol is over and tries to infer additional information about the other party's inputs.
	2. **Active Security:** Each party may arbitrarily deviate from the protocol. Either the protocol computes **f** or the protocol is aborted.
- Passive Security is a prerequisite for Active Security.
	- A protocol can be secure against passive adversaries but not active ones.
	- 