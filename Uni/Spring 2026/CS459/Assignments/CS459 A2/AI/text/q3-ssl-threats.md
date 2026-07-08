# Question 3: SSL/TLS and web security threats

## 3(a) Replay attack: earlier SSL handshake messages are replayed

SSL/TLS counters handshake replay attacks by incorporating fresh random nonces from both the client and the server into the key exchange and the derivation of session keys.

In a normal handshake, the client and server each contribute fresh random values. These values are included in the computation of the master secret and later session keys. If an attacker replays old handshake messages, the random values will not line up with the current session, so the Finished messages will fail verification. In many cipher suites, ephemeral key exchange also contributes fresh session-specific material, which further prevents successful replay.

## 3(b) Man-in-the-middle attack: an attacker interposes during key exchange

SSL/TLS counters man-in-the-middle attacks through authenticated key exchange using certificates and public-key signatures.

The server presents a certificate binding its identity to a public key, and the client validates that certificate against trusted certificate authorities. The server also proves possession of the corresponding private key, either directly in the handshake or implicitly through decryption/signing operations depending on the cipher suite. Because the attacker does not possess the legitimate server’s private key, the attacker cannot successfully impersonate the server without causing certificate validation or handshake verification to fail.

Mutual TLS can also authenticate the client using a client certificate, but even standard server-authenticated TLS protects the client from a fake server.

## 3(c) Password sniffing: passwords in HTTP or other application traffic are eavesdropped

SSL/TLS counters password sniffing by encrypting the application data after the handshake completes.

Once the session keys are established, HTTP requests and responses, including usernames and passwords submitted through forms, are encrypted before being sent over the network. An eavesdropper may still see metadata such as IP addresses and packet sizes, but cannot read the actual password content without the session keys.

## 3(d) IP spoofing: forged IP addresses are used to fool a host into accepting bogus data

SSL/TLS counters this only indirectly, not completely.

An attacker who merely spoofs an IP address cannot successfully inject useful SSL/TLS application data, because the attacker will not know the negotiated session keys and therefore cannot produce valid encrypted records or integrity checks. The receiver will reject tampered or forged TLS records.

However, SSL/TLS does not itself stop IP spoofing at the network layer. It protects the application session by requiring cryptographic authentication and integrity, so spoofed packets cannot be used to create a believable secure session.

## 3(e) SYN flooding: many TCP SYN messages are sent without completing the connection

SSL/TLS does not counter SYN flooding.

SYN flooding is a denial-of-service attack against the TCP connection establishment phase, which occurs before the SSL/TLS handshake begins. Since TLS runs on top of TCP, it only starts after the TCP connection is established. Therefore, TLS provides no direct defense against SYN flooding. This attack is usually mitigated using TCP-level or network-level mechanisms such as SYN cookies, backlog tuning, rate limiting, or upstream filtering.
