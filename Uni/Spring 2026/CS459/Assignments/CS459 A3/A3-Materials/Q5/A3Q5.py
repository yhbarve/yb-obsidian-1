#!/usr/bin/env python3

# Combined Blockchain Assignment

# ================ Libraries (DO NOT EDIT) ======================
import pandas as pd
import hashlib
import sys
import json
import os
from typing import List

# ================ Global Variables (DO NOT EDIT) ======================

hash_length = None  # Truncated hash length
leading_zeroes = None    # PoW difficulty (hardness)

# ================ Helper Classes (DO NOT EDIT) ======================

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float, fee: float, size: int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.size = size

    def __repr__(self):
        return f"{self.sender}->{self.receiver}|v:{self.amount}|f:{self.fee}|s:{self.size}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))

# ================ Helper Functions (DO NOT EDIT) ======================

def SHA256(input: str) -> str:
    """This is the only hash function you should use throughout the code."""
    return hashlib.sha256(input.encode()).hexdigest()[:hash_length]

def import_dataset(path: str) -> pd.DataFrame:
    """Imports the transaction dataset."""
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: Could not parse the CSV file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def load_transactions(path: str) -> List[Transaction]:
    """Loads transactions from a CSV file into a list of Transaction objects."""
    df = import_dataset(path)
    return [
        Transaction(
            row['Sender'], row['Receiver'], row['Transaction Amount'],
            row['Transaction Fee'], row['Transaction Size']
        )
        for _, row in df.iterrows()
    ]

def stringify_payload(payload: List[Transaction]) -> str:
    return "|".join([str(tx) for tx in payload])

# ================ Blockchain Class ======================

