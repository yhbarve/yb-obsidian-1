**Example:**

> **Problem:** You have just cloned a small Flask-style web app (sketch below). A user reports that the site silently rejects passwords longer than 32 characters during signup. Your task is to find where that 32-character limit is being enforced. Show the steps you would take using strategy A, then strategy B, then strategy C, and what fact each step would reveal. Do not just "guess the file": you must justify each move.
>
> **Starter material** (project structure and a few snippets):
>
> ```
> myapp/
>   app.py
>   models/user.py
>   views/auth.py
>   forms/signup.py
>   utils/validators.py
>   tests/test_signup.py
>   tests/test_validators.py
>   config/defaults.yaml
> ```
>
> ```python
> # forms/signup.py  (excerpt)
> class SignupForm(Form):
>     email    = EmailField(validators=[Required(), valid_email])
>     password = PasswordField(validators=[Required(), strong_pw])
>     ...
> ```
>
> ```python
> # utils/validators.py  (excerpt, names only)
> def valid_email(value): ...
> def strong_pw(value): ...
> def _length_ok(value, name): ...
> ```
>
> ```yaml
> # config/defaults.yaml  (excerpt)
> auth:
>   password:
>     min_length: 8
>     max_length: 32
> ```


```
Answer: 



```

---

**Example:**

> **Problem:** Below is a Python function `total(items)` that has been "carefully read" by a teammate, who says it returns the sum of `price * qty` over all items, treating any item with a negative qty as zero. (a) Form your own static-reading prediction for the call `total([{"price": 10, "qty": 3}, {"price": 5, "qty": -2}, {"price": 4, "qty": 2}])`. (b) Now actually run it (or trace it carefully line by line). (c) If the result differs from your prediction, identify which static-reading assumption was wrong.
>
> **Starter material:**
>
> ```python
> def total(items):
>     subtotal = 0
>     for it in items:
>         qty = it.get("qty", 0)
>         if qty < 0:
>             qty == 0   # treat negative qty as zero
>         subtotal += it["price"] * qty
>     return subtotal
> ```

```
Answer: 



```

---

**Example:**

> **Problem:** You are reviewing a junior teammate's pull request that simplifies the function below. They have proposed reordering the two checks, arguing that "checking the cache first is faster, and the validation is the same either way". (a) Without changing the code, list the questions you would investigate before approving or rejecting the reorder. (b) Use the in-file comment as a guide and explain, in one sentence, why the current order is probably load-bearing. (c) State the rationale-recovery steps (commit, issue, author) you would take to be sure.
>
> **Starter material:**
>
> ```python
> # auth/lookup.py  (current code on main)
>
> def resolve_user(token, cache):
>     # IMPORTANT: validate the token BEFORE consulting the cache.
>     # See issue #1247 (cache poisoning, 2019-04). Reordering these
>     # two checks reintroduces the vulnerability.
>     if not validate_token(token):
>         return None
>     if token in cache:
>         return cache[token]
>     user = db_lookup(token)
>     cache[token] = user
>     return user
> ```
>
> ```
> # The PR diff the junior submitted:
>
> -    if not validate_token(token):
> -        return None
> -    if token in cache:
> -        return cache[token]
> +    if token in cache:
> +        return cache[token]
> +    if not validate_token(token):
> +        return None
> ```

```
Answer: 



```

---
