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
| 1      | In        | 192.168.3.4 | 172.16.1.1  |          | 443       | Permit | A    |
| 2      | Out       | 172.16.1.1  | 192.168.3.4 |          | 1234      | Permit | B    |
| 3      | Out       | 172.16.1.1  | 192.168     |          | 443       | Permit | C    |
| 4      | In        | 192.168.3.4 |             |          | 1357      | Permit | D    |

**Q1 (b)**
- 