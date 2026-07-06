#uni #s26 #cs398 
# Week 05: Code Generation
---
### Key Terms:
1. **Pass@1**: Measures the probability that the model will generate a fully correct, working solution on its very first try.
2. **HumanEval**: It is a dataset created by OpenAI consisting of 164 Python coding problems.
3. **MBPP (Mostly Basic Python Problems):** This is another major, standard industry benchmark used to test the functional correctness of LLMs on basic Python tasks.
---
### Guideline 01: Size Each Subtask So You Can Review Every Line
- Every sub-task you hand to the module must produce code small enough to read line by line, typically 10-50 lines.
- If the output exceeds that budget, reject it and ask for a smaller scope or further decomposition.
- This is a standing constraint on every interaction, not a one-time workflow step.
#### Reasoning
- A piece-by-piece structured workflow reduces cognitive load and improves correctness judgments.
	- It makes it easier for you to verify that the code generated is correct and follows best practices.
- Defect detection falls sharply past 200 to 400 lines per hour.
- AI-generated code is harder to review than human-authored code.
- As code volume grows, single-pass decisions accumulate unreviewed context and system quality degrades.
- AI assistant users write less secure code and are significantly more likely to believe that it is secure.
#### Key Practices
1. **Prompting**
	- State the expected size in the prompt: "Implement only the loading function around 20-30 lines with type hints and a docstring."
	- If a step would not fit in 50 lines, decompose it before asking for code, not after.
	- One concept per prompt. For example, loading and validating is two prompts, not one.
2. **Reviewing**
	- Read every line out loud or in your head, and if you find yourself skipping a block "because it's obviously fine", stop and read it.
	- For each branch, name the case it handles and the case it does not. If you cannot, you have not reviewed it.
	- If the model returned more than your budget, reject the output and ask for a smaller piece.
---
### Guideline 02: Ask for Plans as Options, Not as Answers
- For any task larger than a single function, ask the model for two or three plans with the trade-offs between them, not a single recommendation.
- At each step inside the chosen plan, ask it to name the meaningful alternatives and why it picked one.
- You, the developer, make the decisions. The model surfaces options and the reasons behind them.
#### Reasoning
- Plan-then-implement gives up to 25.4% relative Pass@1 improvement over direct generation.
- Role-based decomposition gave 29.9% to 47.1% improvement.
- The human must decide at each decomposition step;
- Errors at planning compound through every step that follows.
#### Key Practices
1. **Multiple Plans**
    - Ask for two or three complete plans, not one; require the model to state what each is better and worse at.
    - Reject plans that differ only cosmetically; ask for plans that differ on data structure, algorithm, failure mode, or cost.    
    - Pick one plan explicitly in the prompt before going further: "let's go with plan B" makes the decision visible.    
2. **Options and Review**
    - For each non-trivial step, ask the model to name the alternatives it considered and why it picked one.    
    - Treat vague justifications ("more efficient", "idiomatic") as defaults, not decisions and push for a concrete reason tied to your problem.    
    - If a step's choice depends on an unverifiable assumption, promote it into the prompt and decide whether it is true before continuing.    
    - Verify the chosen plan covers all requirements, not just the happy path.
---
### Guideline 03: Ground Prompts In Your Existing Codebase
- Before asking for code that will live in an existing project, show the model what it has to fit with:
	- Signatures
	- Type definitions
	- Naming conventions
	- The libraries already in use
- Tell the model to prefer existing libraries and abstractions.
- When it proposes something different, ask it for a justification against what is already in the project, not against alternatives in the abstract.
#### Reasoning
- Developers avoid AI tools mostly because suggestions use unfamiliar APIs that they cannot understand.
- Providing surrounding code as context is one of the strongest levers for function level.
- Repository context retrieval improves code completion by more than 10% over in-file only baselines.
- Specifying which libraries to use reduces inventory dependencies and duplication.
- Skipping context causes fragmentation, for example, two HTTP clients, two date formatters, or competing test helpers in the same project.
#### Key Practices
1. **Context**
	- Paste the signatures of functions your new code will call or be called by, as the model needs the interface, not just the description.
	- List libraries already in use and tell the model to prefer them.
	- Include 5 to 10 lines of an existing similar function as a style reference.
	- Name the conventions the project follows:
		- Case style
		- Exception types
		- Logging patterns, etc.
2. **Reviewing for Fit**
	- Read the imports first before the logic, as an unexpected import signals a choice you should invalidate.
	- For every new dependency, ask: Is this already in the project? Is the benefit worth a new entry in the manifest?
	- Check naming. Does the new code use the same vocabulary as its neighbours?
	- When the model suggests a different library, ask it to compare specifically against the existing ones.
