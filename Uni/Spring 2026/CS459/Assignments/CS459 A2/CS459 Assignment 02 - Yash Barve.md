---
tags:
  - cs459
  - uni
  - s26
---
Name: **Yash Harshal Barve**
Email: yhbarve@uwaterloo.ca
Student ID: **20930353**
- - -
### Question 01
**Q1 (a)**
- All the four packets are permitted, as described in the following table.

| Packet | Direction | Src Addr    | Dest Addr   | Protocol | Dest Port | Action | Rule |
| ------ | --------- | ----------- | ----------- | -------- | --------- | ------ | ---- |
| 1      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 443       | Permit | A    |
| 2      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 1234      | Permit | B    |
| 3      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 443       | Permit | C    |
| 4      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 1357      | Permit | D    |

- - -

**Q1 (b) i**
- Both the packets succeed.

| Packet | Direction | Src Addr   | Dest Addr  | Protocol | Dest Port | Action | Rule |
| ------ | --------- | ---------- | ---------- | -------- | --------- | ------ | ---- |
| 5      | In        | 10.1.2.3   | 172.16.3.4 | TCP      | 8080      | Permit | D    |
| 6      | Out       | 172.16.3.4 | 10.1.2.3   | TCP      | 5150      | Permit | B    |
- However, note that packet 5 is sent as part of initiating the connection with the server. Ideally, it should be sent to port 443 (standard port for HTTPS). Here, it is sent to port 8080. But because it matches Rule D, the packet will be permitted.

**Q1 (b) ii**
- Yes, the attack will succeed. This is because both packets 5 & 6 are permitted, allowing the external attacker to establish a connection to the server on port 8080.
- - -

**Q1 (c)**
- Packets 1, 2, 3, 4 are permitted while 5 and 6 are denied.

| Packet | Direction | Src Addr    | Dest Addr   | Protocol | Src Port | Dest Port | Action | Rule |
| ------ | --------- | ----------- | ----------- | -------- | -------- | --------- | ------ | ---- |
| 1      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 1234     | 443       | Permit | A    |
| 2      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 443      | 1234      | Permit | B    |
| 3      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 1357     | 443       | Permit | C    |
| 4      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 443      | 1357      | Permit | D    |
| 5      | In        | 10.1.2.3    | 172.16.3.4  | TCP      | 5150     | 8080      | Deny   | E    |
| 6      | Out       | 172.16.3.4  | 10.1.2.3    | TCP      | 8080     | 5150      | Deny   | E    |
- - -
### Question 02
**Q2 (a)**
- The application server verifies the client by decrypting the service ticket using its own secret share key to extract the session key.
- It then uses the session key to decrypt the client's authenticator, which contains a timestamp and the client ID.
- If the client ID matches and the timestamp is fresh, authenticity is proven.
- - -
**Q2 (b)**
- The authentication server encrypts TGT using the secret key $K_{TGS}$ of the ticket granting server.
- The client or any outside adversary does not have access to $K_{TGS}$.
- Therefore, any alteration to the TGT will corrupt the data, causing decryption to fail at the TGS stage.
- - -
**Q2 (c)**
- The Kerberos protocol uses an authenticator containing the current timestamp.
- The server checks this timestamp against its local clock, and if the message window is outside an acceptable range, the packet is dropped
- Additionally, servers maintain a replay cache within that time range to catch duplicate messages.
- - -
**Q2 (d)**
- 
