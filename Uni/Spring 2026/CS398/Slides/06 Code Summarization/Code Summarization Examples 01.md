# Code Summarization

## 1. Guidelines

---

### Guideline 1: Specify the Summary Intent Before Asking

**Example:**

> **Problem:** You are adding docstrings to a utility function in a CPython standard-library module. Reviewers have complained that previous AI-generated docstrings only repeat what the code does and never explain *why* the function exists or *how callers should use it*. Ask an AI assistant to produce a docstring for `os.path.commonpath` that captures its purpose and usage, not just its mechanics.
>
> **Starter material:**
> Source: CPython `Lib/posixpath.py`, pinned commit `v3.12.0`, lines 550-585
> https://github.com/python/cpython/blob/v3.12.0/Lib/posixpath.py#L550-L585
> ```python
> def commonpath(paths):
>     """Given a sequence of path names, returns the longest common sub-path."""
>
>     if not paths:
>         raise ValueError('commonpath() arg is an empty sequence')
>
>     paths = tuple(map(os.fspath, paths))
>     if isinstance(paths[0], bytes):
>         sep = b'/'
>         curdir = b'.'
>     else:
>         sep = '/'
>         curdir = '.'
>
>     try:
>         split_paths = [path.split(sep) for path in paths]
>
>         try:
>             isabs, = set(p[:1] == sep for p in paths)
>         except ValueError:
>             raise ValueError("Can't mix absolute and relative paths") from None
>
>         split_paths = [[c for c in s if c and c != curdir] for s in split_paths]
>         s1 = min(split_paths)
>         s2 = max(split_paths)
>         common = s1
>         for i, c in enumerate(s1):
>             if c != s2[i]:
>                 common = s1[:i]
>                 break
>
>         prefix = sep if isabs else sep[:0]
>         return prefix + sep.join(common)
>     except (TypeError, AttributeError):
>         genericpath._check_arg_types('commonpath', *paths)
>         raise
> ```

> **Answer:**

---

### Guideline 2: Surface the Semantic Facts the AI Cannot See

**Example:**

> **Problem:** You are documenting a helper inside a large monorepo. The function lives in a module whose name carries domain meaning, and it calls a couple of project-specific helpers. Produce a one-paragraph summary that captures the domain intent, not a generic natural-language paraphrase of the loop.
>
> **Starter material:**
> ```python
> # Repository: recsys-platform
> # Module: recsys.ranking.candidate_filters
> # Fully qualified name: recsys.ranking.candidate_filters.drop_stale_candidates
>
> def drop_stale_candidates(candidates, now, ttl_seconds):
>     fresh = []
>     for c in candidates:
>         age = now - c.generated_at
>         if age <= ttl_seconds and not c.is_blacklisted():
>             fresh.append(c)
>     return fresh
> ```

> **Answer:**

---

### Guideline 3: Verify the Summary Against Behaviour, Not Just Plausibility

**Example:**

> **Problem:** You have a utility function and a summary an AI produced for it. The summary sounds polished, but before you paste it into the project you want to check each claim.
>
> **Starter material:**
> ```python
> def dedupe_preserving_order(items):
>     seen = set()
>     out = []
>     for x in items:
>         if x in seen:
>             continue
>         seen.add(x)
>         out.append(x)
>     return out
> ```
>
> AI summary under review:
> "Removes duplicates from the input, returns a sorted list of unique
> items. Runs in O(n log n) time and accepts any iterable, including
> iterables of unhashable elements."

> **Answer:**

---