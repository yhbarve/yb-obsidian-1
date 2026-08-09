# Poisoning Attacks
## Background & Informal Definition
- A poisoning attack is an attack where someone corrupts the information a system learns from so that the system behaves badly later.
- Poisoning is like secretly editing a textbook or an answer key that a student refers to while studying.
- A pausing attack is an attack on the learning process.
- An example is a spam filter attack which involves reporting massive amounts of spam emails as not spam.
## Formal Definition
- **Formula:** $f_\theta(x)$ = Prediction for input $x$
- **Components:**
    - $f$ = Model function / architecture
    - $\theta$ = Internal settings / weights (parameters)
- **Example:** $f_\theta(\text{"Win money now"}) = \text{spam}$
- **Objective:** Training finds optimal parameters $\theta$ to make accurate predictions.
### Clean Learning Pipeline
- **Pipeline:** $D \longrightarrow A(D) \longrightarrow f_\theta$
- **Components:**
    - $D$ = Clean training dataset
    - $A$ = Learning algorithm
    - $A(D)$ = Training process (running algorithm $A$ on dataset $D$)
    - $f_\theta$ = Resulting trained clean model        
### Poisoned ML Pipeline
- **Pipeline:** $D' \longrightarrow A(D') \longrightarrow f_{\theta'}$    
- **Components:**
    - $D'$ = Poisoned dataset (modified or added malicious samples)        
    - $A$ = Standard learning algorithm (remains unchanged)        
    - $A(D')$ = Training process executed on poisoned data        
    - $f_{\theta'}$ = Corrupted model learned from poisoned data        
### Key Takeaway
- **Data Poisoning Attack:** The adversary alters the data ($D \rightarrow D'$) rather than the algorithm ($A$), forcing the model to learn malicious parameters ($f_\theta \rightarrow f_{\theta'}$).
## Motivation for an attacker
- An attacker can initiate a **targeted attack** which would make one target input wrong.
- A **backdoor attack** where the model behaves normally unless a trigger appears
- And **knowledge-based poisoning**, where the attacker would make a retrieved context support the attacker's answer.
- - -
# Backdoor Attacks
- Basic label poisoning changes labels of ordinary examples. This can make the model fail broadly.
- But broad errors are easier to notice during validation.
- Backdoor poisoning is more targeted. The model behaves normally on clean inputs but predicts the attacker's target when a trigger appears.
- The goal of a backdoor attack is to ensure a high clean accuracy but, at the same time, have a high triggered attack success.
- There is no universal single explanation for all backdoors, but shortcut learning gives a useful intuition:
	- Models learn from correlations in the data.
	- Models often learn the easiest predictive correlation that reduces training loss.
	- We give the model an easy correlation.
	- It learns to easily correlation.
- - -
# Web Scale and LLM Era Poisoning
## LLM Pipeline
- Pre-training: LLM learns general language patterns from massive text.
- Instruction Tuning: This process teaches the model how to respond to user requests.
- RAG: This process retrieves external knowledge so that answers are grounded.
- Agent memory: This preserves context for long-running personalized tasks.
## Pre-training
- Pre-training teaches the model general language patterns by showing it huge amounts of text.
- The task for the model is to predict the next token, when given a token sequence.
- A token is a small piece of text, such as a word or a punctuation mark.
- At the end of pre-training, the model learns grammar, facts, and can code.
## Instruction Tuning
- A pre-trained model can generate text, but it does not automatically know how to follow instructions.
- Instruction tuning means fine-tuning on examples that pair user instructions with good responses.
## RAG
- A problem cannot store all fresh and private knowledge.
- RAG solves this by retrieving relevant documents at answer time.
	- Retrieval: find relevant information
	- Augmented: add that information to the model's context.
	- Generation: produce the final answer.
- The LLM answers using both its trained language ability and retrieved external context.
## Agent
- A regular LLM usually answers one prompt at a time.
- An agent uses an LLM as a controller for a task loop.
	- Break a goal into steps
	- Retrieve relevant knowledge or use tools
	- Observe results
	- Update Memory
	- Continue
- - -
# Poisoning Web-Scale Training Datasets
- Split view poisoning attacks the data set construction pipeline.
- Web pages can change, and images at URLs can be replaced.
- Domains can expire and be deregistered, and crowd edited pages can be modified.
- Dataset users may download content long after the dataset was indexed.
- How Split View Poisoning Works:
	- Dataset records of web reference
	- The reference initially points to clean content.
	- The attacker later controls or changes that content.
	- A model trainer downloads the dataset later.
	- The trainer receives pause and content.
- It is estimated that 0.01% of huge data sets could be poisoned for about $60 under their attack assumptions.
- Even though 0.01% sounds small, 0.01% of 400 million is equal to 40,000 examples.
- To carry out this attack, the attacker may need one of the following:
	- Control over content at a URL
	- Ability to acquire expired domains
	- Ability to modify web hosted content after indexing
	- Ability to explore data sets that store references instead of immutable copies
- - -
# Poisoning RAG Knowledge Databases
- A knowledge database is a collection of text passages.
- When a user asks a query, the retriever searches the knowledge database and returns the most relevant passage.
- LLM answers with both the question and the retrieved texts as context.
- Poisoning RAG databases include crafting malicious texts (made up of questions & malicious answers) and inserting it inside the knowledge base.
- A malicious text must do two things:
	1. The malicious text must be retrieved for the target question. The attack fails if the text persuades the LLM but is never retrieved.
	2. The retrieved malicious text must make the LLM output the target answer. The attack fails if the text is retrieved but does not persuade the LLM.
- In **Blackbox Poisoned RAG**, the attacker does not know the knowledge database contents, the LLM parameters, or the retriever parameters, but the attacker can inject a few malicious texts into the knowledge database.
- A few malicious texts can be enough.
	- PoisonedRAG injects five malicious texts per target question.
	- Reported attack success in the black-box PaLM 2 setting is up to 97% on NQ, up to 99% on HotpotQA, and around 91% on MS-MARCO.
	- Knowledge databases contain millions of clean texts.
- - -