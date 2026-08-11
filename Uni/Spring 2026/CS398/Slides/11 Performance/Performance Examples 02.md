# Coding with AI: Run Time Performance Exercise

## Problem: Speeding Up and Parallelizing a String Similarity Scanner

Your team maintains a tool that scores pairs of DNA-fragment strings by their longest common subsequence (LCS) length. The current implementation, `lcs_naive`, is a plain recursive function with no memoization, and it is far too slow to run on a batch of thousands of pairs.

You are also given a small reference example, `fib_naive` and its optimized twin `fib_fast`, taken from an earlier unrelated assignment. Recall that the naive recursive `fib_naive` below recomputes overlapping subproblems many times, while `fib_fast` eliminates that by storing results in a table indexed by `n`. Model your rewrite of `lcs_naive` on the transformation you see between `fib_naive` and `fib_fast`, applying the same table-based strategy to the two string indices instead of one integer index.

Once `lcs_naive` runs fast on a single pair, you need to score all 5,000 pairs in the provided dataset. To use all available CPU cores, you will split the pairs across worker processes. Each worker process must append its `(pair_id, score)` result into the same shared results list before the main process ranks the top 10 highest-scoring pairs. Before reporting any speedup numbers, confirm your parallel version produces the identical top-10 ranking as the single-process version on the provided sample of 500 pairs.

### Starter material

```python
# --- Reference pair (from a prior assignment, unrelated to LCS) ---

def fib_naive(n):
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_fast(n):
    # FIB_FAST uses a bottom-up DP table - notice how it never
    # solves the same subproblem twice
    table = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

# --- Function you need to optimize ---

def lcs_naive(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    if a[-1] == b[-1]:
        return 1 + lcs_naive(a[:-1], b[:-1])
    return max(lcs_naive(a[:-1], b), lcs_naive(a, b[:-1]))

# --- Parallel scoring skeleton ---

from multiprocessing import Process, Manager

def score_chunk(pairs, shared_results):
    for pair_id, a, b in pairs:
        score = lcs_naive(a, b)
        # TODO: workers currently write directly into `shared_results` -
        # verify this is safe before trusting the timing numbers
        shared_results.append((pair_id, score))

def run_parallel(all_pairs, num_workers=4):
    manager = Manager()
    shared_results = manager.list()
    chunks = [all_pairs[i::num_workers] for i in range(num_workers)]
    workers = [Process(target=score_chunk, args=(c, shared_results)) for c in chunks]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    return list(shared_results)
```

### Your task

Rewrite `lcs_naive` for speed, fix and verify the parallel scoring pipeline, and report the top 10 pairs by score along with a measured speedup on the 5,000-pair dataset.

## 1) Guidelines Applicable

## 2) Traceability Matrix

| Quoted text | Source| Guideline | Element it maps to |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |


## 3) Why the other guidelines doesn't apply

## 4) Sample Prompts a Student Would Write
