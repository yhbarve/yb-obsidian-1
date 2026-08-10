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
	- A protocol secure against active adversaries is also secure against passive ones.
- Any protocol secure against passive adversaries can be turned into a protocol secure for active adversaries by adding protocol steps, proving the correct computation of each message.
	- **Cryptographic Commitments:** Can we detect when a participant deviates from the protocol?
	- **Validations:** Are parameters within expected bounds?
- - -
# Private Information Retrieval (PIR)
- The main question is, can we query a database while remaining completely private?
- If a client has index $i$ and server has a database $d_1, d_2, ..., d_n$,
	- The client should learn about $d_i$.
	- The server should not learn about the index $i$.
- **A blatant non-private protocol:**
	- The user send the index $i$ to the server.
	- The server can then send back $X_i$. However, the server learns about $i$.
- **A trivially private protocol:**
	- The user simply sends a request to the server without mentioning any index.
	- The server sends back all or the entire data set back to the user, and the user can select whichever element it wants to access.
	- This ensures complete privacy.
	- However, if the data set is huge, the server will have to send all the entire data set to every single user making a request, which makes it highly impractical.
## Information-Theoretic PIR
- **Setup & Query Generation:** The user wants to retrieve bit $X_i$. They pick a random subset of indices $Q_1$ that specifically **excludes** $i$, and send $Q_1$ to Server 1.
- **Server 1 Response:** Server 1 computes the XOR sum of all bits indexed in $Q_1$ ($R_1 = \bigoplus_{k \in Q_1} X_k$) and sends the single bit $R_1$ back to the user.
- **Query to Server 2:** The user creates a second query $Q_2$ by adding their desired index $i$ into the first query ($Q_2 = Q_1 \cup \{i\}$), and sends $Q_2$ to Server 2.
- **Server 2 Response:** Server 2 computes the XOR sum of the bits in $Q_2$ ($R_2 = \bigoplus_{k \in Q_2} X_k$) and sends $R_2$ back.
- **Reconstruction:** The user recovers their target bit by XORing the two responses together ($X_i = R_1 \oplus R_2$), because all the overlapping random bits cancel out.
- - -
## Quadratic Residues
- A quadratic residue is a number that has a square root modulo m. Basically, it leaves a specific remainder when some integer is squared and divided by m.
- A number $a$ is a quadratic residue modulo $m$ if you can find an integer $x$ such that $x^2 \equiv a \pmod m$.
- **Example with $m = 7$:**
- Squaring integers gives the remainders: $1^2=1$, $2^2=4$, and $3^2=2$ (and they repeat).
- Because $1, 2,$ and $4$ can be reached by squaring an integer modulo $7$, they are **Quadratic Residues**.
- The numbers $3, 5,$ and $6$ can never be produced as a square modulo $7$, so they are **Quadratic Non-Residues**.
## Computational PIR
- **Setup & Query Generation:** To retrieve bit $X_i$ from an $n$-bit database, the user picks a large random number $m$ and creates a sequence of numbers. For every database index _except_ $i$, they generate a random quadratic residue (QR). For the target index $i$, they insert a quadratic non-residue (QNR) $b_i$.
- **Sending the Request:** The user sends this full mixed sequence of numbers to the server. Because the server cannot computationally distinguish between QRs and QNRs mod $m$, it just sees a sequence of random numbers ($u_1, u_2, \dots, u_n$) and has no idea which position is being targeted.
- **Server Computation:** The server multiplies the query elements raised to the power of their corresponding database bits ($R = u_1^{X_1} \cdot u_2^{X_2} \cdot \dots \cdot u_n^{X_n}$) and sends the result $R$ back to the user.
- **Decoding the Result:** The user checks whether $R$ is a quadratic residue mod $m$. If it is a QR, the target bit $X_i = 0$; if it is a QNR, the target bit $X_i = 1$.
- - -
# CPIR vs IT-PIR
| CPIR                                                   | IT-PIR                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| Possible with single server.                           | Only possible with more than one servers.                    |
| Server needs to perform intensive computations.        | Server may need lightweight computations only.               |
| To break it, the server needs to solve a hard problem. | To break it, the server needs to collude with other servers. |
- - -
# Secret Sharing
- Could we share a piece of information between several parties so that the individual parties learn nothing about it but can work together to recover this information?
- Example: nuclear launch codes
## Secret Sharing Schemes
- Secret sharing splits a secret X among N parties into individual pieces called shares, such that any group of at least T shares can rebuild the secret, while fewer than T shares reveal nothing.
- **Generate():** Sets up the environment and returns public parameters $pp$.
- **Share(pp, x, n, t):** Takes a secret $x$ and splits it into $n$ distinct shares ($x_1, x_2, \dots, x_n$), distributing one to each party ($P_1$ through $P_n$).
- **Reconstruct(pp, $\{x_1, \dots, x_t\}$):** Combines any threshold group of $t$ or more shares to successfully recover the original secret $x$.
- We generally split a secret x into n shares, but for some use cases we might want to retrieve x by combining only t shares. These are called **t-out-of-n** secret sharing schemes.
## N-Out-Of-N Secret Sharing Scheme
- **Share Generation ($Share(x, n, p)$):**
    - Randomly select $n-1$ shares ($s_1, s_2, \dots, s_{n-1}$) from the group field $\mathbb{Z}_p$.
    - Compute the final share as: $s_n = (x - \sum_{i=1}^{n-1} s_i) \pmod p$.
    - Distribute each share $s_i$ to party $P_i$.
- **Secret Reconstruction ($Reconstruct(\{s_1, s_2, \dots, s_n\}, p)$):**
    - Collect all $n$ shares because every single share is required.
    - Sum them up and apply modulo $p$: $x = (\sum_{i=1}^{n} s_i) \pmod p$.
- - -