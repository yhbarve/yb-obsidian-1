# Runtime Performance Test Questions
### Coding with AI — Undergraduate Course
### Guideline reference: G1 (Feed the Profiler Output Back Into the Prompt), G2 (Always Verify the Algorithmic Complexity of Generated Code), G3 (Provide Typical Input Characteristics to Prompt Algorithm Switching)

---

## Question 1: Kendall Tau Distance

---

### 1) Problem statement and starter material

#### Problem statement

**Kendall tau distance for a ranking service**

Your team is building a new recommendation service. One piece of it compares two rankings of the same set of items and reports how different they are. The standard measure is the **Kendall tau distance**: the number of pairs of items that the two rankings order differently.

Formally, given two lists `a` and `b` that are permutations of the same `n` distinct items, count the number of unordered pairs `{x, y}` such that `x` comes before `y` in `a` but after `y` in `b`.

This function does not exist yet. You are writing it from scratch as the only function in a new module, and the service has not shipped, so there is no deployed version and no execution history for it. Your job is to produce the first implementation using an AI assistant, and to convince your TA that the implementation you accepted is actually efficient.

**What we know about the calls this function will receive.** The product team logged the request mix from the prototype UI:

- 91% of calls compare two "shortlist" rankings, where `n` is at most 32.
- 9% of calls compare two "full catalogue" rankings, where `n` can be as large as 200,000.

Because the input distribution is known in advance, **do not ask the model for a single general-purpose algorithm.** Ask it for a hybrid implementation that picks between two algorithms at a runtime threshold, and require that the threshold be justified rather than guessed. Both branches must be correct on every legal input, and the small-input branch must not rely on any assumption that would break on a 200,000 element list.

**What you must verify before accepting the code.** Do not assume that a correct solution is also an efficient one. After the assistant gives you an implementation, make it state and justify the time and space complexity of each branch separately, and say at which input size the two branches cross over. Then check that claim yourself by reading the loop nesting and the data structure operations in the generated code, and back it up with the timing harness below. If the assistant claims O(n log n) for the large branch, point at the specific sort, heap, or balanced tree in the code that earns that claim.

**Deliverables.**

1. `kendall_tau.py`, the completed file.
2. `evidence.md`, containing: the complexity you claim for each branch with a one paragraph justification, a table of measured times at n = 1000, 2000, 4000 for the general branch, the doubling ratios you observed, and the measurement that justifies your chosen threshold.
3. The prompts you sent to the assistant, in order.

#### Starter material

`kendall_tau.py`

```python
"""
Kendall tau distance between two rankings.

Both branches must return identical results on every legal input.
Do not change the signature of kendall_tau().
"""

# TODO: pick a value and justify it in evidence.md.
# A number copied from the assistant with no constant-factor argument
# and no micro-benchmark behind it will not be accepted.
THRESHOLD = None

def kendall_tau(a, b):
    """Return the number of discordant pairs between rankings a and b."""
    if len(a) <= THRESHOLD:
        return _small_case(a, b)
    return _general_case(a, b)

def _small_case(a, b):
    """Fast path for the 91% of calls with n <= 32.
    State its time and space complexity in evidence.md.
    """
    raise NotImplementedError

def _general_case(a, b):
    """Path for the 9% of calls with n up to 200,000.
    State its time and space complexity in evidence.md.
    If you claim better than quadratic, the sort, heap, or balanced tree
    that earns that claim must be visible in this function.
    """
    raise NotImplementedError

def reference(a, b):
    """Known-correct but slow. Use only to check the two branches agree.

    WARNING: an earlier draft of this module was advertised as O(n log n)
    but used a .index() call inside its inner loop, which is O(n) in Python
    and quietly made the whole thing quadratic. Read generated code for this
    kind of thing before you believe a complexity claim.
    """
    pos_b = {item: i for i, item in enumerate(b)}
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if pos_b[a[i]] > pos_b[a[j]]:
                count += 1
    return count
```

`harness.py`

