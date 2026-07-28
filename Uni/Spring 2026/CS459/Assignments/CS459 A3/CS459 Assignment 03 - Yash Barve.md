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