class Blockchain:
    def __init__(self, watiam_id: str, block_size_limit: int):
        self.watiam_id = watiam_id
        self.block_size_limit = block_size_limit
        self.chain = []
        genesis = self.create_block(nonce=1, previous_hash=SHA256(watiam_id), payload=[])
        # note that we don't mine the genesis block, so we don't check for PoW here
        
        self.chain.append(genesis)
        print(f"================= Genesis Block Generated =================")
        print(f"previous_hash: {genesis['previous_hash']}")
        print(f"===========================================================")

    def hash_block(self, block: dict) -> str:
        """Computes a truncated SHA-256 hash of a block."""
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()[:hash_length]

    def create_block(self, nonce: int, previous_hash: str, payload: List[Transaction]) -> dict:
        """Creates a new block dict."""
        return {
            'previous_hash': previous_hash,
            'nonce': nonce,
            'payload_hash': SHA256(stringify_payload(payload))
        }

    def get_last_block(self) -> dict:
        """Returns the last block in the chain."""
        return self.chain[-1]

    def add_block(self, block: dict, index: int) -> None:
        """Validates and adds a block to the chain."""
        condition_1 = block['previous_hash'] == self.hash_block(self.get_last_block())
        condition_2 = self.hash_block(block).startswith('0' * leading_zeroes)
        if condition_1 and condition_2:
            self.chain.append(block)
        else:
            print(f"ERROR: proposed block at index {index} is not valid")
            sys.exit(1)

    # ---- Phase 1: Greedy Packing ----

    def pack_block(self, transactions: List[Transaction], start_index: int):
        """
        Greedily packs transactions into a block payload.

        Args:
        - transactions: Full list of transactions (order matches the CSV)
        - start_index: Index to start packing from

        Returns:
        - (payload, next_index): The packed payload and the next unprocessed index
        """
        # TODO: Implement greedy packing
        payload = []

        current_size = 0
        index = start_index

        while (index < len(transactions) and current_size + transactions[index].size <= self.block_size_limit):
            payload.append(transactions[index])
            current_size += transactions[index].size
            index += 1
        
        return (payload, index)

    # ---- Phase 2: Mining ----

    def mine_block(self, payload: List[Transaction], previous_hash: str, block_index: int) -> dict:
        """
        Mines a valid block by finding a nonce that satisfies PoW.

        Args:
        - payload: List of transactions for this block
        - previous_hash: Hash of the previous block
        - block_index: Index of this block in the chain (for display)

        Returns:
        - A valid mined block dict
        """
        
        nonce = 0
        while True:
            candidate_block = self.create_block(nonce, previous_hash, payload)
            if (self.hash_block(candidate_block).startswith('0' * leading_zeroes)):
                return candidate_block
            nonce += 1

    def mine_chain(self, transactions: List[Transaction]) -> None:
        """
        Packs all transactions into blocks and mines each one.

        Args:
        - transactions: Full list of transactions

        Returns:
        - None (appends blocks to self.chain and dumps nonces to file)
        """
        
        current_index = 0
        blocks = 1
        while (current_index < len(transactions)):
            payload, current_index = self.pack_block(transactions, current_index)
            previous_hash = self.hash_block(self.get_last_block())
            block = self.mine_block(payload, previous_hash, blocks)
            self.add_block(block, blocks)
            print(f"Block {blocks} mined: {block}")
            print(f"===========================================================")
            blocks += 1
        self.dump_nonces()


    # ---- Phase 3: Collision ----

    def find_collision(self, fraudulent_payload: List[Transaction]) -> dict:
        """
        Finds a collision block that hashes to the same value as the last block,
        but contains a fraudulent payload.

        The collision block must:
        - Share the same previous_hash as the last block
        - Have a different nonce than the last block
        - Hash to the same truncated SHA-256 value as the last block

        Args:
        - fraudulent_payload: Fraudulent transactions to embed in the collision block

        Returns:
        - The collision block dict
        """

        real_last_block = self.get_last_block()
        target_hash = self.hash_block(real_last_block)
        prev_hash = real_last_block['previous_hash']

        nonce = 0
        while True:
            candidate_block = self.create_block(nonce, prev_hash, fraudulent_payload)
            if (self.hash_block(candidate_block) == target_hash):
                self.dump_collision(candidate_block)
                return candidate_block
            nonce += 1
        return None

    # ---- Dump & Load ----

    def dump_nonces(self, save_file="blockchain.txt") -> None:
        """Saves WatIAM ID and each block's nonce to file (skips genesis)."""
        with open(save_file, 'w') as f:
            f.write(f'{self.watiam_id}\n')
            for block in self.chain[1:]:
                f.write(f'{block["nonce"]}\n')
        print(f"Nonces saved to {save_file}")

    def dump_collision(self, collision_block: dict, save_file="collision.txt") -> None:
        """Saves the collision block's nonce to file."""
        with open(save_file, 'w') as f:
            f.write(f'{self.watiam_id}\n')
            f.write(f'{collision_block["nonce"]}\n')
        print(f"Collision saved to {save_file}")

    def load_from_dump_file(self, transactions: List[Transaction], fraudulent_payload: List[Transaction],
                             save_file="blockchain.txt", collision_file="collision.txt") -> None:
        """
        Reconstructs and validates the blockchain from saved nonces.
        Used by the grader to evaluate submissions.
        """
        with open(save_file, 'r') as f:
            lines = list(map(str.strip, f.readlines()))

        nonces = list(map(int, lines[1:]))

        # Reconstruct and validate each block from nonces + original transactions
        tx_index = 0
        for i, nonce in enumerate(nonces):
            payload, tx_index = self.pack_block(transactions, tx_index)
            previous_hash = self.hash_block(self.get_last_block())
            block = self.create_block(nonce, previous_hash, payload)
            self.add_block(block, i + 1)

        print("SUCCESS: blockchain loaded and validated!")

        # Validate collision file
        if os.path.exists(collision_file):
            with open(collision_file, 'r') as f:
                collision_lines = list(map(str.strip, f.readlines()))

            collision_nonce = int(collision_lines[1])
            target_block = self.get_last_block()
            target_hash = self.hash_block(target_block)
            collision_block = self.create_block(collision_nonce, target_block['previous_hash'], fraudulent_payload)
            if self.hash_block(collision_block) == target_hash:
                print("SUCCESS: collision is valid! Good job!")
            else:
                print("ERROR: collision is invalid. Try again.")
        else:
            print("ERROR: no collision file found.")

