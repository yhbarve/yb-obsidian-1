### Guideline 1: Prepare small, well-described changes. The PR description is now a prompt too.


**Example:**

> **Problem:** You are a student on a group project building a Flask-based class discussion board. You have finished adding a rate-limit feature on the POST /posts endpoint to stop spam. Before opening a PR for AI review, you need to decide how many PRs to open, what goes in each one, and how to describe each one.
>
> **Starter material** (the change you made; assume 280 lines across 6 files):

> rate_limit/limiter.py (new, 80 lines): a RateLimiter class with one public method, allow(key, limit, window_seconds) -> bool. Internally it keeps a dict called _buckets mapping key to a list of timestamps, and wraps access to _buckets in a threading.Lock because the Flask app runs with multiple worker threads. Entries are never removed from _buckets, so memory grows over time. There is no disk or network I/O anywhere in allow(), since it's called on every request.
> rate_limit/__init__.py (new, 3 lines): exports RateLimiter.
> app/routes/posts.py (modified, +25 lines): wires the limiter onto POST /posts, reading the limit from RATE_LIMIT_DEFAULT. This is the change tied to issue #47 ("spam posts in discussion threads").
> app/routes/auth.py (modified, +10 lines): you also wired the limiter onto POST /login because "might as well while I'm here." Nobody asked for this and it isn't tied to issue #47.
> app/config.py (modified, +5 lines): adds a RATE_LIMIT_DEFAULT constant.
> tests/test_limiter.py (new, 130 lines): unit tests covering the allow/deny boundary and window rollover, plus one test that spins up 20 threads hitting allow() concurrently to check the lock is correct. Also includes one integration test that hits POST /posts and reuses a shared test fixture, but the fixture needed restructuring to support it.
> tests/conftest.py (modified, +27 lines): the restructured fixture from above. This fixture is also used by roughly a dozen unrelated tests elsewhere in the suite, so changing it has a blast radius beyond rate limiting.

> One more thing you know but haven't written down anywhere: you considered using Redis to back the limiter instead of an in-memory dict, since Redis would survive a server restart and work across multiple app instances. You decided against it because the app doesn't have Redis in its stack yet, and adding it felt out of scope for this PR.


**Answer**

---

### Guideline 2: Feed the reviewer the surrounding code, not just the diff.

**Example:**

**Problem**: You are reviewing a change to an Order class in an e-commerce backend. The PR adds a discount_code field to Order so that customer receipts can show which promo code was applied. Before sending the change to an AI reviewer, you need to decide what to include in the review prompt.

**Starter material**
```
python# order.py (full file before the change)
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    order_id: int
    user_id: int
    items: List[str]
    total: float

def to_receipt_dict(order: Order) -> dict:
    """Build the dict passed to the receipt-rendering template."""
    return {
        "order_id": order.order_id,
        "user_id": order.user_id,
        "items": order.items,
        "total": order.total,
    }

def validate_order(order: Order) -> bool:
    return order.order_id > 0 and order.total >= 0
    
```

```
Diff submitted in the PR:
diff from dataclasses import dataclass
-from typing import List
+from typing import List, Optional

 @dataclass
 class Order:
     order_id: int
     user_id: int
     items: List[str]
     total: float
+    discount_code: Optional[str] = None

```

PR description: "Add discount_code to Order so receipts can show which promo code the customer used. Marketing wants this live before the weekend sale."
Known caller (from checkout.py):
pythonreceipt_data = to_receipt_dict(order)
render_template("receipt.html", **receipt_data)

**Answer**

---

### Guideline 3: Run the review as two passes. Understand first, then critique against a rubric.

**Example:**

> **Problem:** Your team is building a Flask API for event ticket booking. A teammate opened a PR that adds a seat reservation endpoint. In the last sprint, your AI reviewer went straight to critique mode and flagged the if/else structure as "could be a ternary" while missing a bug that let two people book the same seat. This sprint you are switching to a two-pass review: first have the AI explain what the code does and what it's supposed to guarantee, then have it critique against a rubric.
>
> **Starter material** (the diff under review):
>
> ```python
# reservations.py (new endpoint added in this PR)
from flask import request, jsonify
from .models import Event, Reservation, db

def reserve_seats(event_id):
    data = request.get_json()
    num_seats = data["num_seats"]
    event = Event.query.get(event_id)

    if event.seats_available >= num_seats:
        event.seats_available -= num_seats
        db.session.add(Reservation(event_id=event_id, seats=num_seats))
        db.session.commit()
        return jsonify({"status": "confirmed"})
    else:
        return jsonify({"status": "sold_out"})
> ```

**Answer**

---