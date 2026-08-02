# Poisoning Attacks
## Background & Informal Defination
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
	- It learns to easily correlate.
- 