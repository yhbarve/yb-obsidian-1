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