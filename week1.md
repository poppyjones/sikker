# Week 1

>The weakest point of cyber security is humans!

## A few lists

### Types of adversaries

- Vandals
  - unmotivated, not really an issue any more.
- Activists
  - Politically motivated.
  - Not a big deal tbh.
- Criminals
  - w. unlawful intensions.
  - Sometimes used by companies to gather info about competition.
- States
  - Main source of current attacks!
  - Have lots of money and resources to finance/enable large scale attacks.

#### FE (CFCS)

>**• Truslen fra cyberterror er LAV.** Begrænsede evner og ressourcer til at udføre alvorlige cyberangreb.
>
>**• Cyberaktivisme: MIDDEL.** Cyberaktivister retter sjældent fokus på danske myndigheder og virksomheder.
>Visse grupper har væsentlige evner og ressourcer til at udføre cyberangreb.
>
>**• Cyberkriminalitet: MEGET HØJ.** Myndigheder, virksomheder og borgere.
>Særligt afpresning af myndigheder, virksomheder og borgere.
>Visse netværk arbejder organiseret og langsigtet, sandsynligvis statsstøttet.
>
>**• Cyberspionage: MEGET HØJ.** Mål: Danske myndigheder, evt. virksomheder.
>
>**• Visse stater bruger cyberangreb til at styrke deres magtposition.** Risiko for destruktive cyberangreb, hvis en virksomhed er til stede i visse konfliktområder.

### Types of Assets

- Hardware
  - Any data processing, storing, or communication services.
- Software
  - Including OS, system utilities, and applications.
- Data
  - files, DBs, any security related data (passwords, private keys, and whatnot).
- Communication facilities and networks
  - both local and wide com links, bridges, routers, etc.

### Types of vulnerabilities

Being..

- Corrupted
- Leaky
- Unavailable

See the CIA triad for more.

### Types of threats

Page 32 has a good overview.

#### Unauthorised disclosure (Confidentiality)

Something happens which leads to an entity gaining info that it is not authorisation to access.

- **Exposure**: Can be active/inside (someone leaks something), or unintentional (software/hardware error)
- **Interception**: Someone gains access to a copy of information (maybe on a shared LAN)
- **Inference**: Using traffic analysis or basic queries to infer something bigger about activities of others.
- **Intrusion**: breaking and entering

#### Deception

A threat to system- or data integrity. By making entities believe something false is true (not in the boolean sense).

- **Masquerage**: Gaining access by posing as a authorised user. (Simply knowing the username and password or more advanced like a trojan horse)
- **Falseification**: Altering/replacing data with false data. (entering own grades to learnit).
- **Repudiation**: When a user denies that it sent and or received data.

#### Disruption

Threat to the availability or system integrity. Interuption or preventing the system to operate correctly.

- **Incapacitation**: Attack on system availibity by disabling a component. Could be physical harm to hardware, more commonly Trojan horse, virus, worm that disable the system. (ex. stuxnet)
- **Corruption**: Attack on integrity; altering system operation by altering functions or data. This could be many things, one example is leaving a backdoor.
- **Obstruction**: Obstruction communications. Snip snip or overloading the comm system (dos).

#### Usurpation

Threat to integrity. An event that leads to an unauthorised entity gains control of services or functions.

- **Misappropriation**: Theft og service (logical or physical). DDoS w use of maliious software to send the excess traffic.
- **Misuse**: Cause a component to perform in a way detrimental to system security.

### Types of Attacks

- Active
  - attempts to alter system resources or affect operations
- Passive
  - attempts to learn and/or make use of information from the system but does not alter anything.
- Inside
  - Initiated by an entity *inside* a security measure. Someone who is authorised and is supposed to be authorised (ligitimate) can access a servie or some data, but uses/shares it in a way unintended by the entity who granted the authorisation.  
- Outside
  - Initiated by unauthorised or illigitimate users.

#### Spear-phishing

Specific phishing emails. NOT nigerian prince, but "Hey hi, I know you! let me in".
Active, outside.

### Countermeasures

>Means taken to deal with a security attack

**Ideally**: Preventing an attack from succeeding
**Otherwise**: Detect failure and recover.

Some counter measures may introduce new vulnerabilies. And there will probably still be vulnerabilies after one/some countermeasure have been taken care of.
Vulnerabilities put the assets at **risk**.

## Security assumptions

Assumptions are potential vulnerability.

### Technical Assumptions

**Stuxnet**: The attack on the Iranian uranium enrichment plant! The Assumption was - "No USB keys, therefore no entry point".

## Security goals (CIA(AA))

### Confidentiality

Meaning secrecy of data. "Preserving authorised restrivtions on information access and disclosure".

**Data confidentiality**: Assuring that private/confidential data is not available to unautorised individuals/entities.

**Privacy**: That individuals have control over who can access, collect, or store their personal.

**Associated vulnerability**: leakiness

**Attacks**:

- Eavesdropping
- Man in the middle

### Integrity

Ensuring assets can't be altered wo. permission. "Guarding against improper information modification or destruction."
May include ensuring *non-repudiation* and *authenticity*.

>Non-repudiation is the assurance that someone cannot deny the validity of something. Non-repudiation is a legal concept that is widely used in information security and refers to a service, which provides proof of the origin of data and the integrity of the data. In other words, non-repudiation makes it very difficult to successfully deny who/where a message came from as well as the authenticity and integrity of that message.

