### Guideline 1: Narrow the bug before you prompt: bisect, minimize, slice

**Example:**

> **Problem:** Yesterday your test suite was green. Today `pytest tests/test_report.py::test_summary` fails with `AssertionError`. The project has 40 files and you made 14 commits today. The test feeds a CSV into `summarize(rows)` and checks the output row count.
>
> **Starter material:**
> ```bash
> # What you already know
> $ git log --oneline HEAD~14..HEAD
> <14 commits>
> $ pytest tests/test_report.py::test_summary
> E  assert 97 == 100
> ```

> **Answer:**

---

### Guideline 2: Prompt with observed runtime state, not source code alone

**Example:**

> **Problem:** A numerical simulation produces `NaN` sometime around iteration 50,000. Printing every iteration would produce 50,000 lines you cannot realistically paste. You want to stop at the first non-finite value.
>
> **Starter material:**
> ```python
> import math
>
> def step(positions, velocities, dt):
>     forces = compute_forces(positions)          # returns a list of floats
>     for i in range(len(positions)):
>         velocities[i] += forces[i] * dt
>         positions[i]  += velocities[i] * dt
>     return positions, velocities
>
> # Run loop:
> for t in range(100_000):
>     positions, velocities = step(positions, velocities, dt)
> ```

> **Answer:**

---

### Guideline 3: Get ranked hypotheses with reasons, then you pick and justify

**Example:**

> **Problem:** A test in your concurrency homework passes most of the time but fails about 1 in 10 runs with `AssertionError: 39987 != 40000`.
>
> **Starter material:**
> ```python
> import threading
>
> counter = 0
>
> def increment():
>     global counter
>     for _ in range(10000):
>         counter += 1
>
> def test_counter():
>     threads = [threading.Thread(target=increment) for _ in range(4)]
>     for t in threads:
>         t.start()
>     for t in threads:
>         t.join()
>     assert counter == 40000
> ```

> **Answer:**

---


## 2. References

[1] Layman, L., Diep, M., Nagappan, M., Singer, J., DeLine, R., and Venolia, G. (2013). *Debugging Revisited: Toward Understanding the Debugging Needs of Contemporary Software Developers*. In 2013 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM), pp. 383-392. DOI: 10.1109/ESEM.2013.43.

[2] Bajpai, Y., Chopra, B., Biyani, P., Aslan, C., Coleman, D., Gulwani, S., Parnin, C., Radhakrishna, A., and Soares, G. (2024). *Let's Fix this Together: Conversational Debugging with GitHub Copilot*. In IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC 2024), pp. 1-12. IEEE Xplore: 10714559.

[3] Kang, S., Chen, B., Yoo, S., and Lou, J.-G. (2025). *Explainable automated debugging via large language model-driven scientific debugging*. Empirical Software Engineering, 30(2): 45. DOI: 10.1007/s10664-024-10594-x. Preprint: arXiv:2304.02195.

[4] Chen, X., Lin, M., Schärli, N., and Zhou, D. (2023). *Teaching Large Language Models to Self-Debug*. arXiv:2304.05128. Published at ICLR 2024.

[5] Perry, N., Srivastava, M., Kumar, D., and Boneh, D. (2023). *Do Users Write More Insecure Code with AI Assistants?* In Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (CCS '23), pp. 2785-2799. DOI: 10.1145/3576915.3623157.

[6] Zeller, A. (2009). *Why Programs Fail: A Guide to Systematic Debugging*, 2nd ed. Morgan Kaufmann. ISBN: 978-0-12-374515-6.

[7] Yang, D., Zhu, G., Liu, X., Xu, Z., Zhou, Y., Chen, X., and Lou, Y. (2024). *Patch Correctness Assessment: A Survey*. ACM Transactions on Software Engineering and Methodology. DOI: 10.1145/3702972.

[8] Liu, F., Liu, Y., Shi, L., Huang, H., Wang, R., Yang, Z., and Zhang, L. (2024). *Exploring and Evaluating Hallucinations in LLM-Powered Code Generation*. arXiv:2404.00971. (Later versions appear under the title *Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code*, accepted to IEEE Transactions on Software Engineering.)

[9] Kang, S., An, G., and Yoo, S. (2024). *A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization*. Proceedings of the ACM on Software Engineering, 1(FSE): 1424-1446. DOI: 10.1145/3660771.

[10] Zeller, A., and Hildebrandt, R. (2002). *Simplifying and Isolating Failure-Inducing Input*. IEEE Transactions on Software Engineering, 28(2): 183-200. DOI: 10.1109/32.988498.

[11] Weiser, M. (1984). *Program Slicing*. IEEE Transactions on Software Engineering, SE-10(4): 352-357. DOI: 10.1109/TSE.1984.5010248.

[12] Zhong, L., Wang, Z., and Shang, J. (2024). *Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step*. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 851-870. DOI: 10.18653/v1/2024.findings-acl.49. Preprint: arXiv:2402.16906.

[13] Meyer, B. (1992). *Applying "Design by Contract"*. IEEE Computer, 25(10): 40-51. DOI: 10.1109/2.161279.

[14] Parnin, C., and Orso, A. (2011). *Are Automated Debugging Techniques Actually Helping Programmers?* In Proceedings of the 2011 International Symposium on Software Testing and Analysis (ISSTA '11), pp. 199-209. DOI: 10.1145/2001420.2001445. Received the ISSTA 2021 Impact Paper Award.

[15] Tian, R., Ye, Y., Qin, Y., Cong, X., Lin, Y., Pan, Y., Wu, Y., Haotian, H., Weichuan, L., Liu, Z., and Sun, M. (2024). *DebugBench: Evaluating Debugging Capability of Large Language Models*. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 4173-4198. DOI: 10.18653/v1/2024.findings-acl.247. Preprint: arXiv:2401.04621.