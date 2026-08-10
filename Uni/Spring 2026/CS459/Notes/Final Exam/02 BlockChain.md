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
	4. 