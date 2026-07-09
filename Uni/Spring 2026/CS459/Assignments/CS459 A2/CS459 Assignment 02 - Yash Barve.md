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
- The first packet fails but the second packet succeeds.

| Packet | Direction | Src Addr   | Dest Addr  | Protocol | Dest Port | Action | Rule |
| ------ | --------- | ---------- | ---------- | -------- | --------- | ------ | ---- |
| 5      | In        | 10.1.2.3   | 172.16.3.4 | TCP      | 8080      | Deny   | E    |
| 6      | Out       | 172.16.3.4 | 10.1.2.3   | TCP      | 5150      | Permit | B    |
- Note that even though packet 1's details match rule D, the client is attempting to open a connection. Initiation is usually done on port 443 on the server, which is not the case here. Therefore, the packet will be denied.

**Q1 (b) ii**
- No, the attack will not succeed because the connection attempt will be denied.
- - -

**Q1 (c)**
- Packets 1, 3

| Packet | Direction | Src Addr    | Dest Addr   | Protocol | Src Port | Dest Port | Action | Rule |
| ------ | --------- | ----------- | ----------- | -------- | -------- | --------- | ------ | ---- |
| 1      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 1234     | 443       | Permit | A    |
| 2      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 443      | 1234      | Permit | B    |
| 3      | Out       | 172.16.1.1  | 192.168.3.4 | TCP      | 1357     | 443       | Permit | C    |
| 4      | In        | 192.168.3.4 | 172.16.1.1  | TCP      | 443      | 1357      | Permit | D    |
| 5      | In        | 10.1.2.3    | 172.16.3.4  | TCP      | 5150     | 8080      | Deny   | E    |
| 6      | Out       | 172.16.3.4  | 10.1.2.3    | TCP      | 8080     | 5150      | Deny   | E    |
