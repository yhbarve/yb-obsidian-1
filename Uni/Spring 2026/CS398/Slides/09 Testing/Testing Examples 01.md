### Guideline 1: Anchor Assertions to the Specification, Not to the Code

**Example:**

> **Problem:** You are testing `compound_interest`, a function that computes the final amount after compound interest is applied. The function has a known off-by-one risk in how it handles the number of compounding periods. Write a prompt that will produce assertions grounded in the mathematical specification, not in the code.
>
> **Starter material:**
>
> ```python
def compound_interest(principal: float, rate: float, n: int, t: int) -> float:
    amount = principal
    total_periods = n * t

    # Off-by-one bug: this should run `total_periods` times,
    # but it runs one extra period.
    for _ in range(total_periods + 1):
        amount *= (1 + rate / n)

    return amount
    
> ```
>	  
>     Specification:
>       A = P * (1 + r/n) ** (n * t)
>     where:
>       P = principal
>       r = annual interest rate (decimal, e.g. 0.05 for 5%)
>       n = number of times interest compounds per year
>       t = number of years
>
> 

---

### Guideline 2: Prompt for Boundary and Equivalence-Class Coverage Explicitly

**Example:**

> **Problem:** You are testing `bisect_left` from CPython's standard library. This function returns the leftmost index at which value `x` should be inserted into sorted list `a` to keep it sorted. The signature is `bisect_left(a, x, lo=0, hi=None, *, key=None)`.
>
> **Starter material (Option B):**
>
> Source: CPython `Lib/bisect.py` at tag `v3.12.0`
> URL: https://github.com/python/cpython/blob/v3.12.0/Lib/bisect.py lines 74--107
>
> ```python
> def bisect_left(a, x, lo=0, hi=None, *, key=None):
>     """Return the index where to insert item x in list a, assuming a is sorted.
>
>     The return value i is such that all e in a[:i] have e < x, and all e in
>     a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
>     insert just before the leftmost x already there.
>
>     Optional args lo (default 0) and hi (default len(a)) bound the
>     slice of a to be searched.
>
>     A custom key function can be supplied to customize the sort order.
>     """
>     if lo < 0:
>         raise ValueError('lo must be non-negative')
>     if hi is None:
>         hi = len(a)
>     if key is None:
>         while lo < hi:
>             mid = (lo + hi) // 2
>             if a[mid] < x:
>                 lo = mid + 1
>             else:
>                 hi = mid
>     else:
>         while lo < hi:
>             mid = (lo + hi) // 2
>             if key(a[mid]) < x:
>                 lo = mid + 1
>             else:
>                 hi = mid
>     return lo
> ```


---

### Guideline 3: Tell the Model Which Dependencies to Mock and What Behavior to Stub

**Example:**

> **Problem:** You are testing `get_user_email`, a method that looks up a user in a database and returns their email address. It raises `ValueError` when the user is not found. Write a prompt that produces properly isolated unit tests.
>
> **Starter material (Option A):**
>
> ```python
> # module: user_service.py
>
> class UserService:
>     def __init__(self, db_session):
>         self.db = db_session
>
>     def get_user_email(self, user_id: int) -> str:
>         """
>         Return the email address for the given user_id.
>         Raises ValueError if the user does not exist.
>         """
>         row = self.db.execute(
>             "SELECT email FROM users WHERE id = ?", (user_id,)
>         ).fetchone()
>         if row is None:
>             raise ValueError(f"User {user_id} not found")
>         return row["email"]
> ```

---
