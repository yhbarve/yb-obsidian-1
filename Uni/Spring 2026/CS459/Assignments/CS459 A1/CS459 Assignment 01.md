#uni #s26 #cs459

**Name: Yash Harshal Barve**
**ID: 20930353**

---

Q1.
(a) Ciphertext: "RWXLXZEQXLFXKOFRQFORMEOMONKXQGXREOCFGYMREFO MOLRWIKEROXXLOFRJXSGFRXQRXLMDMEOKREOKSXQREFOMOIOCMER WCIUXHXQIREZXYIKRWMZXMRUXMKRRTFMQQFYSUEQXKEOFGLXGRFC FGDXRWXQFYSMONKKEDOMRIGXEORWEKKQWXYX", Cipher: Substitution cipher

**Solution:** `THEDEVICEDOESNOTCONTAINANYSECRETINFORMATIONANDTHUSITNEEDNOTBEPROTECTEDAGAINSTINSPECTIONANUNFAITHFULEXECUTIVEMUSTHAVEATLEASTTWOACCOMPLICESINORDERTOFORGETHECOMPANYSSIGNATUREINTHISSCHEME`

**Explanation:**
- As presented in the class, a substitution cipher simply replaces each character (alphabet in this case) with another character. It still preserves the frequency distribution of the language.
- I first calculated the frequencies of each alphabet in the ciphertext, and tried to map it with that of the English language.
	- The most frequent alphabets were 'X', 'R', 'O', and 'E'.
	- Moreover, I also noticed 'RW' multiple times, just like 'TH' in English.
- After mapping R->T, W->H, and X->E, I had the following result: `THE_E___E__E___T___T_______E__ET_______T______TH___T_EE___T_E___TE_TE_______T____E_T__________TH___E_E__T__E___TH__E_T_E__TT___________E______E_T_____ETHE_____________T__E__TH____HE_E` 
- Next, I searched the source material for words and sentences starting with `THE_E`.
- `THERE`seemed like a possible match, so I mapped L->R and got the following result: `THERE___ER_E___T___T_______E__ET_______T_____RTH___T_EER__T_E___TE_TER______T____E_T__________TH___E_E__T__E___TH__E_T_E__TT___________E_____RE_T_____ETHE_____________T__E__TH____HE_E`. However, I couldn't find any mappings after this point.
- The next match was `THEDE`(from "The device..."). When I tried mapping L->D and Z->V, I got the following result: `THEDEV__ED_E___T___T_______E__ET_______T_____DTH___T_EED__T_E___TE_TED______T____E_T__________TH___E_E__T_VE___TH_VE_T_E__TT___________E_____DE_T_____ETHE_____________T__E__TH____HE_E`
- This was matching the sentence, so I mapped the remaining alphabets to the corresponding matches, and ended up with the plain text: `THEDEVICEDOESNOTCONTAINANYSECRETINFORMATIONANDTHUSITNEEDNOTBEPROTECTEDAGAINSTINSPECTIONANUNFAITHFULEXECUTIVEMUSTHAVEATLEASTTWOACCOMPLICESINORDERTOFORGETHECOMPANYSSIGNATUREINTHISSCHEME`
- After verifying, I indeed found this text in the source material.

---

(c) Ciphertext: `YHTHGDCZHTQDGNSFZDSFDEXENCDSJFDQZXMDNGAFQGHR DGHQTGAFDNGAXSXMDJFZZDTFGAFPADUFDQNJKFSXMHJEXSGDQGESX EFSGHFZZHQRFYHTHGDCZHTQDGNSFZNZFENKCHRVFPRSPEGXTSDEAPHGHZQXGQFRFZZDSPMXSFUFSPEDHSXMRXJJNQHRDGHQTEDSGHFZGXJDH QGDHQDCXQTGFSJZADSFYZFRSFGHQZGFDYFUFSPEDSGPQFFYZGXADUF DZHQTCFENKCHRVFPGADGHZVQXBQGXFUFSPXQFFCZFDQYNZFYGXUFS HMPGAFHSZHTQDGNSFZ`, Cipher: Affine cipher

