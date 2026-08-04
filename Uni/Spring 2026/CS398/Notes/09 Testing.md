---
tags:
  - uni
  - s26
  - cs398
---
# Week 09 - Testing
- - -
### Guideline 01: Anchor Assertions to the Specification, Not to the Code
- When prompting an AI assistant to generate test assertions, supply the specification as the basis for expected values.
- Never let the model derive expected values solely by reading the implementation under test.
- If the implementation is wrong, oracles built from it will also be wrong, and the tests will pass silently on the bug.
#### Reasoning
- The oracle problem:  Determining if observed behaviour matches intended behaviour predates LLMs by decades.
- LLMs introduce a new variant: the model reads code and generates assertions capturing actual behaviour, not what the specifications require.
- Oracle deficiency, where there is no external reference for correctness, so the model trusts the implementation.
- Oracle problem is the primary open weakness in current LLM-based test generation.