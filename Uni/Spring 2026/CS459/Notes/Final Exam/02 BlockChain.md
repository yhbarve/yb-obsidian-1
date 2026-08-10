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
- 
