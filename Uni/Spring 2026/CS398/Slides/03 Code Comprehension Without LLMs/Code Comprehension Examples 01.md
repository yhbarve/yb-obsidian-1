**Example:**

> **Problem:** A user has filed bug #4421 against your team's web application. The reproduction steps are below. You have not seen this codebase before. Before you open a single source file, write down the 3 to 5 specific code-comprehension questions you will use to drive your reading. 
>
> **Starter material** (the bug report):
>
> ```
> Bug #4421: "Logout link still works after session expires"
>
> Repro:
>   1. Log in as a normal user.
>   2. Wait 31 minutes (session timeout is configured to 30 min).
>   3. Click "Logout" in the navbar.
>
> Expected: The user is shown the "Your session has expired, please
>   log in again" page.
> Actual:   The user sees the normal "You have been logged out" page,
>   as if their session had still been active. No 401 is logged on
>   the server.
>
> Code layout the bug reporter mentions:
>   - middleware/session.py
>   - middleware/auth.py
>   - views/logout.py
>   - templates/expired.html
>   - templates/logged_out.html
> ```

```
Answer: 



```

---

**Example:**

> **Problem:** Below is a small Python function from a data-loading library. You have never seen it before. (a) Write a one-sentence top-down hypothesis based only on its signature and the comment on line 1. (b) Read the body and decide whether your hypothesis is correct, partly correct, or wrong. (c) If it is wrong or partly wrong, drop to bottom-up: pick one execution and trace what `out` looks like after each iteration. (d) Write the corrected one-sentence description.
>
> **Starter material:**
>
> ```python
> # Merge consecutive duplicates in a stream of records.
> def squash(records, key=lambda r: r):
>     out = []
>     for r in records:
>         if out and key(out[-1]) == key(r):
>             out[-1] = r
>         else:
>             out.append(r)
>     return out
> ```

```
Answer: 



```

---

**Example:**

> **Problem:** Below is a small Python function `group_by_minute` and a helper it calls, `minute_of`. (a) Without tracing the body, write a one-sentence summary of what `minute_of` returns. (b) Then list every variable in `group_by_minute` and assign each one a role from the standard role set (or a short phrase if none fits). (c) Using only your labels, write a one-sentence description of what `group_by_minute` does. (d) Now do a quick trace on `timestamps = [10, 30, 65, 70, 130]` with `tz_offset = 0` to confirm the description.
>
> **Starter material:**
>
> ```python
> def group_by_minute(timestamps, tz_offset=0):
>     groups = []
>     bucket = []
>     last_minute = None
>     for t in timestamps:
>         m = minute_of(t, tz_offset)
>         if last_minute is None or m == last_minute:
>             bucket.append(t)
>         else:
>             groups.append(bucket)
>             bucket = [t]
>         last_minute = m
>     if bucket:
>         groups.append(bucket)
>     return groups
>
> def minute_of(t, tz_offset):
>     return (t + tz_offset) // 60
> ```

```
Answer: 



```

---