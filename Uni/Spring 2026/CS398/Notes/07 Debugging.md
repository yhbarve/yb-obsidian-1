#uni #s26 #cs398 
# Week 07: Debugging
---
### Key Terms
1. **APR:** Automated Program Repair
---
### Guideline 01: Narrow the Bug Before You Prompt
- Before prompting, shrink the problem along three axes:
	1. **In history:** Use `git bisect` to find the commit where the test started failing.
	2. **In input:** Reduce the failing input to a minimal case that still fails.
	3. **In code:** Trace the backward slice on the wrong value prompt with only the statements that can affect it. Paste the narrowed artifact, not the whole project.
#### Reasoning
- Bounding the failure is the step that most often unblocks debugging.
- **Delta Debugging (ddmin):** Halve the input, rerun, keep the failing half, recurse to a minimal case.
- **Program slicing:** Skilled programmers reason about a backward slice, not the full program.
- Both techniques concentrate signal and strip noise, exactly what an LLM needs.
- Without this step, models produce confident but wrong fixes by guessing at the symptom.
#### Key Practices
1. **Prompting**
	- Bisect in history first if the bug is a regression.
		- `git bisect` + a one-line test finds the offending commit in logarithmic time.
	- Minimize the input using the **ddmin**.
	- Minimize the code by including only the backward slice on the wrong value. Delete unrelated imports, helpers, and branches.
2. **Reviewing**
	- If the AI asks a clarifying question, treat it as a signal that your prompt was too big or too vague. Shrink further instead of answering in prose.
	- If the AI suggests changes to code you did not include in the prompt, reject that suggestion. It is guessing outside its context.
	- Before accepting any fix, re-run your minimal reproducer and confirm the input now gives the expected output.
---
### Guideline 02: Prompt with Observed Runtime State
- When the failure is about wrong values, do not hand the AI the source and ask why.
- First, state the invariant you expect to hold. Set a conditional breakpoint on its negation.
- Run to the breakpoint, print the relevant variables, and paste the invariant plus the observed state plus the source into your prompt.
- The AI should diagnose a specific, concrete execution and not simulate a program in its head.
#### Reasoning
- Debugger-assisted LLMs produce more accurate and more explainable fixes.
- Design by contract provides the vocabulary: preconditions, postconditions, and loop invariants to name what should be true at a given point.
- A prompt naming an invariant and showing its violation is a sharp, falsifiable question.
- Concrete state is the main defense against hallucinated APIs and fabricated reasoning.
#### Key Practices
1. **Prompting**
	- Write the invariant first in one sentence before you open the debugger.
	- Set a conditional breakpoint on the negation of the invariant. It only fires when the invariant actually breaks.
	- At the breakpoint, print the variables and copy the debugger output into your prompt. Do not paraphrase.
	- If a structure is large, include a summary plus the one or two elements that look wrong, not the whole object.
2. **Reviewing**
	- The AI's explanation should refer to the specific observed values you pasted.
		- If it reasons from hypothetical values, push back.
	- Before applying a fix, set a second breakpoint after the change and verify by hand that the invariant now holds.
	- Reject fixes that reference variables not in scope at your break point. This is a common hallucination mode that debuggers catch immediately.
---
### Guideline 03: Get Ranked Hypotheses, Then You Pick
- When a bug is not trivially reproducible, do not ask "What's wrong?"
- Ask for a ranked list of hypotheses, each with an explicit reason tied to concrete evidence.
- You pick which hypothesis to test first. Write your reason for picking in your next prompt and ask the AI to push back on that reason.
- Only after the pick and the pushback do you ask for the falsifying experiment.
#### Reasoning
- **Zeller's Scientific Debugging:** The tool generates candidate theories. The human scientist picks which theory to test based on evidence and prior knowledge.
- Handing the pic to the model recreates the automation bias failure mode. Developers accept the first plausible suggestion and stop investigating.
- Writing a reason surfaces private context the AI cannot know, such as recent commits, already tried paths, and environment quirks.
- Writing a reason gives the AI something falsifiable to push back on, enabling real disagreement rather than sycophantic agreement.
- The value of LLM-assisted debugging is in the explanations and not the verdicts.
- Explanations are where the developer can catch the model being wrong.
#### Key Practices
1. **Getting Hypotheses**
	- Require a ranked list of at least three hypotheses, each with an explicit reason tied to specific evidence in the code, the error, or the observed state.
	- Ask the AI to state a prediction for each hypothesis that would hold if the hypothesis is true.
	- Forbid the AI from proposing a patch at this stage. 
2. **Choosing and Testing**
	- Read the AI's reasoning against what you privately know, such as recent commits, test history, environment, and earlier tried paths.
	- Write your reason for your pick, citing something concrete like a line number, log entry, or a commit.
	- Ask the AI to push back on your reason before it proposes an experiment. Treat sycophantic agreement as a signal to rebrand.
	- Ask for the cheapest experiment that distinguishes your hypothesis from its closest alternative.
	- Only accept a patch after the experiment confirms the hypothesis.
		- An experiment means verifying your hypothesis is correct. It is not generating a fix yet.
