### Guideline 4: Land every fix with a failing test and a stated invariant

**Example:**

> **Problem:** A classmate reports that your `remove_duplicates(xs)` helper sometimes returns elements in the wrong order.
>
> **Starter material:**
> ```python
> def remove_duplicates(xs):
>     return list(set(xs))
> ```

> **Answer:**


---

### Guideline 5: Ask the AI to classify its own fix as root-cause or symptom before you accept it

**Example:**

> **Problem:** Your web application's get_user_profile(user_id) raises KeyError in production when user_id is not found in an in-memory cache. The function runs on the request-handling path, so if it raises, the whole request fails with a 500 error.

The contract: `_cache` is meant to mirror the users table. It is loaded at startup and refreshed every 60 seconds by a background thread that re-reads the database. Every user that exists in the database should be present in the cache. A `user_id` that reaches `get_user_profile` always belongs to a real, existing user, because it comes from an authenticated session.

Starter code:
```python_cache = {}   # refreshed every 60s from the users table

def get_user_profile(user_id):
    return _cache[user_id]

def handle_request(request):
    profile = get_user_profile(request.user_id)
    return render_page(profile)
```

You ask an AI to fix the KeyError. It returns this patch:
pythondef get_user_profile(user_id):

```
    if user_id not in _cache:
        return {}          # empty profile so the page still renders
    return _cache[user_id]
```
The AI reports: "Fixed. The KeyError no longer occurs and the request returns 200."

> **Answer:**


---

### Guideline 6: Keep a debugging log so neither you nor the AI loses the thread

**Example:**

> **Problem:** You have been debugging a flaky CI build for 40 minutes with an AI assistant. The build fails with `ImportError: cannot import name 'foo' from 'mymodule'`, but only in CI and only sometimes. You have tried four things already and are getting suggestions that repeat earlier ones.
>
> **Starter material (your current log):**
> ```
> Symptom: CI build fails ~1 in 3 runs with:
>   ImportError: cannot import name 'foo' from 'mymodule' (line 14 of app.py)
> Local: never reproduces.
>
> Tried:
>   T1. Pin mymodule==2.4.0 in requirements.txt.
>       Picked because: pinning isolates version drift (cheapest first check).
>       Result: still flakes, same error.
>   T2. Clear CI cache, rerun.
>       Picked because: stale build artifacts are a classic CI flake cause.
>       Result: still flakes on next run.
>   T3. Add "import mymodule; print(mymodule.__file__)" before the failing import.
>       Picked because: rules out a shadowed local file named mymodule.py.
>       Result: when it fails, the printed path is site-packages/mymodule/__init__.py,
>       same as when it passes. So it is not loading from a shadowed local file.
>   T4. Check for circular imports.
>       Picked because: circular imports can cause "cannot import name" at runtime.
>       Result: import graph is a DAG; mymodule does not import from app.
>
> Still open:
>   H_cache: CI is caching a partially built wheel of mymodule.
>   H_race: two test processes import mymodule simultaneously and one sees a
>           half-initialized module.
> ```

> **Answer:**


---
