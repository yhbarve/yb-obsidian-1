# Code Summarization

## 1. Guidelines

---

### Guideline 4: Do Not Trust Surface Fluency as a Quality Signal

**Example:**

> **Problem:** You asked an AI to summarize a small binary-search helper. The returned summary is fluent and confident. Decide whether it is actually useful for a new maintainer.
>
> **Starter material:**
> ```python
> def first_index_ge(sorted_items, target):
>     lo, hi = 0, len(sorted_items)
>     while lo < hi:
>         mid = (lo + hi) // 2
>         if sorted_items[mid] < target:
>             lo = mid + 1
>         else:
>             hi = mid
>     return lo
> ```

Summary: This function performs a search over a list to find a target value. It starts by setting up two pointers, lo and hi, and then repeatedly cuts the search range in half until it zeroes in on the answer. On each pass through the loop it looks at the middle element and shifts the pointers based on what it finds, which is what makes the whole thing so fast. At the end it returns the position of the target in the list, giving you a quick and reliable way to find what you are looking for in sorted data.

> **Answer:**

---

### Guideline 5: Adapt Your Prompt to the Language and Paradigm

**Example:**

> **Problem:** A classmate shares a Prolog predicate and asks you what it does. You want an AI to summarize it, but previous attempts have produced imperative-sounding output that misreads the logic.
>
> **Starter material:**
> ```prolog
> ancestor(X, Y) :- parent(X, Y).
> ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
> ```

> **Answer:**

---

### Guideline 6: Seed Project Style with a Few Local Exemplars

**Example:**

> **Problem:** You have joined a Flask-based web project mid-semester. The project uses a very specific docstring style: one imperative sentence, a blank line, then a `Returns:` line. You want a new helper's docstring to match, without hand-tuning the prompt every time.
>
> **Starter material:**
> ```python
> # Two existing functions and their project-style docstrings:
>
> def load_user(user_id):
>     """Fetch the user row for user_id from the primary database.
>
>     Returns: User instance, or None if no such row exists.
>     """
>     ...
>
> def invalidate_session(session_id):
>     """Delete the session record and evict it from the cache.
>
>     Returns: True if a record was deleted, False otherwise.
>     """
>     ...
>
> # New function that needs a docstring in the same style:
> def rotate_api_key(user_id):
>     old = db.keys.get(user_id)
>     new = secrets.token_urlsafe(32)
>     db.keys.put(user_id, new)
>     cache.delete(f"apikey:{user_id}")
>     audit.log("rotate_api_key", user_id, old_prefix=old[:4])
>     return new
> ```

> **Answer:**

---