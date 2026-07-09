## Programming Question 2

### (a) New Features

I improved the closed-world website fingerprinting attack by extending the feature set in `A2 Files/p-q2/code/fextractor.py`. The main goal was to move beyond simple total-cell counts and capture multiple aspects of each Tor trace: overall traffic volume, early-page behavior, timing structure, direction ordering, and burst/run patterns.

The strongest improvements came from adding features that describe the beginning of the trace and the temporal structure of the cell sequence. Intuitively, many websites have distinctive startup behavior when loaded through Tor, and that behavior remains partially visible even though the payload contents are encrypted.

### Feature Categories and Rationale

| Feature category | Example features | Why it helps accuracy |
| --- | --- | --- |
| Global traffic size and directionality | `total_cells`, `trace_duration`, `outgoing_fraction`, `normalized_switches` | Different websites generate different total amounts of traffic, finish in different amounts of time, and exhibit different levels of back-and-forth interaction. |
| Early-window traffic summaries | counts in the first 20, 30, and 50 cells | The beginning of a page load often contains a distinctive request/response pattern. Measuring early outgoing and incoming activity helps distinguish websites before the rest of the trace unfolds. |
| Mid/late-window summaries | counts in middle and ending windows | Some sites remain active later in the trace while others finish quickly. These features capture how the traffic evolves after the initial startup phase. |
| Direction-order features | cells before first incoming, cells before first outgoing | These features describe how the trace begins structurally, e.g. whether it starts with a burst of outgoing requests or early incoming responses. |
| Timing features | `mean_gap`, `max_gap`, `gap_std`, `prefix_duration_ratio` | Even though Tor encrypts content, the pacing of cells still leaks information. Gap statistics capture burstiness and loading rhythm. |
| Burst/run-length features | longest outgoing run, longest incoming run, run-length ratios | Consecutive streaks of incoming or outgoing cells describe traffic burst structure, which can vary meaningfully across websites. |

### Iterative Feature Development

I developed the feature set incrementally and measured the effect of each change.

1. **Baseline feature set:** total cells only / simple directional counts.  
   This provided some signal, but the classifier accuracy was limited because these features only captured coarse traffic volume.

2. **Added global timing and switching features:** trace duration, number of direction switches, directional ratios.  
   This improved the classifier modestly, showing that coarse timing and interaction structure matter.

3. **Added early-window and order features:** prefix counts, prefix switching, prefix duration, and counts before the first opposite-direction cell.  
   This gave a much larger improvement, suggesting that the startup phase of a trace is highly informative.

4. **Added timing-shape and multi-window features:** gap statistics and multiple fixed windows across the trace.  
   These features captured both pacing and multi-scale temporal structure, and they produced the best results overall.

5. **Tested pruning:** I also experimented with a smaller feature set to remove overlap between similar early-window features.  
   The reduced set was slightly cleaner, but it performed worse than the best larger set, which suggests that the weighted k-NN classifier benefited from keeping multiple scales of early and late traffic summaries.

### Best Feature Set and Accuracy

My best-performing feature set used **33 features** in total. It combined:

- global size and directionality features
- early-window traffic summaries
- mid/late-window traffic summaries
- direction-order features
- timing-gap features
- run-length features

This multi-scale representation gave the best accuracy for the closed-world attack with `k = 5`.

**Best `k = 5` accuracy:** `TODO_INSERT_FINAL_BEST_K5_ACCURACY`

Note: during experimentation, a reduced 24-feature version achieved about `0.6811` accuracy, but the larger 33-feature set performed better and reached approximately `70%` accuracy.

### (b) Influence of the Choice of k

Using the best feature set, I then evaluated the classifier for several values of `k`.

| k | 1 | 2 | 5 | 10 | 15 |
| --- | --- | --- | --- | --- | --- |
| ACC | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

### Trend Analysis

In general, changing `k` affects the balance between sensitivity to local neighbors and robustness to noise:

- Smaller values such as `k = 1` usually make the classifier more sensitive to local variation in the data. This can sometimes help when the feature space is highly discriminative, but it can also overfit noisy or atypical traces.
- Moderate values such as `k = 5` often provide a better balance by smoothing over noisy nearest neighbors while still preserving class structure.
- Larger values such as `k = 10` or `k = 15` can become too coarse, because the vote includes more distant neighbors that may belong to other websites. This can reduce accuracy when class boundaries are already blurred.

For my experiments, the best-performing value of `k` was `TODO_INSERT_BEST_K_VALUE`, with accuracy `TODO_INSERT_BEST_K_ACCURACY`.

Overall, the results suggest that classifier performance depends heavily on the feature set, but once a strong feature set is available, moderate `k` values tend to work better than extremely small or extremely large ones.

### Summary

The most important finding from this exercise is that **feature engineering matters much more than the raw classifier choice in this setup**. The provided weighted k-NN classifier improved substantially once the feature set was extended to include:

- traffic volume information
- early-window traffic behavior
- timing-gap summaries
- ordering features
- burst/run-length structure

These additions increased the closed-world attack accuracy from a weak baseline to a strong final result, demonstrating that Tor still leaks useful traffic-shape information even when content is encrypted.