```python
import random
import time
from kendall_tau import kendall_tau, _small_case, _general_case, reference

def random_pair(n):
    a = list(range(n))
    b = a[:]
    random.shuffle(b)
    return a, b

def check_agreement():
    """Both branches must match the reference. Include the boundary."""
    sizes = [0, 1, 2, THRESHOLD_MINUS_1, THRESHOLD_VALUE, THRESHOLD_PLUS_1, 500]
    # TODO: fill in the three boundary sizes once you have chosen a threshold,
    # and assert _small_case, _general_case, and reference all agree.

def doubling_test():
    """If time roughly quadruples each time n doubles, the branch is
    quadratic no matter what the assistant claimed."""
    for n in (1000, 2000, 4000):
        a, b = random_pair(n)
        start = time.perf_counter()
        _general_case(a, b)
        print(n, round(time.perf_counter() - start, 4))

def crossover_scan():
    """Time both branches at n = 8, 16, 24, 32, 48, 64, 96, 128 and find
    where the general branch actually overtakes the small branch.
    The measured crossover is what THRESHOLD should be set from."""
    # TODO
```

---

### 2) Traceability matrix

_Complete the traceability matrix below. For each guideline element you applied, quote the exact text from the problem statement or starter material, note where it came from, and identify which guideline and which element of that guideline it maps to._

| Exact quoted text | Source | Guideline | Element of that guideline it maps to |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

### 3) Why the remaining guideline does not apply

_One of the three guidelines (G1, G2, G3) does not apply to this problem. Identify it and explain why, using specific facts about the problem rather than a general statement._

---

### 5) Sample student prompts, annotated

_Write the prompts you would send to an AI assistant to work through this problem, in the order you would send them. Annotate each relevant sentence with the guideline (G1, G2, or G3) it reflects._

---

## Question 2: Calibration Stage of an Ingestion Service

---

### 1) Problem statement and starter material

#### Problem statement

**Speeding up the calibration step in a live telemetry service**

Your team runs an ingestion service for building sensors. Clients POST a batch of raw readings, and before anything is stored, each reading is calibrated: subtract the device offset, multiply by the device scale, clamp the result into the sensor's legal range, and round to three decimals. Every reading in a batch must be calibrated, and the calibrated batch must come back in the same order it arrived.

The service has been in production for eight months and is now too slow at peak. You have been handed the on-call engineer's working copy of the repository as it stood at the end of their shift, including whatever they left in it. Your job is to make the calibration stage faster using an AI assistant, and to get the change through the repository's merge gate. The gate is `make accept`. It is the same command CI runs, you cannot edit the files it depends on, and a change that does not pass it does not count as a solution no matter how fast it is.

**What we know about the batches this endpoint receives.** The gateway logs one line per request, and the traffic team summarised last week as follows:

- 87% of requests are single device heartbeats, where the batch holds 64 readings or fewer.
- 13% of requests are bulk uploads from a gateway that has been offline. These have a median of roughly 900 readings and a documented maximum of 500,000.

The typical batch is therefore nowhere near the largest batch. Do not ask the assistant for one general purpose implementation that has to serve both ends of that range. Ask it for a hybrid that selects between two implementations at a runtime threshold, and give it the percentages above so it can reason about which case it is optimising for.

Ask for the two paths to be separate, clearly named functions, one for the heartbeat case and one for the bulk case, so a reviewer can see at a glance which one runs. Require that both paths produce identical output on every legal batch, including empty batches, and do not let the assistant put a shortcut in the heartbeat path that would give a wrong answer on a 500,000 reading upload.

Do not accept a threshold that the assistant simply picked. Either it derives the number from an argument about the fixed setup cost each path pays per call, or you measure it. Time both paths across batch sizes on both sides of the number you end up with, and report the size at which the bulk path actually starts winning. Then test at the boundary: a batch of exactly `THRESHOLD - 1`, `THRESHOLD`, and `THRESHOLD + 1` readings must all match a known correct reference, so that no batch size falls through a crack between the two paths.

**Deliverables.**

1. `calibration.py`, with the hybrid in place and the public signature unchanged.
2. A clean `make accept` run, with whatever files that command requires you to have produced.
3. Your measured crossover table and the justification for the threshold you chose.
4. The prompts you sent to the assistant, in order, appended to `prompts.md`.