# ================ Unit Tests (DO NOT EDIT) ======================

def test_block_size_limit(blockchain: Blockchain, transactions: List[Transaction]) -> bool:
    tx_index = 0
    for i, block in enumerate(blockchain.chain[1:]):
        payload, tx_index = blockchain.pack_block(transactions, tx_index)
        total_size = sum(tx.size for tx in payload)
        if total_size > blockchain.block_size_limit:
            print(f"Block#{i+1} exceeds block_size_limit.")
            return False
    return True

def test_hardness(blockchain: Blockchain) -> bool:
    for i, block in enumerate(blockchain.chain[1:]):
        if not blockchain.hash_block(block).startswith('0' * leading_zeroes):
            print(f"Block#{i+1} fails hardness check.")
            return False
    return True

def test_all_transactions_included(blockchain: Blockchain, transactions: List[Transaction]) -> bool:
    tx_index = 0
    block_transactions = []
    for block in blockchain.chain[1:]:
        payload, tx_index = blockchain.pack_block(transactions, tx_index)
        block_transactions.extend(payload)
    if set(block_transactions) != set(transactions):
        print("Mismatch between original and block transactions.")
        return False
    return True

def test_collision_valid(blockchain: Blockchain, fraudulent_payload: List[Transaction],
                         collision_file="collision.txt") -> bool:
    if not os.path.exists(collision_file):
        print("No collision file found.")
        return False
    with open(collision_file, 'r') as f:
        lines = list(map(str.strip, f.readlines()))
    input_watiam_id = lines[0]
    collision_nonce = int(lines[1])
    target_block = blockchain.get_last_block()
    target_hash = blockchain.hash_block(target_block)
    collision_block = blockchain.create_block(collision_nonce, target_block['previous_hash'], fraudulent_payload)
    if blockchain.hash_block(collision_block) != target_hash:
        print("Collision hash does not match target.")
        return False
    if collision_nonce == target_block['nonce']:
        print("Collision nonce must differ from original nonce.")
        return False
    if input_watiam_id != blockchain.watiam_id:
        print("Collision ID must be the same as the blockchain's WatIAM ID.")
        return False
    return True

def unit_tests(blockchain: Blockchain, transactions: List[Transaction], fraudulent_payload: List[Transaction]):
    print("\n\nUnit Tests:\n" + "%" * 30)
    print(f"test_block_size_limit:           {test_block_size_limit(blockchain, transactions)}")
    print(f"test_hardness:                   {test_hardness(blockchain)}")
    print(f"test_all_transactions_included:  {test_all_transactions_included(blockchain, transactions)}")
    print(f"test_collision_valid:            {test_collision_valid(blockchain, fraudulent_payload)}")
    print("%" * 30)

# ================ Main ======================

def main():
    global hash_length, leading_zeroes
    if len(sys.argv) != 5:
        print("Usage: assignment <WatIAM> <path_to_transactions.csv> <hash_length> <block_size_limit>")
        sys.exit(1)

    watiam_id = sys.argv[1]
    dataset_path = sys.argv[2]
    hash_length = int(sys.argv[3])
    block_size_limit = int(sys.argv[4])
    
    leading_zeroes = hash_length - 2  # Set global variable for PoW difficulty

    transactions = load_transactions(dataset_path)
    fraudulent_payload = load_transactions("fraudulent.csv")

    # Phase 1 + 2: Pack and mine chain
    blockchain = Blockchain(watiam_id, block_size_limit)
    blockchain.mine_chain(transactions)

    # Phase 3: Find collision
    blockchain.find_collision(fraudulent_payload)

    # Student self-evaluation
    unit_tests(blockchain, transactions, fraudulent_payload)

    # Grader evaluation (reconstructs everything from dump files)
    print("\n\nGrader Evaluation:\n" + "%" * 30)
    testing_blockchain = Blockchain(watiam_id, block_size_limit)
    testing_blockchain.load_from_dump_file(transactions, fraudulent_payload)

if __name__ == "__main__":
    main()