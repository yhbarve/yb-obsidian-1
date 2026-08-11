### Guideline 4: Prompt for Properties and Metamorphic Relations, Not Just Concrete Assertions

**Example:**

> **Problem:** You are testing `run_length_encode`, a function that compresses a string using run-length encoding (e.g., `"aaabbc"` becomes `"3a2b1c"`). A companion `run_length_decode` function reverses it. Encoding and then decoding should always return the original string. Write a prompt that produces property-based tests using Hypothesis instead of hardcoded expected values.
>
> **Starter material (Option A):**
>
> ```python
> def run_length_encode(s: str) -> str:
>     """
>     Return the run-length encoding of s.
>     Each run of consecutive identical characters is replaced by
>     the count followed by the character.
>     Example: "aaabbc" -> "3a2b1c", "" -> ""
>     """
>     if not s:
>         return ""
>     result = []
>     count = 1
>     for i in range(1, len(s)):
>         if s[i] == s[i - 1]:
>             count += 1
>         else:
>             result.append(f"{count}{s[i-1]}")
>             count = 1
>     result.append(f"{count}{s[-1]}")
>     return "".join(result)
>
> def run_length_decode(encoded: str) -> str:
>     """Inverse of run_length_encode."""
>     result = []
>     i = 0
>     while i < len(encoded):
>         count_str = ""
>         while i < len(encoded) and encoded[i].isdigit():
>             count_str += encoded[i]
>             i += 1
>         if i < len(encoded) and count_str:
>             result.append(encoded[i] * int(count_str))
>             i += 1
>     return "".join(result)
> ```


**Answer**


---

### Guideline 5: Generate Regression Tests from Bug Reports and Diffs, Not from General Coverage Goals

**Example:**

> **Problem:** A bug report states: "When `parse_date` receives a date string with a single-digit month (e.g., `'2024-1-5'`), it raises `ValueError` instead of returning the correct date. Dates with two-digit zero-padded months like `'2024-01-05'` work fine." Write a prompt that produces a regression test targeting this exact bug.
>
> **Starter material:**
>

Buggy Code:

import re
from datetime import date

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def parse_date(date_str: str) -> date:
    """
    Parse a date string in YYYY-MM-DD format.
    Returns a datetime.date object.
    Raises ValueError for strings that are not valid dates.
    """
    if not DATE_RE.match(date_str):
        raise ValueError(f"Invalid date format: {date_str!r}")
    year, month, day = (int(p) for p in date_str.split("-"))
    return date(year, month, day)
    

Patched Code:

from datetime import date

def parse_date(date_str: str) -date:
    """
    Parse a date string in YYYY-MM-DD or YYYY-M-D format.
    Returns a datetime.date object.
    Raises ValueError for strings that are not valid dates.
    """
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError(f"Invalid date format: {date_str!r}")
    year, month, day = (int(p) for p in parts)
    return date(year, month, day)

**Answer**

---

### Guideline 6: Be Skeptical of Coverage Numbers Alone. Use Mutation Testing to Check Test Strength

**Example:**

> **Problem:** You have the following `clamp` function and an AI-generated test suite that achieves 100% line coverage. Identify why coverage is high but mutation score is low, then write a mutation-targeted prompt.
>
> **Starter material (Option A):**
>
> ```python
> def clamp(value: float, lo: float, hi: float) -> float:
>     """Return value clamped to the range [lo, hi]."""
>     if lo > hi:
>         raise ValueError(f"lo ({lo}) must be <= hi ({hi})")
>     if value < lo:
>         return lo
>     if value > hi:
>         return hi
>     return value
> ```
>
> AI-generated tests (100% line coverage, poor mutation score):
>
> ```python
> def test_clamp_below():
>     assert clamp(1, 5, 10) == 5      # hits "return lo"
>
> def test_clamp_above():
>     assert clamp(20, 5, 10) == 10    # hits "return hi"
>
> def test_clamp_inside():
>     assert clamp(7, 5, 10) == 7      # hits "return value"
>
> def test_invalid_range():
>     try:
>         clamp(5, 10, 5)
>     except ValueError:
>         pass                          # swallowed: vacuous
> ```

**Answer**

---