**Data integrity**:  Ensuring information isn't altered.

Historical case: Mary Queen of Scots sent weakly encrypted message which leads to her revealing her accomplices.

**System integrity**: Insuring a system works as intended. Free from unintended or deliberate manipulation of system functions.

"Historical case": Calibrating the whiteboard incorrectly at school.

**Associated vulnerability**: Corruption
  
- something does something wrong...
- something is improperly modified.

### Avalability

Duh! Timely and reliable, please!

**Associated vulnerability**: unavailability. (duh!)

**Attacks**:

- Denial of service
- distributed denial of service.

Example: Drone over Gatwick cost buckets of money :)

### Accountability

Using logs and whatnot to backtrack and find out who made the attack????

>The security goal that generates the requirement for actions of an entity to be traced uniquely to that entity. This supports nonrepudiation, deterrence, fault isolation, intrusion detection and prevention, and after-action recovery and legal action. Because truly secure systems are not yet an achievable goal, we must be able to trace a security breach to a responsible party.
> Systems must keep records of their activities to permit later forensic analysis to trace security breaches or to aid in transaction disputes.

Quote from book.

### Authencity

Ensuring that data or a service is genuine. Making something verifiable and trusted.

This one is tricky to ensure.

## Security is hard!

Even though the requirements seem straightforward and self explanatory. When designing security measure you have to think of the unexpected exploitations.

The defender must attack **ALL** possible attacks.
The attacker just needs to find the weakest link.

> Having designed various security mechanisms, it is necessary to decide where to use them. This is true both in terms of physical placement (e.g., at what points in a network are certain security mechanisms needed) and in a logical sense [e.g., at what layer or layers of an architecture such as TCP/IP (Transmission Control
Protocol/Internet Protocol) should mechanisms be placed].

Even if all security measures are in place there is still one issue: ***The weakest point of cyber security is humans!***

Also time!!!

Also people don't care until they have experienced an attack.

It's expensive and may require monitoring.

Sometimes security is a percieved hinderance to user friendliness.

## Security Design Principles

Economy of principles aka. Economy of mechanism.

- Keep It Simple Stupid.
- Complex design yields complex failure analysis.

Open design.

- Does not mean open source.
- The security of a system should ot depend on the security of the secrecy of the protection mechanism.
- example: 2005 DRM (digital rights managment??). The system was broken within a month and turned out to be a way to....
- Iowa caucus app is an example of why this is important

Minimum exposure

- Only have the software/hardware that you really need
- example: bluetooth on linux

Least Privilege

- Any component should operate using the least set of privileges.
- Accessing something basic as an admin shouldn't run on admin privileges.

Fail safe default

- In Die Hard the vault default should be a locked door. (In any other case it should be opposite for fire safety)
- **Permission rather than exclusion**.

Complete mediation

- Access to **any** object must be controlled.
- "Don't rely on cache." but checking every time is to resource intensive.
- example: Maginot line - France (WWII?)

No Single point of failure

- The attacker only needs one weak point.
- Redundant security mechanism is good for this
  - multi factor authentication.
  
Phycological acceptability

- Design usable security mechanisms.
- Help users make the right choice.
  - "Should i click Yes"
- Therefore, avoid human interaction....

Seperation of privilege

- Each thing has it's own previlege requirements.

Least Common Mechanism

- Minimise functions shared by diff. users.
- This helps reduce unintended communication paths.

Isolation

- Public access systems should be **isolated** from critical resouces.
- other stuff page 42

Encapsulation

- Isolation w use fo OO-functionality.
- Designate domain entry points.

Modularity

- Developement of security functions
- Protected modules
- use modular architecture for mechanism design and implementation.

Layering

- overlapping protection

Least Astonishment

- UX should be transparent and intuitive

### Attack surfaces

> Reachable and exploitable vulnerabilities in a system.

- **Network attack surface**
- **Software attack surface**
- **Human attack surface**

Examples:

- Open ports on outward facing Web and other servers, and code listening on
those ports
Services available on the inside of a firewall
- Code that processes incoming data, e-mail, XML, office documents, and
industry-
specific custom data exchange formats
- Interfaces, SQL, and web forms
- An employee with access to sensitive information vulnerable to a social engineering
attack

### Summary

- Adversary: *state-sponsored* cyber attacks
- Assumptions: as **few** as possible
- Goals: as **many** as possible
- Principles: as **many** as possible
- Resort to maths!

## Group Theory

Basis of some cryptography?

### definition of group

A Group is a set with is associated with a binary operator (that is an operator to combine two elements in the set).

A set *G* under the closed binary operation * is a group denoted (*G*,*) or simply *G* iff

1. The operation must be associative
   - a \* ( b * c ) = ( a * b ) * c
2. Must have an identity element (neutral element)
   - If we use the operator on the identity and any other element (*x*) it returns the element *x*
3. Every element must have an inverse
   - for all a in *G* there exists b in *G* such that a*b=e and b*a=e

4. The group is closed under the operation
   - for all elements if a and b are elements in *G*, a*b is also in *G*

***TODO: Check somewhere other than slides!!!***

## Cyclic groups

Groups where applying the operation a finite number of times will cycle through all elements of the group.

An example being the group *G = {0,1,2,3}* and the operator being .
