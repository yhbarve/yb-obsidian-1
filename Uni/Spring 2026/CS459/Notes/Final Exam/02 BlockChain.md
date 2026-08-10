# Byzantine Fault Tolerance (BFT) in Decentralized Systems
- Consider a chess tournament. 5 players are participating, and we need to find a way to keep records.
- Some of the security challenges to consider are:
	- Confidentiality: Not an issue because data can be accessible for anyone.
	- Availability: Records might get lost, and the data must be explicitly made accessible for all.
	- Integrity: Nobody can be fully trusted. Data should not be manipulated.
- **Solution 1**: Trust Bob for recording results.
	- Availability and integrity are the two risks.
	- Bob might lose the notebook in which he is tracking results, which could affect availability.
	- Bob might cheat and/or manipulate the data, which could lead to inaccuracies.
- **Solution 2**: Each member independently records all the results
	- This fixes the availability issue because it is very unlikely that all the notebooks go missing.
	- However, integrity is still a risk because we need to find a way to ensure that all the books stay synced and up to date.
- **Solution 3**: Each member records all results by following a consensus protocol to keep the data synchronized.
	- This solves the issue related to integrity because an attempt to change the personal notebook is not enough to change the reality.
## Fault Tolerance Level
- **No fault tolerance (NFT)**: The system fails completely if any node crashes, behaves incorrectly, or acts maliciously.
- **Crash Fault Tolerance (CFT):** Handles the case "if a node crashes". No single point of failure. No single source of truth. System cannot handle dishonest nodes. 
- **Byzantine Fault Tolerance (BFT):** Also handles the case "if a node acts maliciously or dishonestly", inherently addresses CFT. Solutions include proof of work or proof of stake.
- - -
# Blockchain
- A blockchain is a chain of blocks.
- Each block contains a cryptographic hash of the total body of the previous block. Therefore, each block cryptographically depends on the previous blocks.
- In version one, the previous blocks hash covers both the header and the payload. To verify, you are forced to fetch the entire prior block, including the payload.
- Version to fix that by dividing the block into a header and a payload.
	- The header contains two critical values:
		- **H**: A cryptographic hash of the previous block's header.
		- **R**: A cryptographic hash of the current block's payload.
	- Now, to verify a previous block, you only fetch the small headers and verify that the value in the current block's **H** matches the hash of the previous block's header. You never touch the payloads.
- Anything can go into the payload. From our previous examples, the chest results could be stored as lines in the payload.
- - -
# Consensus
- Conscious is the answer to how data gets into the block.
- A block is simply a digital container or a batch that stores data and seals them together with cryptographic metadata.
- Instead of writing transactions one by one to a ledger across a distributed network, the network bundles them into a single block to process them as a single step.
- Once the nodes agree via consensus that a block is valid, it gets permanently appended to the shared chain, making its history immutable.
- Nodes are hosting the blockchain. Clients are not necessarily nodes, but they have access to the blockchain.
- Steps involved in adding data to a block:
	1. A transaction is created and signed by a client.
	2. The transaction is sent to one or multiple nodes. The nodes validate the transaction and broadcast it to other nodes.
	3. If all the nodes agree, the block is added right away.
	4. Two nodes may propose a competing block N. Both nodes broadcast their computing versions across the network.
	5. Because network propagation takes time, the network temporarily splits or forks.
	6. If a fork happens, they should choose which block to pick wisely, regardless of their choice.
	7. To resolve this fork, conscientious rules dictate that nodes must eventually follow the longest chain. Whichever branch grows longer first becomes the canonical history, and the shorter branch gets discarded.
