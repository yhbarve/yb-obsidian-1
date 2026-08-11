## 1) Problem Statement and Starter Material

**Problem Statement**

Your team used an AI coding assistant to scaffold a small course project: a Flask app that looks up student records in a Postgres database. The code and infrastructure files are provided below exactly as the AI generated them. This service will be deployed on a public cloud VM for grading, so anything you leave open to the network is open to anyone, not just your grading TA.

Fix the infrastructure so the database is not reachable from outside the VM and is not using default credentials. Also fix the code vulnerability shown in the Bandit output below. Include that exact output in your prompt to the AI so it is working from a specific finding rather than a vague "make this secure" request.

You do not need to add, remove, or upgrade any Python packages for this task. `requirements.txt` is already final.

**Starter Material**

`docker-compose.yml`
```yaml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: coursedb
    ports:
      - "5432:5432"
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
```

`app.py` (excerpt)
```python
@app.route("/lookup")
def lookup():
    username = request.args.get("username")
    conn = get_db_connection()
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cur.execute(query)
    return jsonify(cur.fetchone())
```

`requirements.txt` (already pinned, do not modify)
```
Flask==3.0.3
psycopg2-binary==2.9.9
gunicorn==22.0.0
```

Bandit output (already run for you):
```
Test results:
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through
   string-based query construction.
   Severity: Medium   Confidence: High
   CWE: CWE-89
   Location: app.py:34
   34      query = f"SELECT * FROM username = '{username}'"
```

Submit: an updated `docker-compose.yml`, an updated `app.py`, and the two prompts you used.

---

## 2) Traceability Matrix

| Quoted text | Guideline | What it maps to |
|---|---|---|

---

## 3) Why Other Guideline Does Not Apply

---

## 4) Sample Prompts a Student Would Write