---
### Guideline 04: Land Every Fix With a Failing Test and Invariant
- Before accepting any AI-proposed patch, require two things alongside the patch.
	1. A test that currently fails on the buggy code for the right reason
	2. An executable assertion of the invariant inside the function that should hold after the fix
- The patch must make the test pass and preserve the invariant under adversarial inputs.
- We are basically verifying that the AI detected the correct issue and is fixing the core logic and not just overfitting to the test cases.
#### Reasoning
- An automated program repair has a known failure mode called overfitting, where the patch passes every test but it is still wrong because the suite did not pin the root cause.
- A large fraction of plausible APR patches are semantically incorrect once inspected against a ground truth specification.
- A patch is only accepted after a hypothesis has been confirmed against run-time evidence.
- LLMs frequently invent APIs or confused versions, so a fix that reads as sensible can reference functions that do not exist.
- The invariant upgrades the test-only regimen towards **Design-by-Contract**. Tests pin boundary behavior, whereas invariants pin what must be true inside the function.
#### Key Practices
1. **Prompting**
	- Ask for the failing test, the invariant, and the minimal patch in that order, and not just the patch.
	- Ask for two adversarial tests that a naive fix would not pass.
	- Give the AI your language and library version numbers to reduce hallucinated API calls. 
2. **Reviewing**
	- Run the failing test on the unpatched code and confirm it fails for the right reason by reading the assertion and not just the error message.
	- Apply the patch, re-run the whole suite, and run the adversarial tests.
	- Read the invariant assertion. If you can name an input that would violate it, add it to the adversarial set.
	- Watch for overfitting patterns.
---
### Guideline 05: Ask the AI to Classify Its Fix
- Before reading the diff of any AI-proposed patch, ask the AI one question: *"Does this fix remove the cause from the execution trace, or does it add a guard that prevents the symptom from being observed?"*
- A root cause fix changes the code so the wrong state is never reached.
- Whereas a symptom adds a guard that intercepts the failure after the wrong state has already been produced.
- Always know which kind of fix you are accepting.
#### Reasoning
- Most plausible APR patches suppress a symptom rather than remove a cause.
- LLM performance drops sharply on semantic bugs compared to syntactic ones.
- Semantic bugs are where symptom fixes are most tempting. Wrong state is subtle, and the root cause is hard to articulate.
- A fix is valid only if it removes the cause and not just prevents the observable failure.
- Developers stop at the first plausible fix. A confident AI patch makes this failure mode worse.
#### Key Practices
1. **Before you read the diff**
	- Ask the AI to classify its own fix in one sentence before you evaluate any code: "*root cause removal or symptom guard?* "
	- If it says guard, ask it to describe the root cause the guard is protecting against and why that cause is not being fixed directly.
	- If the AI cannot clearly state which category its fix falls into, treat that as a signal that the reasoning is unclear and ask it to re-examine.
2. **Reading the diff and after**
	- Recognize 4 common symptom fixed patterns:
		1. Broad try/except
		2. None guard just before the failure
		3. Special case branch for the exact input
		4. Logging and continue
	- For each yellow flag, trace backward. If the guard tests `if result is None`, ask what code path makes the result `None`. 
	- Run a probe input that exercises the same root cause via a different call path than the one in your failing test. A symptom guard will still fail this probe.
	- If you accepted a symptom fix intentionally, add a comment naming the root cause and linking to the tracking issue.
---
### Guideline 06: Keep a Debugging Log
- Write down every hypothesis tested, every experiment run, and every fix tried, with the result and a one-line reason for why you picked it.
- Feed the log back in with each prompt so that the next suggestion is constrained by what has already been ruled out. 
- When the conversation starts looping, start a fresh chat with only the log and your current minimal reproducer as context.
#### Reasoning
- The debugging logbook keeps the cause-effect chain visible and prevents repeated experiments.
- Losing track of what has been tried is the main reason professional debugging sessions spiral into wasted hours.
- Multi-turn AI debugging gets stuck because the model repeatedly proposes fixes that were already tried earlier.
- Re-pasting a short log at each turn turns the model's limited memory into a non-issue.
- The '*why I picked this*': notes become a record of your own learning.
#### Key Practices
1. **Prompting**
	- Start the prompt with a short log consisting of:
		- the hypothesis tried and ruled out with reasons
		- picks and their reasons
		- fixes tried and results
	- Ask the ear to reason from the log: "*Given what has been ruled out, what is the next most likely hypothesis and cheapest experiment?*"
	- If the chat is more than a handful of turns long, start a new one with only the log and the current minimal reproducer.
2. **Reviewing**
	- If the AI suggests something already on your tried list, point it out explicitly.
	- Update the log immediately after each experiment or fix attempt while the result is fresh.
	- When handing off the bug to a teammate, share the log and not the chat transcript. It is the actual record of what you learned.
---