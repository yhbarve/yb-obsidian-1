**Q4.**
**(a)**
- Using a Merkle tree allows verification of a specific transaction in $O(\text{log}\ n)$ time and requires only $O(\text{log}\ n)$ sibling nodes to be download onto the client (wallet).
- On the contrary, hashing all transactions as a single concatenated string would require downloading all the transactions and re-hashing all of them again to verify. This takes $O(n)$ time and requires $O(n)$ space.

**(b)**
- 