#### Starter material

The working copy contains the following files.

`calibration.py`

```python
"""Calibration stage of the ingest pipeline. Called once per request."""

def calibrate_reading(raw, offset, scale, lo, hi):
    value = (raw - offset) * scale
    if value < lo:
        value = lo
    elif value > hi:
        value = hi
    return round(value, 3)

def calibrate_batch(readings, device):
    """readings: list of floats. device: dict with offset, scale, lo, hi.
    Returns a list of calibrated floats in the same order.
    """
    out = []
    for raw in readings:
        out.append(
            calibrate_reading(
                raw, device["offset"], device["scale"],
                device["lo"], device["hi"],
            )
        )
    return out
```

`Makefile`

```make
BASELINE = perf/baseline.prof.txt
CANDIDATE = perf/candidate.prof.txt

$(CANDIDATE): calibration.py
	python tools/profile_endpoint.py > $@

perf/peak_memory.json: calibration.py
	python tools/memory_probe.py > $@

accept: $(CANDIDATE) perf/peak_memory.json
	python tools/accept.py $(BASELINE) $(CANDIDATE) perf/peak_memory.json

.PHONY: accept
```

`perf/baseline.prof.txt` (committed, produced by `tools/profile_endpoint.py` on the current code)

```
Ordered by: internal time
Total profiled wall time: 27.61 s

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  5417338   14.882    0.000   19.774    0.000 calibration.py:4(calibrate_reading)
    41386    4.334    0.000   24.108    0.001 calibration.py:13(calibrate_batch)
  5417338    2.611    0.000    2.611    0.000 {built-in method builtins.round}
    41386    1.402    0.000    1.402    0.000 ingest.py:88(validate_device)
    41386    0.907    0.000    0.907    0.000 store.py:31(append_rows)
    41386    0.588    0.000    0.588    0.000 ingest.py:52(parse_body)
    41386    0.411    0.000    0.411    0.000 ingest.py:104(emit_metrics)
    82772    0.294    0.000    0.294    0.000 store.py:60(flush)
    41386    0.221    0.000    0.221    0.000 ingest.py:71(auth_check)
    41386    0.190    0.000    0.190    0.000 metrics.py:14(timer)
```

`perf/candidate.prof.txt`

```
(file is empty)
```

`tools/profile_endpoint.py` (read only, enforced by CI)

```python
"""Replays perf/requests.jsonl under cProfile and prints the top 20 lines
in the same format as perf/baseline.prof.txt.

Usage: python tools/profile_endpoint.py > perf/candidate.prof.txt
"""
import cProfile
import pstats

from replay import replay_request_log

def main():
    profiler = cProfile.Profile()
    profiler.enable()
    replay_request_log("perf/requests.jsonl")
    profiler.disable()
    pstats.Stats(profiler).sort_stats("tottime").print_stats(20)

if __name__ == "__main__":
    main()
```

`tools/accept.py` (read only, enforced by CI)

```python
"""Merge gate. Exits non-zero if the change is not acceptable.

Compares a candidate profile against the committed baseline and refuses
changes that do not move the bottleneck, that change observable behaviour,
or that buy speed with unreported memory.
"""
import json
import sys

BOTTLENECK = "calibration.py:13(calibrate_batch)"
MEMORY_CEILING_BYTES = 96 * 1024 * 1024

def share_of_wall_time(profile_path, frame):
    """Returns cumtime for `frame` divided by the total profiled wall time
    reported at the top of the file."""
    ...

def main(baseline_path, candidate_path, memory_path):
    before = share_of_wall_time(baseline_path, BOTTLENECK)
    after = share_of_wall_time(candidate_path, BOTTLENECK)
    print(f"{BOTTLENECK}: {before:.1%} -> {after:.1%}")

    if after >= before - 0.10:
        fail(
            f"bottleneck still holds {after:.1%} of profiled wall time "
            f"(baseline {before:.1%}). the candidate profile does not show "
            f"this frame getting cheaper."
        )

    for name, batch, expected in load_golden_cases("perf/golden/"):
        got = calibrate_batch(batch, DEVICE)
        if got != expected:
            fail(f"golden case {name}: output differs from the recorded run")

    peak = json.load(open(memory_path))["peak_bytes_500k_batch"]
    print(f"peak memory on a 500,000 reading batch: {peak / 1e6:.1f} MB")
    if peak > MEMORY_CEILING_BYTES:
        fail(
            f"peak memory {peak / 1e6:.1f} MB exceeds ceiling. speed bought "
            f"with buffers this large is not an accepted trade here."
        )

    print("ACCEPT")
```

