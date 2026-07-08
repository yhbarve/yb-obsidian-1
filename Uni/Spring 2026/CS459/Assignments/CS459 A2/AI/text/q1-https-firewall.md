# Question 1: HTTPS packet filtering

## 1(a)

Given the rule set:

| Rule | Direction | Src Addr | Dest Addr | Protocol | Dest Port | Action |
|---|---|---|---|---|---|---|
| A | In | External | Internal | TCP | 443 | Permit |
| B | Out | Internal | External | TCP | >1023 | Permit |
| C | Out | Internal | External | TCP | 443 | Permit |
| D | In | External | Internal | TCP | >1023 | Permit |
| E | Either | Any | Any | Any | Any | Deny |

The four packets are handled as follows.

| Packet | Direction | Src Addr | Dest Addr | Protocol | Dest Port | Action | Rule |
|---|---|---|---|---|---|---|---|
| 1 | In | 192.168.3.4 | 172.16.1.1 | TCP | 443 | Permit | A |
| 2 | Out | 172.16.1.1 | 192.168.3.4 | TCP | 1234 | Permit | B |
| 3 | Out | 172.16.1.1 | 192.168.3.4 | TCP | 443 | Permit | C |
| 4 | In | 192.168.3.4 | 172.16.1.1 | TCP | 1357 | Permit | D |

### Explanation

- Packet 1 is an inbound TCP packet from an external host to the internal HTTPS server on destination port 443, so it matches rule A.
- Packet 2 is an outbound TCP packet from the internal host to an external host using destination port 1234, which is greater than 1023, so it matches rule B.
- Packet 3 is an outbound TCP packet from the internal host to an external host on destination port 443, so it matches rule C.
- Packet 4 is an inbound TCP packet from an external host to an internal host on destination port 1357, which is greater than 1023, so it matches rule D.

This shows the weakness of the filter: it permits traffic based only on destination port and direction, without checking whether the packet is part of a legitimate established connection.

## 1(b)

### (i) Packet decisions

| Packet | Direction | Src Addr | Dest Addr | Protocol | Dest Port | Action | Rule |
|---|---|---|---|---|---|---|---|
| 5 | In | 10.1.2.3 | 172.16.3.4 | TCP | 8080 | Deny | E |
| 6 | Out | 172.16.3.4 | 10.1.2.3 | TCP | 5150 | Permit | B |

### (ii) Will the attack succeed?

No, the attack should not succeed.

The attacker is trying to initiate a connection from an external host to an internal web proxy on destination port 8080. The inbound packet to destination port 8080 does not match rule A, because A only permits inbound packets to destination port 443. It also does not match rule D, because D only permits inbound packets whose destination port is greater than 1023 on the internal side, but the important point is that this would only help packets addressed to ephemeral client ports in a reply path; it does not specifically authorize access to an internal proxy service. Since packet 5 does not match any permit rule, it is denied by rule E.

Because the initial inbound connection attempt is denied, the attacker cannot establish the TCP session to the proxy server. Packet 6 might match rule B in isolation, but without a successfully established connection, that does not let the attack complete.

## 1(c)

Using the extended rule set with source ports:

| Rule | Direction | Src Addr | Dest Addr | Protocol | Src Port | Dest Port | Action |
|---|---|---|---|---|---|---|---|
| A | In | External | Internal | TCP | >1023 | 443 | Permit |
| B | Out | Internal | External | TCP | 443 | >1023 | Permit |
| C | Out | Internal | External | TCP | >1023 | 443 | Permit |
| D | In | External | Internal | TCP | 443 | >1023 | Permit |
| E | Either | Any | Any | Any | Any | Any | Deny |

Applying this to packets 1 through 6:

| Packet | Direction | Src Addr | Dest Addr | Protocol | Src Port | Dest Port | Action | Rule |
|---|---|---|---|---|---|---|---|---|
| 1 | In | 192.168.3.4 | 172.16.1.1 | TCP | 1234 | 443 | Permit | A |
| 2 | Out | 172.16.1.1 | 192.168.3.4 | TCP | 443 | 1234 | Permit | B |
| 3 | Out | 172.16.1.1 | 192.168.3.4 | TCP | 1357 | 443 | Permit | C |
| 4 | In | 192.168.3.4 | 172.16.1.1 | TCP | 443 | 1357 | Permit | D |
| 5 | In | 10.1.2.3 | 172.16.3.4 | TCP | 5150 | 8080 | Deny | E |
| 6 | Out | 172.16.3.4 | 10.1.2.3 | TCP | 8080 | 5150 | Deny | E |

### Explanation

- Packet 1 now matches rule A because HTTPS clients normally use an ephemeral source port greater than 1023 and connect to destination port 443.
- Packet 2 matches rule B because the internal HTTPS server replies from source port 443 to the client’s ephemeral destination port.
- Packet 3 matches rule C because an internal client uses an ephemeral source port to contact an external HTTPS server on destination port 443.
- Packet 4 matches rule D because the external HTTPS server replies from source port 443 to the internal client’s ephemeral destination port.
- Packet 5 is denied because its source port is 5150 and destination port is 8080, which does not fit any HTTPS rule.
- Packet 6 is also denied because a proxy response from source port 8080 to destination port 5150 does not match rule B, which requires source port 443.

### Why the new rule set is better

The new rule set is more precise because it checks both source and destination ports. That lets it distinguish genuine HTTPS request and response traffic from unrelated traffic that merely uses a high-numbered port. In particular, it blocks the proxy attack in part (b), because packets involving port 8080 no longer resemble valid HTTPS traffic.