---
### Guideline 04: Drive Generation with Executable Tests
- Before asking for code, write test cases that capture the intended behavior, including edge cases. 
- Hand the model the signature and tests together and require an implementation that passes them. 
- Treat any tests the model proposes as a hypothesis about your intent, not the ground truth. 
	- Review each one, then accept it, edit it, or reject it.
#### Reasoning
- Giving LLMs the problem statement plus tests consistently improves success on MBPP and human eval vs giving it the problem alone.
- Test-driven workflows make participants significantly more likely to correctly evaluate AI-generated code and report less cognitive load.
- Executable acceptance criteria improve semantic consistency between requirements and generated code.
- Test's PIN intent in machine-checkable form. Review becomes "Did it pass my tests?" rather than "Does this prose look right?"
#### Key Practices
1. **Prompting With Tests**
	- Write three to six test cases before the prompt. Cover the normal case, one boundary, and at least one the model is likely to miss.
		- Empty input
		- Wrong types
		- Large inputs
	- Hand the model the signature and the tests together, and ask for an implementation that passes them and explains any assumptions made.
	- If the model writes tests for you, read each one and ask, "Does this match what I actually want?" before running it.
2. **Reviewing**
	- Run the tests yourself as a model saying that the test pass is not evidence.
	- Add at least one adversarial test the model did not see before accepting the code.
		- An **adversarial test** is a test case intentionally designed to break or trick the implementation by targeting potential blind spots, edge cases, or weak assumptions that the model likely did not anticipate when writing the code.
	- Watch for test overfit. If the fix is a special case for a failing input, reject it.
---
### Guideline 05: Specify Preconditions, Postconditions, and Edge Cases
- Before asking for code, write down:
	- the input types and ranges
	- the output contract
	- the behavior on empty and boundary inputs
- Name which exceptions must be raised and when.
- Use assertive language rather than "should" or "may".
#### Reasoning
- Four of the five most applied prompt improvement patterns are about specification.
	- Algorithmic Details
	- IO format
	- More examples
	- Postconditions
		- A **postcondition** is a guaranteed condition or state that a piece of code **must satisfy upon its completion**, provided that all initial inputs were valid.
- I/O format and pre/post conditions are rated as most useful patterns in practice.
	- A **precondition** is a condition or requirement that **must be true before** a piece of code executes.
	- Common examples of preconditions are input ranges, data types, formats, system state, etc.
- Assertive language is applied less often but rated highly, and practitioners find it effective when they try it.
- Tests pin behavior by example. Specifications pin behavior by contract, and you want both.
#### Key Practices
1. **Prompting with Specs**
	- State each parameter's type, shape, and allowed range. Explicitly say what empty, zero, negative, or very large inputs must do.
	- State the output contract with the same precision.
	- Name the exceptions and when they fire.
		- "Raise a ValueError if x is negative." 
2. **Reviewing**
	- For every stated edge case, we run a test that exercises exactly that input.
	- Confirm exception types and messages match the spec and that the code does not follow them in a broad except block.
	- If the code silently accepts something you told it to reject, that is a spec violation and not a style issue.
---
### Guideline 06: Have the Model Critique Its Own Output Before You Run It
- After the model produces code, do not run it yet.
- Prompt the model to critique its own output against the spec.
- Read the critique and decide what is actually a problem.
- Then ask for a revision based on your decisions, not the models.
#### Reasoning
- Model feedback on its own output, followed by refinement beats single-pass generation across multiple tasks, including code.
- Explicit self-reflection between attempts improves Pass@1 on HumanEval.
- Self repair works only when feedback quality is high.
- Quality drops on harder problems requiring you to evaluate the critic instead of blindly trusting it.
- Critique before running catches what tests miss.
#### Key Practices
1. **Prompting for Self-Critique**
	- After the model returns code, ask for three specific lists.
		- Assumptions made
		- Edge case is not handled
		- Lines the model is uncertain about
	- Forbid the model from rewriting the code in the critique step, as you want the audit and not a new draft.
	- For each item, ask one follow-up: "If this assumption is wrong, what breaks?" This tells you whether the item matters.
2. **Reviewing**
	- Read every item and treat each as a hypothesis the model is offering and not a fact.
	- For each item, decide if it's real, a non-issue, or if the model is wrong about being wrong. All three can happen.
	- If the critique misses something you can see, the model's understanding is shallower than expected. So, be more skeptical of the rest.
	- Only after forming your own verdict should you ask for a revision. Specify what to fix, not "fix the issues you found."
---