**Solution:** `DIGITALSIGNATURESAREAPOPULARMEANSOFAUTHENTICATINGTHEAUTHOROFAMESSAGETHEYHAVEANUMBEROFIMPORTANTPROPERTIESSINCEDIGITALSIGNATURESUSEPUBLICKEYCRYPTOGRAPHYITISNOTNECESSARYFOREVERYPAIROFCOMMUNICATINGPARTIESTOMAINTAINALONGTERMSHAREDSECRETINSTEADEVERYPARTYNEEDSTOHAVEASINGLEPUBLICKEYTHATISKNOWNTOEVERYONEELSEANDUSEDTOVERIFYTHEIRSIGNATURES`

**Explanation:**
- Affine cipher encryption has the following formula: $E(x) = (ax + b)\ (mod\ 26)$ where $a$ must be co-prime with 26, and $0 \leq b \leq 25$.
- To decrypt text, $D(y)=a^{-1}(y - b) (mod\ 26)$
- This leaves us with just 12 options for $a$: $$a \in \{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\}$$
- Since $b$ can be between 0 and 25, this gives us $12.26 = 312$ possible keys. I wrote a short program to try decrypting the text using all possible keys.
- $(a = 7, b = 3)$ resulted in the following result: `DIGITALSIGNATURESAREAPOPULARMEANSOFAUTHENTICATINGTHEAUTHOROFAMESSAGETHEYHAVEANUMBEROFIMPORTANTPROPERTIESSINCEDIGITALSIGNATURESUSEPUBLICKEYCRYPTOGRAPHYITISNOTNECESSARYFOREVERYPAIROFCOMMUNICATINGPARTIESTOMAINTAINALONGTERMSHAREDSECRETINSTEADEVERYPARTYNEEDSTOHAVEASINGLEPUBLICKEYTHATISKNOWNTOEVERYONEELSEANDUSEDTOVERIFYTHEIRSIGNATURES`
- After verifying, I found this text in the source material.

**Note: The program used to test all combinations (`test-affine.py`) is submitted along with the other files.**

---

**Q2.** 
**(a)** ***Scenario**: Lily encounters a "404 Not Found" error on a blocked news website.*
- This is a **security issue** that violates **availability**.
- Availability means that a system or a piece of data is accessible when you want it. In this example, because the news website is censored, Lily isn't able to access it.
- It is not a privacy issue because Lily's data (such as IP address) is not being tracked or stored by the website or the government.

**(b)** ***Scenario**: Lily installs a VPN to bypass the block. However, the VPN is a malware that steals her data.*
- This is both a **security** and a **privacy issue**.
- It is a security issue because confidentiality is being violated. The VPN, which is an unauthorized party, is able to access Lily's data.
- It is a privacy issue because the VPN's ability to access and steal Lily's data completely compromises her and makes her vulnerable to financial, professional, or safety risks.

**(c)** ***Scenario**: Lily begins using the Tor browser to access the news site. She wishes to share it with her friend Luna but it's banned in her country. So, Lily copies the software to a USB drive and delivers it to Luna in person. Luna checks the file's signature and notices that it does not match the official signature on the Tor Project's website.*
- This is a security risk. **Integrity** is being violated in this example.
- Because the digital signatures did not match, the software may have been modified or corrupted. Therefore, the guarantee that Luna received the 'correct' data is no longer valid.

---

