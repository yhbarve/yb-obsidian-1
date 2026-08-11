# Example 1

## 1. The Question

**Problem statement:**

You are the reviewer of record on a pull request from a teammate who has contributed to this course project's practice repository many times before. The PR adds one small utility function, `merge_sorted`, to a shared `helpers.py` module used only inside the class repo. The diff is eight lines, and nothing in it touches authentication, cryptography, CI configuration, build or release scripts, or the project's dependency manifest.

You will be the one who clicks "Approve," and you will be expected to explain and maintain this function later in the term.

A teaching assistant already left one comment on the PR thread: "Watch out for shared mutable state." Get the AI's first set of findings on the function without showing it that comment, and only bring the comment in for a second, later pass. Require each finding from that first pass to include a way you can check it against the code yourself, such as the specific line and a short example that shows the problem.

Read the function yourself before you look at anything the AI produces, since you are the one who will explain and maintain this code later in the term. Ask the AI for observations and its reasoning, not a recommendation on whether to merge, and when you write your own comments on the PR, explain why each issue matters rather than repeating the AI's wording.

**Starter material:**

```python
# helpers.py (added by the PR)
def merge_sorted(a, b, result=[]):
    for x in a:
        result.append(x)
    for x in b:
        result.append(x)
    result.sort()
    return result
```

**Task:** Write the prompt(s) you would send the AI, in the right order, and write the review comments you would post yourself, ending with your merge decision.

---

## 2. Which Guidelines This Tests



---

## 3. Traceability: What in the Prompt Points Where

Every sentence below was placed on purpose. None of this is implied, you should be able to point to the exact clause that told you to do each thing.



If you can't match a sentence in your answer back to one of these rows, you're probably missing something the question asked for, or adding something it didn't.

---

## 4. Why Other Guidelines Don't Apply Here

This is the part students most often get wrong, so read it carefully.


---

## 5. Sample Solution


---

# Example 2:

## 1. The Question

**Problem statement**

You are the reviewer of record on a pull request to your team's open-source data pipeline library, and you will be the one who clicks approve. This is the contributor's first pull request to the project, and the PR description notes it was drafted with the help of an AI coding assistant. The PR adds a new GitHub Actions workflow that publishes a build artifact and injects a deployment token as an environment variable, along with a small helper script the workflow calls. A teammate has already left one comment on the thread: "This will let outside contributors run code with our deploy token." You will also be the person maintaining this workflow if it breaks after you graduate this program next term.

Run the AI reviewer once without sharing that comment, then run it again including the comment, to see whether it confirms, extends, or misses anything relative to what your teammate flagged. For every finding across both passes, mark it as a confirmed defect, a style preference, a false positive, or unknown, and note which pass first surfaced it. Before you decide, read the workflow and script yourself, not just the AI's output. Then write the review comments you would post on the PR and state whether you approve.

**Starter material**

`.github/workflows/publish.yml`
```yaml
name: publish-artifact
on:
  pull_request_target:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: python scripts/push_artifact.py "${{ github.event.pull_request.title }}"
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

`scripts/push_artifact.py`
```python
import os
import subprocess
import sys

def push(title: str) -> None:
    token = os.environ["DEPLOY_TOKEN"]
    cmd = f"curl -H 'Authorization: Bearer {token}' -d 'title={title}' https://artifacts.example.com/upload"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    push(sys.argv[1])
```

---

## 2. Which Guidelines This Tests



---

## 3. Traceability: What in the Prompt Points Where

Every sentence below was placed on purpose. None of this is implied, you should be able to point to the exact clause that told you to do each thing.



If you can't match a sentence in your answer back to one of these rows, you're probably missing something the question asked for, or adding something it didn't.

---

## 4. Why Other Guidelines Don't Apply Here

This is the part students most often get wrong, so read it carefully.


---

## 5. Sample Solution


---