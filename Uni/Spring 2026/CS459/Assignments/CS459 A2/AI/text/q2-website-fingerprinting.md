## Programming Question 2

### (a) New Features

I improved the closed-world website fingerprinting attack by extending the `extract()` function in `A2 Files/p-q2/code/fextractor.py`. The starter code used a single feature (the total number of cells), which only captures coarse page size. My goal was to describe each Tor cell sequence along several independent axes: overall traffic volume, direction balance, behavior in different phases of the page load, the order in which requests and responses appear, timing rhythm, and burst structure.

The key intuition is that even though Tor encrypts the content and hides the destination, it preserves the *timing and direction* of cells to keep browsing interactive. Those patterns leak the "shape" of a page load, and different websites have distinctive shapes.

I deliberately kept the final feature set small (13 features) and removed features that were strongly correlated with one another, so that each remaining feature contributes distinct information and can be explained on its own.

### Final Feature Set and Rationale

| # | Feature | Category | How it helps accuracy |
| --- | --- | --- | --- |
| 1 | `total_cells` | Volume | Different sites transfer different total amounts of data, so overall size is a strong first discriminator. |
| 2 | `trace_duration` | Volume/timing | Some pages finish loading quickly while others take much longer; total elapsed time separates them. |
| 3 | `outgoing_fraction` | Directionality | Fraction of cells that are outgoing. Captures whether a page is interaction/request-heavy or content-heavy. Kept as a bounded value in [0, 1], which behaves better in the distance-based k-NN than an unbounded outgoing/incoming ratio. |
| 4 | `normalized_switches` | Directionality | Direction switches divided by total cells. Measures how "chatty" (back-and-forth) the exchange is, independent of trace length. |
| 5 | `first20_outgoing_cells` | Early window | Size of the initial request burst at the very start of the load, which reflects how a page bootstraps. |
| 6 | `first50_incoming_cells` | Early window | How much content the server pushes back early in the load. |
| 7 | `mid_incoming_cells` | Mid window | How much content is still streaming in the middle of the load (cells 30–100), separating quick pages from content-heavy ones. |
| 8 | `last50_outgoing_cells` | Late window | Whether the client is still issuing requests near the end of the load. |
| 9 | `outgoing_before_first_incoming` | Direction order | Number of outgoing (request) cells sent before the first incoming (response) cell arrives, describing the page's startup handshake structure. |
| 10 | `mean_gap` | Timing | Average inter-arrival time between cells, capturing the overall pacing of the load. |
| 11 | `gap_std` | Timing | Standard deviation of inter-arrival times, capturing burstiness vs. a steady stream. |
| 12 | `longest_outgoing_run` | Burst | Longest uninterrupted streak of outgoing cells (biggest request burst). |
| 13 | `longest_incoming_run` | Burst | Longest uninterrupted streak of incoming cells (biggest content burst). |

### Removing Redundant Features

While tuning, I found that several intuitive features were strongly correlated with others and did not add independent signal, so I removed them:

- **`outgoing/incoming` counts alongside `outgoing_fraction`:** the raw counts and the fraction encode the same directional balance, so I kept only the bounded fraction.
- **Paired direction counts inside a fixed window** (e.g. `first20_incoming_cells` when `first20_outgoing_cells` is present): within a fixed-size window the two are near-complements, so keeping both is redundant.
- **`incoming_before_first_outgoing`:** Tor traces almost always begin with outgoing request cells, so this was nearly constant and carried little information.
- **Run-length ratios** (`longest_run / total_cells`): derivable from features already in the set, so I kept only the raw run lengths.

### Iterative Development and the Size/Accuracy Trade-off

I built the feature set incrementally and measured accuracy (closed-world, `k = 5`) at each step. I also explored both larger and smaller sets to understand the trade-off between accuracy and simplicity:

| Feature set size | Accuracy (k = 5) |
| --- | --- |
| 3 (basic counts) | 0.36 |
| 8 | 0.40 |
| 14 | 0.49 |
| ~20 | 0.52 |
| 33 | ~0.70 |
| 24 | 0.68 |
| 16 | 0.667 |
| 10 | 0.63 |
| **13 (final)** | **0.67** |

A larger 33-feature set reached the highest raw accuracy (~70%), but many of those features overlapped and were hard to justify individually. Aggressively pruning to 10–11 features dropped accuracy to 60–63%. The final 13-feature set recovers essentially all of the accuracy of the larger sets (0.67) while remaining compact and easy to explain, which is why I selected it as my final set.

### (b) Best Feature Set and Influence of k

Using the final 13-feature set, I ran the closed-world attack for several values of `k`:

| k | 1 | 2 | 5 | 10 | 15 |
| --- | --- | --- | --- | --- | --- |
| ACC | 0.875 | 0.79 | 0.67 | 0.54 | 0.45 |

**Best accuracy:** `0.875` at `k = 1`.

### Trend Analysis

Accuracy decreases monotonically as `k` increases, and is highest at `k = 1`. This happens because:

- With 100 monitored classes and 90 loads each, the feature set is discriminative enough that the *single* nearest neighbor of a test trace is usually another load of the same website. At `k = 1` the classifier simply trusts that closest match, which is correct most of the time.
- As `k` grows, the majority vote pulls in neighbors that are further away. Because there are many classes and the per-class clusters are relatively tight, those additional neighbors increasingly belong to *other* websites and dilute the correct label. Each extra neighbor is more likely to add noise than to reinforce the right class.
- By `k = 10` and `k = 15`, the vote is dominated by these more distant, wrong-class neighbors, so accuracy drops substantially (0.54 and 0.45).

In short, for this closed-world setup the classification benefits from very local decisions, so small `k` performs best and larger `k` over-smooths across class boundaries. (Larger `k` values are typically more useful when classes overlap heavily or when the training data is noisy, which is not the dominant regime here.)

### Summary

The main takeaway is that feature engineering, not classifier complexity, drives performance in this setup. Extending the feature set from a single cell count to a compact set of 13 features spanning volume, directionality, phase-based window counts, direction ordering, timing rhythm, and burst structure raised closed-world accuracy from 0.36 to 0.67 at `k = 5`, and up to 0.875 at `k = 1`. This demonstrates that Tor still leaks substantial traffic-shape information even though it encrypts content and hides the destination.
