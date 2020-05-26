# Exercises

## Not group theory

### 1.1

> Consider a student information system (SIS) in which students provide a university student number (USN) and a card for account access. Give examples of confidentiality, integrity, and availability requirements associated with the system and, in each case, indicate the degree of the importance of the requirement.

### 1.4

> In exercise 1.4 use table 1.3 (p. 35) for asset and threat identification and the definitions of impact level on p 26/27.

> For each of the following assets, assign a low, moderate, or high impact level for the loss of confidentiality, availability, and integrity, respectively. Justify your answers.
>
> - a. An organization managing public information on its Web server.
> - b. A law enforcement organization managing extremely sensitive investigative information.
> - c. A financial organization managing routine administrative information (not privacy related information).
> - d. An information system used for large acquisitions in a contracting organization contains both sensitive, pre-solicitation phase contract information and routine administrative information. Assess the impact for the two data sets separately and the information system as a whole.
> - e. A power plant contains a SCADA (supervisory control and data acquisition) system controlling the distribution of electric power for a large military installation. The SCADA system contains both real-time sensor data and routine administrative information. Assess the impact for the two data sets separately and the information system as a whole.

Q   | Confidentiality | Integrity | Availabiliy
--- | --- | --- |----
a   | **low**  | high (depending on the info) | med
b   | very high | very high | med/high
c   | high | high | low
d1  | high | high | low
d2  | med  | medb | med
d   | high | high | med
e1  | high | high | high
e2  | med  | high | high
e   | high | high | high

### 1.5

> Consider the following general code for allowing access to a resource:

    DWORD dwRet = IsAccessAllowed(...);
    if (dwRet == ERROR_ACCESS_DENIED) {
    // Security check failed.
    // Inform user that access is denied.
    } else {
    // Security check OK.
    }

> - a. Explain the security flaw in this program.
> - b. Rewrite the code to avoid the flaw.
> *Hint: Consider the design principle of fail-safe defaults.*

- **a.** Failure safe default. So long as access in NOT denied the entity has access. T
- **b.**

    DWORD dwRet = IsAccessAllowed(...);
    if (dwRet == ACCESS_ALLOWED) {
    // Security check OK.
    } else {
    // Security check failed.
    // Inform user that access is denied.
    }

#### The IT department is considering to introduce multi-step authentication to protect their users. Before applying the new policy, the department asks for your advice. Multi-step authentication requires the user to choose any two of the following authentication methods at each login.

- Password
- Fingerprint recognition
- Student card
- SMS via phone
- Call via phone
- Email confirmation
- Iris Scanning

> Give a recommendation: should this policy be adopted or not? Use security principles to motivate your recommendation.

Password & student card

## Group theory

Demonstrate that the following are groups. State what are the neutral elements and inverse operators:

### 1.1 Integers with addition. Use things you know addition, e.g., (x + y) + z = x + (y + z) or x + 0 = x.

**Neutral element:** 0 eks. 5+0=5

**Inverse operators:** the inverse of x is -x 

### 1.2 16-bit strings with xor.

XOR is orerated on every bit of the operand by adding the values and applying mod(the max val) an the result.

eks: *a* = 1001, b = 0101 in a binary string. a XOR b = 1+0 mod 2, 0+1 mod 2, 0 + 0 mod 2, 1 + 1 mod 2 = 1100

The same goes for 16-bit words, except w mod 16

**Neutral element:** 0 eks: B+0 = B 

**Inverse operators:** same

### 1.3 The numbers from 0 to 19 with wrap-around addition (18+1 = 19, 18+2 = 0, 18+3 = 1, ...).

- Hint 1: You don't need to think when your computer can simply check.

- Hint 2: In many modern programming languages "wrap-around addition" can be achieved something with the modulus operator %. E.g., in python:

    def compose (g,h):
        return (g + h) % 20

**Neutral element:** 0

**Inverse operators:** still +, as in 2+19=1 and 19+2=1

## Demonstrate that the following are not groups:

### 2.1 Integers with multiplication.

The inverse operation is missing. You can't multiply 2 to get 1 wo. using the rational number 1/2

### 2.2 Lists with list concatenation.

Man kan ikke have en liste med anti-elementer... aka. elementer der fjerner ting fra en liste.

### In your favourite program, implement a type/interface/protocol/abstract class that represents the abstract concept of "a mathematical group", that is, a possibly infinite set of elements, a neutral element, a binary composition operator, and a unary invert operator.

### 3.1. Implement (1) integers with addition, and (2) 16-bit bit strings with xor.

### 3.2. Test, for both implementations, that your implementation satisfies group laws.

### 3.3. Implement a general exponentiation operator that works on any group implementation.