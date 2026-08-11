# Code Generation

### Guideline 4: Drive generation with executable tests

**Example:**

> **Problem:** You are building a helper that groups a list of events by calendar week (Monday-to-Sunday, ISO 8601). The function should be called `group_by_week(events)` where each event is a dict with at least a `"date"` key holding an ISO date string, and it must return a dict mapping `(iso_year, iso_week)` to the list of events that fall in that week.
>
> **Starter material:**
> ```python
> # Sample events
> events = [
>     {"id": 1, "date": "2024-12-30", "title": "Sprint planning"},  # Mon of ISO week 1 of 2025
>     {"id": 2, "date": "2025-01-05", "title": "Retro"},            # Sun of ISO week 1 of 2025
>     {"id": 3, "date": "2025-01-06", "title": "Standup"},          # Mon of ISO week 2 of 2025
>     {"id": 4, "date": "2024-01-01", "title": "Kickoff"},          # ISO week 1 of 2024
> ]
> ```

> **Answer:**

---

### Guideline 5: Specify preconditions, postconditions, and edge cases

**Example:**

> **Problem:** You are asked to write a Python function `decimal_to_binary(n)` that returns the binary representation of an integer as a string, with no leading zeros. The function will be used inside a larger number-formatting library, so its behavior on negative numbers and on zero must be precise.
>
> **Starter material:**
> ```python
> def decimal_to_binary(n):
>     """Write a function to convert the given decimal number to its binary
>     equivalent, represented as a string with no leading zeros."""
> ```

> **Answer:**

---

### Guideline 6: Have the model critique its own output before you run it

**Example:**

> **Problem:** You asked the model to write a Python function `parse_duration(s)` that takes a string like `"1h30m"`, `"45m"`, `"2h"`, or `"15s"` and returns the total number of seconds as an int. The model has just produced a 12-line implementation. You have not run it yet.
>
> **Starter material:**
> ```python
> # The implementation the model just produced:
> import re
>
> def parse_duration(s: str) -> int:
>     pattern = r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
>     m = re.match(pattern, s)
>     hours = int(m.group(1) or 0)
>     minutes = int(m.group(2) or 0)
>     seconds = int(m.group(3) or 0)
>     return hours * 3600 + minutes * 60 + seconds
> ```

> **Answer:**

---