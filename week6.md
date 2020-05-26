# Week 6

## Secure emails

**S/MIME** secure/Multipurpose Internet Mail Extension: a security enhancement to the MIME email format standard.

### MIME

An extension to the even older RFC 822 specification of an internet mail format(To, From, Subject, additional routing fields). RFC822 assumes ASCII text format. MIME adds new headers fields to define info about the body of the message and any encoding related stuff. MIME defines a number of content formats sa text image audio video.

### S/MIME

Built into most modern email software and interoperates between them. S/MIME is a set of additional MIME content types which provide the ability to sign and/or encrypt email messages. They can be summarised in these for functions

- Enveloped data: encrypted content of any type, encrypted-content encryption keys
- Signed data: digital signature is formed from a msg digest of the content. encrypted w priv-key of signer. The signed message can only be viewed by recipient w S/MIME capability.
- Clear-signed data: as above but only the digital signature is encoded, meaning the recipient doesn't need S/MIME capabilities to view message, however they cant verify the signature.
- Signed and enveloped data: in the name

#### Signed and clear-signed data

The preferred algorithm is usually RSA or DSA signature of a SHA-256 message hash.

> The signature is a binary string, and sending it in that form through the Internet e-mail system could result in unintended alteration of the contents, because some e-mail software will attempt to interpret the message content looking for control characters such as line feeds. To protect the data, either the signature alone or the signature plus the message are mapped into printable ASCII characters using a scheme known as radix-64 or base64 mapping. Radix-64 maps each input group of three octets of binary data into four ASCII characters (see Appendix G)

#### Enveloped data

The default for S/MIME encrypting is AES and RSA.

#### Public key certificates

TODO read page 686 again..

## DOmainkeys identified mail

---

## Lecture notes

> TLS fixes everything??

### Certificate revokation

#### certificate revocation list (CRL)

For when someone realises that their private key is compromised. The old public key and cerficate to the CRL. However! the CRL was not a standard, people had different implementations and they were all difficult to maintian.

Now we use OCSP

#### Online Certificate Status Protocol (OCSP)

The client doesn't have to download the list which makes it less of a burden for client AND network.

Problems: availability, privacy.

A: The CA needs to be online always... which means it can be attacked w DoS

P: The CA can keep a log of all clients actions.

#### However

Chrome and Firefox would still rather use their own CRLs hardcoded in the browsers, giving Google and Mozilla a lot of power.

### What if the CA is compromised

2011 Diginotar - *.google.com

2015-2017 Symantec

2018 DigiCert/Trustico sent private keys by email which lead to 23000 certificates being revoked for bad practice.

### Certificate transparency

Uses logs - think of it as certificate auditing.

The log needs to be fact checked - thish is simply done by making the log an append only logs, this is done w merkel trees

#### Merkel trees

Each parent node is the hash of the concatenation of their two children.
Each leaf stores a certificate.

Audit proofs can be done in O(log n)

Appending new certificates is also done in O(log n)

## Transport Layer Security

1994 - Secure Socket Layer (SSL) introduced by Netscape
1999 - TLS 1.0 working group of IETF
2018 - TLS 1.3

Goal is to provide confidentiality and data integrity, optional: Authentication

C: symmetric encryption
I: MAC (using hash function)
A: Asym encryption

Not a single protocol but a suite of protocols

### Record protocol

Data |> Fragment |> Compress |> MAC |> encrypt |> append SSL header

compression first (remember the way compression uses patterns and re)

authenticate w mac so the authentication is also encrypted and cant be tampered with

### Alert protocol

Fatal alerts and warning alerts

### Heartbeat protocol

Make sure other party is still alive in a tls connection

Heartbleed attack is a notorious attack on the protocol.

### Handshake Protocol (!!!)

Most complex!
TLS 1.2 has 4 msgs and 2 round trips (300 ms)
TLS 1.3 has 3 msgs and 1 round trip (200 ms) (0 rt if resumption (100 ms)) (also deprecates shitty ciphers)

#### 1.2

- 1: A -> B
  - (all in clear tet)
  - Alice establishes cipher-suite
  - nonce
- 2: B -> A
  - Bob chooses cipher from the suite
  - and his public key - signed by a CA
- 3: A -> B
  - TODO read about the TLS handshake protocol!
- 4: B -> A
  - same as 3 basically

#### 1.3

- 1: A -> B
  - same as 1.2
- 2: B -> A
  - everything else!
- 3: A -> B
  - Confirmation

Resumption:

- 1: A -> B
  - Alice and Bob have already agreed on cipher and what not
  - they use the old key to generate the new??
    - Still secure if 1st key leaked
  - kinda like Diffie-Hellman

### Attacks on TLS

Attacks on design

Attacks on implementation

- Heartbleed: used the heartbeat protocol to leak confidential memory. Eve says "Hey server are you alive? if so, reply "hi" (2000 characters)" server replies "hi[+ 1998 characters]"
- TODO see slides

todo hack mit.itu