`perf/golden/` (five recorded cases, generated from the current production code before any change)

```
case_01_n3.json         # 3 readings, none clamped
case_02_n19.json        # 19 readings, one clamps low
case_03_n250.json       # 250 readings, values on a rounding boundary
case_04_n4096.json      # 4,096 readings, mixed
case_05_n120000.json    # 120,000 readings, both clamps exercised
```

`tools/memory_probe.py` (read only, enforced by CI)

```python
"""Runs calibrate_batch on a synthetic 500,000 reading batch under
tracemalloc and prints {"peak_bytes_500k_batch": <int>} as JSON."""
```

`prompts.md` (the on-call engineer's log, left in the working copy)

```markdown
## 2026-07-16 22:40  attempt 1
prompt sent: "here is calibration.py, please optimize this file"

got back: helper inlined into the loop, device fields hoisted into locals,
list comprehension instead of append.

result: make accept FAILED
    calibration.py:13(calibrate_batch): 87.3% -> 86.5%
    bottleneck still holds 86.5% of profiled wall time (baseline 87.3%).
    the candidate profile does not show this frame getting cheaper.

notes: 5.4M helper calls did disappear and total wall time dropped about
2 seconds, but the frame's SHARE barely moved, so the gate rejected it.
the model had no idea which frame mattered or by how much. it just made
the code look tidier. i had given it nothing to aim at.

## 2026-07-16 23:15  attempt 2
prompt sent: same file, plus "make it faster, this is the slow part"

got back: essentially attempt 1 again with different variable names.

result: make accept FAILED
    calibration.py:13(calibrate_batch): 87.3% -> 86.9%

notes: asking twice in the same way gets the same answer twice. going
home. whoever picks this up: everything the gate measures is already
sitting in perf/, i just never put any of it in front of the model.

## <your attempts go here>
```

`.github/workflows/ci.yml`

```yaml
jobs:
  gate:
    steps:
      - run: pytest tests/
      - run: make accept
    # tools/ and perf/baseline.prof.txt are protected paths.
    # a PR that modifies them is closed automatically.
```

`tests/test_calibration.py`

```python
"""Existing suite. Must stay green."""
from calibration import calibrate_batch

DEV = {"offset": 0.5, "scale": 2.0, "lo": -10.0, "hi": 10.0}

def test_order_preserved():
    assert calibrate_batch([1.0, 9.0, 3.0], DEV) == [1.0, 10.0, 5.0]

def test_clamps_low():
    assert calibrate_batch([-100.0], DEV) == [-10.0]

def test_rounds_to_three_places():
    assert calibrate_batch([0.5004], DEV) == [0.001]

def test_signature_unchanged():
    import inspect
    from calibration import calibrate_batch as f
    assert list(inspect.signature(f).parameters) == ["readings", "device"]
```

---

### 2) Traceability matrix

_Complete the traceability matrix below. For each guideline element you applied, quote the exact text from the problem statement or starter material, note where it came from, and identify which guideline and which element of that guideline it maps to._

| Exact quoted text | Source | Guideline | Element of that guideline it maps to |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

### 3) Why the remaining guideline does not apply

_One of the three guidelines (G1, G2, G3) does not apply to this problem. Identify it and explain why, using specific facts about the problem rather than a general statement._

---

### 5) Sample student prompts, annotated

_Write the prompts you would send to an AI assistant to work through this problem, in the order you would send them. Annotate each relevant sentence with the guideline (G1, G2, or G3) it reflects._

