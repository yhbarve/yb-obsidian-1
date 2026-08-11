# Code Generation

### Guideline 1: Size each subtask so you can review every line

**Example:**

> **Problem:** You are building a small command-line tool that reads a JSON config file, validates it against a schema, applies environment-variable overrides, and returns a frozen settings object. 
>
> **Starter material:**
> ```
> # config.json
> {
>   "host": "localhost",
>   "port": 8080,
>   "log_level": "INFO",
>   "features": {"new_ui": false, "beta_api": true}
> }
> ```

> **Answer:**

---

### Guideline 2: Ask for plans as options, not as answers

**Example:**

> **Problem:** You need a Python script that reconciles two CSV files: `transactions.csv` (columns: `id, date, amount, description`) and `bank_statement.csv` (columns: `ref, posted_on, value, memo`). The script must output three files: matched rows, transactions with no bank match, and bank entries with no transaction match. Amounts in `transactions.csv` are signed; bank values are always positive. Match on same date and absolute-value amount.
>
> **Starter material:**
> ```
> transactions.csv:
> id,date,amount,description
> 1001,2025-03-04,-42.50,"Coffee shop"
> 1002,2025-03-05,-120.00,"Grocery"
> 1003,2025-03-05,-15.00,"Tip"
> 1004,2025-03-06,1500.00,"Payroll"
>
> bank_statement.csv:
> ref,posted_on,value,memo
> A1,2025-03-04,42.50,"COFFEE SHOP #42"
> A2,2025-03-05,135.00,"GROCERY+TIP"
> A3,2025-03-06,1500.00,"ACME PAYROLL"
> ```

> **Answer:**
---

### Guideline 3: Ground prompts in your existing codebase

**Example:**

> **Problem:** Your group project is a small Flask web app that already has a `services/` package. The existing `services/users.py` uses `requests` for HTTP, `pydantic` for data models, and a project-specific exception type `ServiceError`. You are adding a new function in `services/billing.py` that calls an external invoicing API and returns a parsed `Invoice` model.
>
> **Starter material:**
> ```python
> # services/users.py (existing, abridged)
> import requests
> from pydantic import BaseModel
> from app.errors import ServiceError
>
> USERS_BASE = "https://api.example.com"
>
> class User(BaseModel):
>     id: int
>     email: str
>
> def fetch_user(user_id: int) -> User:
>     try:
>         r = requests.get(f"{USERS_BASE}/users/{user_id}", timeout=5)
>         r.raise_for_status()
>     except requests.RequestException as e:
>         raise ServiceError(f"users API failed: {e}") from e
>     return User.model_validate(r.json())
> ```

> **Answer:**

---