**Q3.**
**(a)** This scheme is insecure because another member within the group can impersonate Alice.
- Consider a group of Alice and her $n$ friends: $U = \{Alice, B_1, B_2, ..., B_n\}$
- Alice and all her friends share the secret key $k$.
- Therefore, a malicious user can send a fake message $M$ compute a valid MAC tag using the shared key. $$tag = MAC(k, M)$$
- For example, consider $B_2$ is the malicious user and sends a ($M$, tag) to $B_1$ impersonating Alice.
- When $B_1$ receives the packet, he will verify the tag using the key $k$. The verification will succeed because the key matches.
- However, this only proves that the packet originated from someone with the same key $k$. $B_1$ cannot verify that the message came from Alice.
- Thus, this scheme **does not ensure authenticity.**

**(b)** **For this scheme to enforce authenticity, no single friend's set of keys can be a subset of another friend's set.**
- Consider $B_2$ has the set of keys $S_2$, and $B_1$ has the set of keys $S_1$.
- According to the rule, $S_1 \not \subseteq S_2$ and $S_2 \not \subseteq S_1$.
- Whenever $B_1$ receives a message, he checks the MAC tags corresponding to the keys in $S_1$.
- Therefore, for $B_2$ to be able to impersonate Alice and send a fake message to $B_1$, he will first have to compute MAC tags for all the keys in $S_1$.
- This is only possible if $S_1 \subseteq S_2$. This is a contradiction.
- Thus, $B_1$ will reject the message sent by $B_2$.
- **Therefore, this scheme preserves authenticity.**

**(c)**
- We have 5 keys, and need 10 unique subsets.
- Since ${5 \choose 2} = 10$ each subset must have 2 elements.
- Here are the 10 unique sets of keys that will be given to the 10 friends:
	1. $S_1 = \{k_1, k_2\}$
	2. $S_2 = \{k_1, k_3\}$
	3. $S_3 = \{k_1, k_4\}$
	4. $S_4 = \{k_1, k_5\}$
	5. $S_5 = \{k_2, k_3\}$
	6. $S_6 = \{k_2, k_4\}$
	7. $S_7 = \{k_2, k_5\}$
	8. $S_8 = \{k_3, k_4\}$
	9. $S_9 = \{k_3, k_5\}$
	10. $S_10 = \{k_4, k_5\}$
- If these sets are distributed amongst Alice friends, no one friend's set contains all the keys from another friend's set. Therefore, no friend can impersonate Alice.
- **Therefore, authenticity is ensured.**

---

**Q4.**
- **Given:**
	- Carol wants to have 2 public-private key pairs.
	- Common $n = p*q$
	- Two encryption exponents $e_1, e_2$
	- $e_1$ and $e_2$ are relatively prime. So, GCD($e_1$, $e_2$) = 1
	- Two distinct decryption keys $d_1$, $d_2$
- **Required:**
	- Alice sends Carol a message $m$, encrypted with $e_1$.
	- Bob sends Carol the same message $m$, but encrypted with $e_2$.
	- Eve gets the two encrypted messages $c_1$ and $c_2$.
	- Need to show how Eve can use these messages to reconstruct the original message $m$.
- **Process:**
	- Using the Extended Euclidean Algorithm, we can find integers $r$ and $s$ such that $$r.e_1 + s.e_2 = GCD(e_1, e_2) = 1$$
	- Next, Eve can perform the following computation on $c_1$ and $c_2$: $$x = (c_1)^{r}.(c_2)^{s} (mod\ n)$$
	- But, $c_1 = m^{e_1} (mod\ n)$ and $c_2 = m^{e_2}(mod\ n)$. Therefore: $$x = (m^{e_1})^r.(m^{e_2})^s (mod\ n)$$
	- After applying laws of exponents and rearranging the terms, we get: $$x = (m)^{e_1*r}.(m)^{e_2*s} (mod\ n) = (m)^{r.e_1 + s.e_2} (mod\ n) = m^{1} (mod\ n) \equiv m$$
	- Because the same modulus $n$ was used, Eve can reconstruct the original message by combining the two encrypted messages and applying the Extended Euclidean Algorithm.
- **Note:**
	- I referred https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm to learn more about the Extended Euclidean Algorithm.
	
---