- - -
# Proof of Work (PoW)
- Proof of work forces miners to solve a computational puzzle, making history modification prohibitively expensive.
- Without proof of work, altering past transactions requires negligible computational effort.
- To fix this, a rule is added where the block header hash must start with **k** leading zero bits.
- Miners iterate over a nonce value **N** inside the header to continuously change the resulting hash until the target difficulty is met: $\text{Hash}(H \parallel N \parallel \dots \parallel R) = 0x00.._k...$
- **Probability:** For an $m$-bit hash, the probability of finding a valid nonce on a single attempt is $\frac{2^{m-k}}{2^m} = \frac{1}{2^k}$.
- **Expected Work:** A miner expects to perform $2^k$ hash operations to find a single valid block.
- **Bitcoin Implementation:** Uses double SHA-256 ($\text{SHA-256}(\text{SHA-256}(\text{header}))$, adjusting $k$ roughly every 2016 blocks to maintain a 10-minute block time.
- **Incentives:** Miners are compensated via block rewards and transaction fees.
- To construct a valid block, the previous block's header hash and the current block's payload hash remain fixed, while finding the right nonce value takes all the actual computational effort. You combine these three elements, run them through a hash function, and iterate through different nonce values until you successfully generate a final hash that meets the network's requirement of starting with a specific number of zeros.
- How does this protect the changing of history?
	- To rewrite history from 10 blocks ago, an attacker must re-mine that block plus every block after it, racing against the combined power of the rest of the network. Unless they control more than half of the total network hashing power, they will never catch up.
	- You cannot just re-mine a random block N with a new nonce such that the resulting header hash matches the existing header stored in block N + 1. This is prevented by hash function pre-image and second pre-image resistance.
	- **The Catch-Up Race:** If you go back 10 blocks, you must calculate 10 sequential valid nonces. While you are trying to compute those 10 blocks on your local copy, the honest network is working on top of the tip of the existing chain, constantly adding new blocks.
	- **The Hash Power Requirement (51% Attack):** Because block discovery is a probabilistic game based on total hash rate, your speed relative to the rest of the network depends entirely on your percentage of total computational power:
	    - **If you have $< 50\%$ of the network power:** Your branch will grow slower on average than the main chain. The probability of your shorter branch ever catching up and overtaking the main chain approaches zero as the depth increases.
	    - **If you have $> 50\%$ of the network power:** You compute nonces faster than the rest of the network combined. You can eventually build a longer secret branch, broadcast it, and force all honest nodes to reorg to your chain.
- It is always advisable to consider transactions from blocks that reside on the longest branch of a fork and have been further confirmed by additional blocks.
- Mining relies on randomness. A miner with very little hash power can simply get lucky and solve a block first. If an attacker tries to double spend, they might temporarily get lucky and mine a competing block, even without the majority hash power.
- Due to network delays, different parts of the world might see different blocks first. If hash power is spread out, small competing branches happen naturally.
- Therefore, waiting for several subsequent blocks ensures that your transaction is buried under cumulative work, that a competing short-lived fork won't overtake it.
- Example:
	- When Alice pays Bob, her transaction is placed into a block on the blockchain.
	- However, if Bob hands over his goods immediately upon seeing that single block, he risks being scammed.
	- Because mining relies on randomness and network delays can split the chain, an attacker could simultaneously mine a competing block that sends those same funds back to themselves instead.
	- If the network picks up and continues building on the attacker's competing branch, that branch becomes the longer valid chain, and Bob's original block gets completely erased from history.
	- To prevent this, Bob waits for several additional blocks to be mined on top of the block containing his payment. **These additional blocks are called confirmation levels.**
	- Since every node on the network automatically follows whichever valid chain is the longest, each new block stacked on top of Bob's transaction buries it deeper into history.
	- For an attacker to reverse a buried payment, they would have to outpace the rest of the entire network to build an even longer chain from scratch, which becomes virtually impossible as the confirmation count grows.
- Triggering of Fork:
	- Send two transactions to two different nodes in a short time window.
	- Send two transactions to two nodes located in separate sectors of the network.
	- **Selfish Mining:** If you mine a block faster than others, keep it and build on top of it, and only publish it after another block is published by someone else.
### How Networks Protect Against a 51% Attack
Because math alone cannot stop a majority hash-power attack, blockchains rely on economic game theory, social consensus, and higher confirmation thresholds to defend themselves:
- **Massive Economic Cost:** Acquiring over $51\%$ of the hardware and energy for major networks like Bitcoin requires tens of billions of dollars. If an attacker spends that money to double-spend a transaction, they simultaneously destroy public trust in the network—causing the native coin's value to crash to near zero. The attacker burns billions in hardware and electricity just to steal a fraction of that value.
- **Social Reorgs (Hard Forks):** If an attacker attempts to continuously rewrite history, the honest community and node operators can manually flag the attacker's chain as malicious via a software update (a hard fork). The community simply invalidates the attacker's blocks and migrates the honest ledger to a new branch, rendering the attacker's massive ASIC hardware investment completely useless.
- **Extreme Confirmation Levels:** For ultra-high-value transfers (e.g., millions of dollars between exchanges), businesses don't just wait 6 blocks—they might demand 60 or 100+ confirmations, making even a short-lived majority attack too expensive to maintain over time.
- - -
### Drawbacks of PoW
- Speed of confirmation is very slow. A Bitcoin transaction takes on average 10 minutes to confirm. Even worse, it is advised to wait for 6 confirmations (confirmation levels), which takes about an hour.
- Vulnerable to 51% attacks.
- Proof of work is a race of power, relying on the assumption that the collective power of the honest network surpasses a malicious node.
- Proof of work burns energy and negatively impacts the environment.
- - -
# Proof of Stake
- In a proof of stake scheme, collisions are not allowed by design. Only the elected leader proposes a block.
- A node becomes a leader through a weighted random selection process. The probability of being chosen as the leader for a given time slot is directly proportional to the size of the staked financial collateral.
- The network sends valid transactions to the elected leader so that it can construct and publish the block.
- If Node 3 acts dishonestly by proposing a block containing a fraudulent or double-spending transaction, it is considered to be a misbehaviour.
- A node can be punished for its behavior. Its stake can get slashed.
- Misbehaviours are mostly automatically detected and enforced by the blockchain.
	- In some proof-of-stake blockchains, specialized nodes called fishermen can report bad behavior.
	- In rare cases, some blockchains with on-chain governance can make governance-driven slashing, where stakeholders often, via a token-weighted voting system, decide if a node should be punished for behavior that is harder to detect automatically.
## 51% Attack in PoS
- An attacker holding 51% of the stake can exploit the network because leader selection in proof of stake is proportional to the stake. If you own over half the total stake, you get chosen as the elected leader for more than 51% of all block proposals.
- When it is the attacker's turn to propose a block, they simply choose to leave out transactions from specific users or addresses. Because they are the leader for most slots, those transactions get continuously delayed or blocked entirely.
- As the leader, the attacker decides the exact sequence of transactions within a block, allowing them to front-run or back-run users to extract financial value systematically.
- However, an attacker cannot sign a transaction from your private key or create coins out of thin air. They can only manipulate block proposal ordering, inclusion, and chain history.
## PoS Problems
1. **Bootstrapping**
	- A past validator who owned a lot of stake previously goes back in history to the genesis block and secretly signs an entirely new alternative history all the way to the present.
	- Signing blocks requires zero real-world power and electricity, so an attacker can generate millions of fake blocks in seconds.
	- When a brand new user spins up a fresh node for the first time, he receives two valid-looking chains of equal length starting from genesis.
	- Because both chains are properly signed by valid stakeholders at those historical times, Bob has no mathematical way to know which chain is real.
	- In POV, Bob simply measures cumulative heavy computation. Recreating ten years of POP blocks takes ten real years of physical energy, making long-range fake chains impossible to generate instantly.
	- There are no simple solutions to prevent bootstrapping. In some protocols, trusted nodes broadcast the correct block hash or the correct legitimate chain's hash on a daily basis.
	- **A centralized point of trust is by the way the very principles of decentralization.**
2. **The Nothing-At-Stake problem**
	- **How It Starts:** Alice (an attacker with even a small stake, e.g., 1%) gets elected leader and creates a fork by publishing two conflicting blocks ($A \rightarrow B$ and $A \rightarrow D$).
	- **The Incentive Loophole:** In Proof of Work (PoW), splitting your computational hash power across two chains cuts your chances of winning in half. In Proof of Stake (PoS), building on a block costs zero electricity—it is just a digital signature.
	- **The Consequence:** The next honest leader has no financial downside to proposing on **both** forks. By building on all branches simultaneously, the validator guarantees they will get paid no matter which branch eventually wins.
	- **The Exploit (1% Attack):** Because honest validators keep both chains alive for free, Alice can wait until her desired chain gets ahead, append her block there, and kill the opposing chain—allowing her to double-spend.
	- **Solution:** Protocols introduce **Slashing**. If a validator gets caught double-signing (voting/signing on two conflicting blocks at the same height), their locked stake is automatically burned or confiscated.
- - -
