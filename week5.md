# Week 5

## Internet authentication applications

Including the early, yet widely use, *Kerberos*, then X.509 public-key certificates, and the concept of public-key infrastucture (PKI)

### Kerberos

Originally developed by MIT, Kerberos is a software utility which uses software tied to secure authentication servers to ensure secure networked servers and hosts by mediating their mutual authentication.

Kerberos makes use of a protocol that involves clients, hosts and a Kerberos server. In an unprotected network environment any client can apply to any server for service. If each server has to authenticate its own clients the server will be a substantial burden. Alternatively an authentication server (AS) can be used to ensure the identity of ones clients. The AS knows the passwords of all clients and stores them in a centralised db. The question is, how to implement an AS safely? answer: encryption.

Originally Kerberos used DES and it's encryption algorithm, currently is uses AES. Someone logs on to a workstation, the client process sends a msg to the AS w user-ID and request for *ticket-granting ticket* (TGT). The AS checks db to find user password, generates key and attemps to decrypt incoming msg. This way the password its self is never passed over the network. The ticket (user-ID, server-ID, timestamp, lifetime,session-key) is encrypted by the AS and sent back. The tgt grants more tickets from a tgs (ticket granting server), duh! this means the same authentication service doesn't have to be run too many times.

The important variable here is the lifetime. If to short, the user has to reauthenticate a lot. If too long, there there is a vulnerability since an attacker could spoof the tgs. However, this is avoided by using the session key. every new tgt from the tgs is encrypted w the old session key and encludes a new session key. This way, only the true owner of the ticket can decrypt the new ticket.

#### Kerberos Realm

1. The Kerberos server must have the user ID and password of all participating users in its database. All users are registered with the Kerberos server.
2. The Kerberos server must share a secret key with each server. All servers are registered with the Kerberos server.

This called a *realm*.

*inter-realm communication* is when multiple kerberos reamls access each other. this is generally not practical. (read more on page 711)

#### Performance

If the system is properly configured Kerberos has very little affect on performance, even on large scale environments.

### X.509

Public key certificate links a pub key with the identity of the key owner, the whole thing is signed by a trusted 3rd party, usually a *certificate authority* (CA). The CA should be trusted by the user community, typically it will be a gov agency, financial institution or telecom comp. The *end user* (who owns the key) can publish it or otherwise share it with who ever they want.

The X.509 public key certificate is the most widely accepted format and includes elements shown in figure on page 714.

Types of X.509 certificates include:

- **Conventional** (long-lived) certificates: typical certificates. used by CAs and end users. usually issued for months or years.
- **Short-lived** certificates are used for applications sa grid computing, wile avoiding some overhead and limitations of conventional certs. Validity lasts a few hours or days. Not necc issued from a recognised CA and therefore there are issues verifying them outside of their issuing org.
- **Proxy** certificates are also used for appliations sa grid computing, yet address some of the issues w short-lived certs. Have a proxy-certificate extension which allows an end-user to sign a certificate.
- **Attribute** certificates link users identity to a set of attributes, typically used for authorisation and access control.

### Public key infrastructure

A set of hardware software, people policies and procedures need to create, manage, store, distribute, and revoke digital certificates based on asym-crypto.

Who signs what, can you trace to the top of a signiture tree?

The x.509 originally assumed the PKI model would have a single international root CA and a regulated hierarchy. This did not happen. CA directly sign end users or sign a small nr of intermediate CAs to sign end users. Thus all heirarchy is v smol and equally trusted.

#### A few problems

This PKI model relies on users making informed decisions when there is a problem verifying a certificate. This does not happen...

Although perceived s though they are equally trusted and well-managed all CAs in the "trust store" are not equal. There are services to improve the practicalities of x.509 read more on p  717.

---

## Lecture notes

> nonces: random umbers that are only used once. for freshness

dolev-yao: controls network, but can't break cryptography. Diffie-hellman is not good enough since M can drop the authentication messages and generate own keys to act as a man-in-the-middle attack. this also negates confidentiality since A and B encrypt useing the keys coming from M.

Needham-schroder: 3 messages to generate shared key N1N2 for mutual authentication. Valid and safe for 18 but broken by Lowes attack. **Solution Needham-schroder-Lowe**

Mutual authentiction
