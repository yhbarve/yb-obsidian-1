**Q1.**
**(a)**
- From statistic 2B, the total grades for all male students is $4 \mul 74.5 = $
- - -
**Q4.**
**(a)**
- Using a Merkle tree allows verification of a specific transaction in $O(\text{log}\ n)$ time and requires only $O(\text{log}\ n)$ sibling nodes to be download onto the client (wallet).
- On the contrary, hashing all transactions as a single concatenated string would require downloading all the transactions and re-hashing all of them again to verify. This takes $O(n)$ time and requires $O(n)$ space.

**(b)**
- First, we must compute the hashes for the leaves.
	- $L_1 = H(63) = 6 + 3 = 9$
	- Similarly, $L_2 = 16$, $L_3 = 11$, $L_4 = 11$, $L_5 = 7$, $L_6 = 6$, $L_7 = 10$, and $L_8 = 10$.
- Next, we combine adjacent pairs using concatenation & calculate their hashes
	- $H_{1, 1} = H(L_1 || L_2) = H(916) = 9 + 1 + 6 = 16$
	- Similarly, $H_{1, 2} = 4$, $H_{1, 3} = 13$, $H_{1, 4} = 2$
- We repeat the same process again.
	- $H_{2, 1} = 11$
	- $H_{2, 2} = 6$
- Finally, we calculate the hash of the root.
	- $H_{\text{root}} = H(116) = 8$

**(c)**
- **Head Start:** The selfish miner gets a head start on mining subsequent blocks. Honest miners continue wasting computational power and electricity mining on the publicly known chain, while the selfish miner can move to the next blocks.
- **Invalidating Honest Work:** Whenever honest miners discover a block and threaten catch up, the selfish miner releases their hidden block. The network follows the longest-chain rule; therefore the network adopts the selfish miner's longer chain and abandons the honest miner's blocks.

**(d)**
- In Proof-of-Work, mining requires consuming physical energy and computational power. Miners are economically incentivized to concentrate all their hash power on a single long chain, because mining on a losing fork wastes electricity and other resources with zero payout.
- PoS protocols resolve this by implementing slashing mechanisms. When a validator double-signs, cryptographic evidence of the double vote is submitted to the network. The protocol automatically destroys a portion of the validator's staked collateral and forcibly removes them from the validator set, making the attack economically ruinous.