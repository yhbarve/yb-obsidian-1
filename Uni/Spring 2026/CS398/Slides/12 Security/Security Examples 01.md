## 1) Problem statement and starter material

### Problem statement

**Hardening an internal report download endpoint.**

Your team runs a small internal Flask service. One endpoint lets a logged-in employee download a saved report file by name. The current draft of that endpoint is in `naive_reference.py` below. It works, and it is insecure.

The security team has already held its threat modelling session for this endpoint. Their signed-off table is included below as `THREAT_TABLE.md` and is delivered to you as part of the ticket. It is the table the security team will use when they audit your work, so treat it as your specification.

Use an AI coding assistant to produce your submission. In your answer booklet, write out **every prompt you send to the assistant**, in order, plus the final files you would submit. You are graded on the prompts and the files together.

Deliverables:

1. `report_service.py`, a hardened replacement for the draft endpoint.
2. `test_report_service.py`.

Marking note for deliverable 2: the grader runs your test file twice, once against your `report_service.py` and once against the unmodified `naive_reference.py`, and a submission scores zero on this part unless a reader can tell from the test file alone which row of `THREAT_TABLE.md` each check belongs to, and unless each of those checks passes on the first run and fails on the second.

You may assume the database, the login session, and the deployment are all out of scope and already handled elsewhere.

---

### Starter material

**File: `THREAT_TABLE.md`** (delivered with the ticket, signed off by the security team)

| # | Threat | CWE ID | Why it applies to this endpoint |
|---|--------|--------|----------------------------------|
| 1 | A crafted `name` value walks out of the reports directory and returns an arbitrary file from the host | CWE-22 | `name` is taken straight from the query string and joined onto a directory path |
| 2 | A logged-in employee downloads a report belonging to a different employee by guessing its filename | CWE-639 | Ownership is recorded only in the `reports` table and is never consulted on the download path |
| 3 | A failed download returns internal filesystem details to the caller | CWE-209 | The handler returns the raw exception text to the client |

**File: `naive_reference.py`** (current draft, known to be unhardened)

```python
import os
import sqlite3
from flask import Flask, request, send_file, session

app = Flask(__name__)
REPORTS_DIR = "/srv/reports"


def db():
    return sqlite3.connect("app.db")
    # table reports(filename TEXT PRIMARY KEY, owner_id INTEGER)


@app.route("/report")
def get_report():
    name = request.args.get("name")
    try:
        return send_file(os.path.join(REPORTS_DIR, name))
    except Exception as e:
        return str(e), 500
```

**File: `review_checklist.md`** (excerpt, the checklist your reviewer applies to every merge request on this repo)

```
Item 3. Every merge request names a single owning developer.

Item 4. A generation request is accepted only if that one request already
names each weakness class the code must defend against and the exact library
or mechanism that handles it. Requests that leave any of this to a later
round are sent back.

Item 5. Commit messages reference the ticket number.
```

---

## 2) Traceability matrix

| # | Exact quoted text from the question | Where it lives | Guideline triggered | Element of that guideline it maps to |
|---|--------------------------------------|----------------|---------------------|--------------------------------------|


---

## 3) Why other Guideline does not apply


---

## 4) Prompts



---