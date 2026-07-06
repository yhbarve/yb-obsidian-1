#uni #s26 #cs459
# Lecture 01: Introduction
---
### Security
- Security can be described using the CIA triad:
	- Confidentiality: Access to systems or data is limited to authorized parties.
	- Integrity: When you receive data, you get the 'right' data.
	- Availability: The system or data is there when you want it.
### Privacy
- Privacy is broader and deals with how data handles individual identity, user rights, and data friction.
- Security is a way of enforcing privacy.
- Privacy can be broken down into multiple categories:
	- Technical privacy
	- Conceptual privacy
	- Legal privacy
	- Usable privacy
- In this course, we focus on technical privacy.
- We need to define:
	- **What** is being protected
	- From **who**
	- And under what **conditions** this protection will hold
- Breaching someone's privacy can lead to several issues like:
	- Financial
	- Professional
	- Societal
	- Safety
### Assets
- Hardware
- Software
- Data
### Terminologies
- A vulnerability is a weakness that can be exploited, which would compromise an asset.
- An asset getting compromised poses the following threats:
	- Loss or harm
	- Interception
	- Interruption
	- Modification
	- Fabrication
- Attack is a way to exploit a vulnerability and execute a threat.
- Control/Defense involve removing or reducing a vulnerability. This gives control to prevent attacks or defend against threats.
- Dealing with attacks:
	- Prevent it: Stop the attack from happening
	- Deter it: Make the attack difficult or less tempting
	- Deflect it: Distract the attacker to something else (honey-pot)
	- Detect it: Identify an attack that is happening or has already happened
	- Recover from it: Restoring the system, data, and operations to a secure, normal functioning state
- **Principle of Easiest Penetration:**
	- A system is as secure as the weakest link. An attacker will always choose the path of least resistance, i.e., exploiting the easiest point of entry to a system.
- **Principle of Adequate Protection:**
	- A system must be protected so that the cost and effort required to breach its security controls significantly exceed the value of the protected asset itself to the attacker.
	- Basically, you do not need to build an _impenetrable_ system; you just want to make the attack feel not worth the effort and cost required to perform it.
### Some Defenses for Data
- Cryptography
- Network Security
- Data Collection and Usage Practices
### Summary
- Valuable asset exists
	- Could be software, hardware, or data
- A hidden vulnerability is introduced
	- Through mistakes, design flaws, dependency issues, etc.
- An external threat matches that weakness
	- External adversary’s capabilities, tools, or motives perfectly align with the specific internal flaw.
	- An adversary could be created after detecting a potential vulnerability to exploit.
- Adversary launches an attack
- Defensive controls detect / prevent / recover from the exploit
- **An external Threat exploits an internal Vulnerability by launching an Attack, which can be mitigated, blocked, or managed using Defense Controls.**
