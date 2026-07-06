#uni #s26 #cs398
# Week 04: Requirements
---
### Key Terms:
1. **SRS:** Software Requirements Specification
2. **RE:** Requirements Engineering
3. **FR:** Functional Requirements
4. **NFR:** Non-Functional Requirements
5. **FDS:** Functional Design Specification
---
### Guideline 01: Identify Stakeholders First
- Before generating any requirements, ask the model to identify all stakeholder groups.
- Then for each group, run a separate prompt instructing the model to adopt that group's perspective.
- This two-step sequence catches non-user stakeholders that are silently omitted in direct generation.
#### Reasoning
- The root cause of missing non-user requirements is that practitioners working in unfamiliar domains do not know how to look for those stakeholders in the first place.
- Automated tools reproduce the same stakeholder blind spots when given no explicit instruction to look beyond end-users.
#### Key Practices:
1. **Stakeholder Identification**
	- Prompt: "List all stakeholder groups who have a stake in this system. Include not just end users but also anyone who operates, deploys, maintains, supports, or audits it. For each group, write one sentence describing their primary concern."
	- Don't skip this step even if you think you already know all the stakeholders.
	- Treat the models list as a starting point. Add missing rules and remove those that do not apply to your project.
2. **Per-stakeholder requirements**
	- Prompt: "Now adopt the perspective of a {role}. Generate at least three requirements not already covered by existing requirements."
	- Do not merge multiple stakeholders into one prompt, as the model will collapse them and the least visible groups will still be lost.
---
### Guideline 02: Flipped Interaction Pattern
- Instruct the model to drive the conversation by asking you targeted questions one at a time until it has enough information to produce a complete requirements document instead of telling the model what you want upfront.
#### Reasoning
- This allows the model to ask questions to surface assumptions and not hallucinate from a thin description.
- LLM requirements from this prompt are abstract and infeasible. Structured questioning forces confirmation before filling gaps.
- Iterative prompting grounds outputs in confirmed stakeholder intent.
#### Key Practices
1. **Elicitation**
	- Prompt: "Ask me questions one at a time about my software system until you have enough information to write a complete SRS. Start with the most important question."
	- Do not volunteer a long description up front. Let the model discover gaps through its questions.
	- After each answer, confirm the model's understanding before it moves to the next question.
2. **Review**
	- After the session, ask: "Based on our conversation, list any assumptions made that I have not explicitly confirmed."
	- Check that every generated requirement traces back to at least one answer you gave during the session.
	- Reject any requirement containing "appropriate", "reasonable", or "user-friendly" without a measurable criterion attached.
		- These words are ambiguous and untestable.
		- Ignore requirements like "the interface must be user friendly."
		- Instead accept, "A first-time user must be able to complete a checkout in under 3 clicks without training."
---
### Guideline 03: Cognitive Verifier Pattern
- When a stakeholder provides a vague or overloaded requirement, prompt the model to decompose it into specific sub-questions before generating any acceptance criteria.
- Answer those sub-questions yourself, then ask the model to write the final requirement.
	- For example, the statement "The system needs to be fully secured, fast, and let managers easily generate financial reports at the end of the month." is a vague requirement because it lacks specific details, leaving it open to multiple interpretations.
#### Reasoning
- This sub divides questions into sub-questions, first forcing ambiguities to the surface before they reach acceptance criteria.
- Single-shot prompts produce under-specified output because the model fills gaps with statistically common answers, and not the correct answers.
#### Key Practices
- Prompt: "Before generating any requirements for the following statement, list the sub-questions you need answered to write a complete, unambiguous requirement. Do not answer the questions yourself."
- Answer every sub-question yourself in a follow-up message, then ask the model to generate the final requirements explicitly referencing your answers.
- If the model introduces a term you did not define, ask it to flag the assumption and propose two alternatives for you to choose.
---
### Guideline 04: Provide a Structured Output Template
- When asking the model to draft an SRS section, include the exact section template in the prompt.
- Do not ask for free-form prose.
- If you do not supply an template to the model, we invent one from its training data. It will not match your tracker or tooling.
#### Reasoning
- Pre-defined templates improve LLM-generated FDS quality significantly.
- Template constraints for subtasks for SRS generation reduce hallucination and improve non-redundancy scores.
- Explicit output structure prevents field invention and generic documentation boilerplate.
#### Key Practices
1. **Prompting with a Template**
	- Paste your organization's actual SRS template into the prompt before any requirement content.
	- Specify field names and accepted values explicitly.
	- Ask the model to fill in one requirement per temperate block. Do not ask for a batch of requirements in one unstructured block.
2. **Reviewing Output**
	- Confirm that no field was left blank or filled with a placeholder such as TBD, without flagging it for follow-up.
	- Verify that the verification field for each requirement is a method your team can realistically execute.
	- Priority must be justified by business rationale and not left as a default.
---
### Guideline 05: Detect Conflicts and Undefined Terms
- Once a draft requirements set is complete, feed the entire list to the model in one prompt and ask you to identify contradictions between requirements.
- Flag any term used in more than one requirement without a shared definition.
#### Reasoning
- Validation is the RE phase with the most consistent LLM contribution because "find contradictions" is a narrowly defined analytical task rather than generative.
- Structured analytical prompts, where the model is given a checklist of what to look for, produce the most reliable outputs in RE validation tasks.
#### Key Practices
1. **Conflict Detection**
	- Page the complete numbered requirements list and ask: "Identify any pair of requirements that contradict each other. Then list every domain term that appears in more than one requirement and does not have a shared definition. Output each finding as a table row. "
	- Use two separate output tables, one for contradictions and one for undefined shared terms.
	- Include both functional and non-functional requirements in the same prompt.
2. **Acting on Results**
	- For each conflict, hold a stakeholder decision meeting before writing any code. Do not ask the model to resolve the conflict on its own.
	- For each undefined shared term, add a **Definitions** section to the SRS and run the conflict detection again.
	- Treat any conflict between a functional requirement and a non-functional requirement as the highest priority, as these are the most likely to cause architectural rewrites.
---
### Guideline 06: Supply a Worked Example for NFRs
- When asking the model to generate non-functional requirements, include one concrete, measurable NFR as a worked example directly in the prompt.
- This anchors the output format and prevents untestable quality attributes.
#### Reasoning
- NFR score is highest when the model is given a template with an example.
- Without one, the models fall back to vague adjectives like "fast" or "secure".
- LLMs meet quality criteria less frequently than human-authored ones because of language clarity failures.
- Few shot prompting transfers format and measurability expectations to the model, and no fine tuning is needed.
	- Few-shot prompting is a technique where you provide the LLM with one or more concrete, high-quality examples directly within your prompt before asking it to complete a task.
	- You show it exactly what a correct, successful response looks like instead of just telling the model what to do with abstract instructions.
#### Key Practices
1. **Prompting with a Worked Example**
	- Format the example NFR as: `[Quality attribute] -- [Measurable condition] -- [Verification Method]`
		- Example: `Performance -- The search endpoint shall return results within 300 ms at p95 under 200 concurrent requests. -- Verified by a k6 load test.`
	- After providing the example, list the FRs you want NFRs to be derived from, and ask the model to follow the same format for each.
2. **Reviewing NFRs**
	- Delete any NFR that does not contain a numeric threshold or a named standard.
	- For each NFR, confirm the verification method is something your team can actually execute.
	- Recheck that Security and Availability NFRs are present for any FR involving User Authentication or External Data.
---
