#uni #s26 #cs398 
# Week 06: Code Summarization
---
### Key Terms
1. **REPL:** Read-Eval-Print-Loop
2. **RPC:** Remote Procedure Calls
---
### Guideline 01: Specify the Summary Intent Before Asking
- State what kind of summary you want.
	- What the code does
	- Why does it exist
	- How to use it
	- Its properties
	- How it is implemented
- Different audiences and tasks need different summary types.
- Without a pinned intent, the AI defaults to a vague blurb.
#### Reasoning
- Five distinct summary intent categories serve different comprehension needs in real projects.
	- What
	- Why
	- How it is done
	- Property 
	- How to use
- LLMs produce high-quality summaries across all five categories only when intent is explicit.
- Unconditioned prompts default to generic summaries miss what the reader actually needs.
- Real-world Java projects use these categories at different rates.
#### Key Practices
1. **Prompting for a specific intent**
	- Name the intent explicitly.
	- Tell the model who the reader is because that determines which intent is most useful.
	- Ask for one intent at a time, unless you genuinely want a multi-part summary. Blended prompts tend to be long and shallow.
2. **Review the result**
	- Check that the output actually matches the intent you requested and not just any true statement about the code.
	- Reject summaries that restate syntax line by line when you asked for rationale or usage.
	- If you need multiple intents, request them as separate labeled sections so you can evaluate each one independently.
---
### Guideline 02: Surface the Semantic Facts That the AI Cannot See
- When summarizing a function, attach the semantic facts a quick read would extract.
	- Repository name
	- Fully Qualified Function Name
	- Identifier names
	- Data flow relationships
	- And pre and post conditions
- The AI will often miss these even though they look obvious from the code.
#### Reasoning
- Adding data like the repository name, function name, identifiers, and data flow graph to the prompt improves summary quality across three LLMs on standard benchmarks.
- Explicitly labelled semantic facts focus the model's attention on named entities and phrases that carry intent, benefiting even capable models.
#### Key Practices
1. **Prompting with semantic facts**
	- Include the repository or module name and the fully qualified function name so the module can ground its vocabulary in the project.
	- List non-trivial identifiers with a short note if their meaning is not obvious from the name.
	- State any pre- or post-conditions and the main data flow relationship in a couple of lines.		
2. **Reviewing the result**
	- Check that project-specific terms from the facts appear in the summary rather than generic synonyms.
	- Flag summaries that invent behavior not supported by the facts that you provided.
	- If the summary repeats the facts instead of synthesizing them, tighten the prompt to ask for a summary and not a restatement.
---
### Guideline 03: Verify the Summary Against Behaviour, Not Just Plausibility
- Treat an AI-generated summary as a claim about the code's behavior and check it.
- Pick one or two testable statements and confirm them by running the code or writing a quick unit test.
- Do not accept a summary because it sounds correct.
#### Reasoning
- Manual inspection of 540 LLM-generated comments found demonstratively inaccurate statements in roughly one-fifth of cases, even for the strongest models. 
- Existing core common consistency detectors have no statistically significant relationship with actual accuracy, so surface checks cannot catch these errors.
- 'Document testing' turns each summary claim into an executable test.
#### Key Practices
1. **Prompting for a verifiable summary**
	- Ask the model to produce a summary whose claims are phrased as concrete behaviors rather than vague prose.
	- Ask it to list the summary's claims as a short bullet list at the end, so each one can be checked independently.
	- When the summary hinges on an edge case, ask the model to state the expected behavior explicitly.
2. **Reviewing the result** 
	- Pick the most load-bearing claim and confirm it by running the function on a matching input.
	- Write a one-line assertion or REPL expression for any claim about return value, exceptions, or ordering.
	- Treat unverified claims about thread safety, performance, or side effects with ultra-suspicion, as these are the classes where LLM-generated comments most often drift.
---
### Guideline 04: Do Not Trust Surface Fluency as a Quality Signal
- Don't judge a summary by how professional it sounds.
- Fluent summaries routinely miss key facts. 
- Focus on if it answers the question about the code, spots a bug, or decides whether to reuse a function.
#### Reasoning
- Participants with human-written summaries perform significantly better on comprehension tasks.
- LLM confidence scores are poorly calibrated. Two summaries with nearly identical high confidences can differ greatly in accuracy.
- Neither fluency nor model confidence is a safe proxy for usefulness. Both can be high while the summary omits critical inputs, outputs, or error conditions.
#### Key Practices
1. **Prompting for usefulness and not polish**
	- Tell the model the task the summary must support so that the output is shared by the task and not by the generic style.
	- Ask for concrete, checkable facts rather than adjectives.
	- Prefer short, dense summaries over long, polished ones because length hides omissions.
2. **Reviewing the result**
	- Run a quick comprehension test. Close the code and try to answer one concrete question using just the summary.
	- Ignore the module's confidence language when deciding whether to keep the summary.
	- Compare the summary against the factual function signature and a sample call. Missing parameters or error paths mean that the summary is incomplete no matter how well it reads.
---
### Guideline 05: Adapt Your Prompt to the Language and Paradigm
- Change how you prompt based on the programming language and paradigm of the code.
- AI assistants perform noticeably worse on logic programming code than on mainstream imperative code.
- Performance varies even between closely related languages.
- Compensate with explicit paradigm-driven and worked examples.
#### Reasoning
- All four evaluated elements perform worst on logic programming languages such as Prolog.
- Performance varied substantially within paradigms too.
- Paradigm-dependent performance reversals occurred between Haskell and Erlang, showing that language choice matters even within the functional paradigm.
- The LLM as a judge evaluation protocol aligned well with human evaluation, giving students a practical way to cross-check their own summaries.
#### Key Practices
1. **Prompting the language and paradigm**
	- Name the language and paradigm explicitly so that the model does not default to imperative vocabulary.
	- For logic, functional or declarative code, include the meaning you want captured rather than asking for a generic description.
	- For less common languages, give a one-line behavioral anchor to stabilize the output.
2. **Review the result** 
	- Check that the summary uses paradigm-appropriate vocabulary rather than being translated into imperative steps.
	- Be extra skeptical of languages and dialects where the model's training coverage is likely thinner.
	- When unsure, ask the model to summarize the same code twice. Wide disagreement signals you need more context in the prompt.
---
### Guideline 06: Seed Project Style With a Few Local Exemplars
- When asking for a summary inside an existing project, include 2 or 3 example summaries from the same codebase so the AI picks up the project's conventions for terminology, length, voice, and level of detail.
- Do not rely on zero-shot to match project style.
#### Reasoning
- Few-shot prompting with examples from the same project significantly improves quality over zero-shot and cross-project few-shot prompting.
- In context examples, let LLMs generate comments in distinct intent styles matching what developers in that project actually write.
- Vocabulary and conventions in the real codebase are highly project-local. Same project examples are the cheapest way to transfer that data.
#### Key Practices
1. **Prompting with project examples**
	- Pick two or three existing summaries from the same module or closely related modules.
		- Prefer summaries written by the project's most consistent author.
	- Paste each example as a <code, summary> pair in the same format you want the output in, with no extra commentary between them.
	- Put the function to summarize last so that the model uses the examples as a style template and not the other way around.
2. **Reviewing the result** 
	- Compare the output's length, tone, and terminology against the examples.
		- Large deviations usually mean the examples were ignored or were inconsistent with each other.
	- Watch for generic phrasing creeping back in. This is a sign that the model fell back to its default style.
	- If a project uses unusual conventions, make sure at least one example demonstrates that convention clearly.
---