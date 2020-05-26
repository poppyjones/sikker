# week 3

## Advanced Encryption Standard (AES)

Issued in 2001 to replace the DES and triple DES stanards.

AES uses a block length of 128 bits and a key length that can be 128, 192, or 256 bits.

the input "block" is copied into a *state* array which is modified at each stage of en- and decryption. After the final stage the state is copied into an output matrix.

The key is split into 4-byte (32-bit) *words* (44 if key of length 128).

- Not a feistel structure?
  - in which half of data is used to modify the other half. then it is swapped.
- 4 distinct word of the key serve as round key for each round.
- 4 stages: 1 permutation, 3 substitution (details p 640)
  - **Substitute bytes**: uses table known as S-box to perform byte-by-byte sub
  - **Shift rows**: permutation performed row by row
  - **Mix columns**: a sub that alters each byte in a column as a func of all bytes in column
  - **Add round key**: bitwise XOR on current block w a portion of the expanded key
  - sometimes shift row and mix columns are group as the diffusion layer
- "quite simple structure"
  - both for en/decryption
  - starts w Add round key. followed by 9 rounds including all 4 stages
  - final round has 3 stages
- only Add round key makes use of the key. the other three stages scramble the bits. Each by it's self is ot impressive but together v cool
- Means each stages is easily reversable
- en and decryption algorithms are not just reverse of each other

### Confusion: substitution layer

With the s-box look up table. **Identical**: The s-box is public and is always used?? Is **non-linear**: the output of adding two elements of the input is not equal to adding the output of those elements. **Bijective**: 1-to-1 mapping of input and output.

### Diffusion

ShiftRows: provides permutation of the data. This is linear. SR(s1)+SR(s2)=SR(s1+s2)

MixCols:

### Key addition

As name states. protects agaist inverting attacks.

## Public key cryptography

### Diffie-Hellman key-exchange

The first appeance of public key cryptography. Enables two users to exchange a private key securely, which is used subsequently. Relies on the fact that discrete logarithms (def. 275) are hard to compute.

### Digital Signature Standard (DSS)

Makes use of SHA-1. 1991, revised 1993.

### Elliptic-curve cryptography (ECC)

RSA. Takes a some processing to do w a secure bit-length.

ECC is showing up? equal to RSA w smaller bitsize. not so cofident cuz new.

## Lecture notes - Cryptography

Helps with Confidentiality and Integrity, not Availability. Relies on maths.

### Fundamentals

algorithm to generate key
algorithm to encrypt plaintext
algorithm to decrypt

### Symmetric cryptography

Uses *same* key to en and decrypt the message. key usualy 128/256 bits. The algorithm must perform well.

Keyspace: the number of possible solutions?

Limitations: how to share keys? (solution Diffie-hellman)

- Caesar cipher
  - keyspace: 26
- mono-alphabetic substitution
  - pairs of symbols allocated randoml
  - keyspace: 26!
- Vernam cipher / one-time pad
  - XOR w the key.
  - "perfect secrecy" because the attacker has no way of knowing whether they have found the correct key??
  - **Problems:**
    - the key must be the same length of the messsage
    - the key can only be used once (XORs cancel each other out)
- DES
- DES3
- AES

#### Block cipher

Such as AES!

- agreee on a short key that can be used to generate a fixed length permutations from the key
- initialization vector

Cipher Block Chaining: XOR w the initialization vector -> some block cipher encryption.

pseudorandom permutation: the output of a secure cipher can't be distinguished

Confusion: when you look at cipher text you should not be able to determine anything about the key.

Diffussion: flipping *one* bit of the plain text should produce a flipping of half the bits of the cipher text.

### Hash and MAC

#### Cryptographic Hash functions

Helps ensure Integrity. Comparing stuff by hash. Is used for virus protection (in theory), OTP (one time passwords), and storing passwords. Hash functions are the basis of many security things...

Takes an arbitrary block of data and returns a fixed size bit string.

Requires

- **Pre-image resistance**: It must be infeasible to find the message (*m*) from the hash of the *m*.
- **Second Pre-image resistance**: its infeasible to find two messages that hash identically. (although this is possible)
- **collision resitance**: we know there is collision (the input is so much bigger than the possible hashed), however we don't have a way of knowing which possible messages will result in the same output.

##### Hash password storing

When you don't store the password, store the hash of the password. This is a bad idea tho. If two people have the same code you will be able to see it. brute force by dictionary.

Salting: adding a random sequence (salt) to a password before hashing.

Use a slow hash function.

#### Message Authentication Codes (MAC)

Helps ensure integrity and authenticity (not confidentiality).

Consists of an algorithm to generate a tag, which is appended to the plain text message. The recipient knows the key. Removes the tag and re-generates tag to check that it generates the correct tag.

Currently: HMAC uses hash function.

### Asymmetric cryptography

Different key to encrypt than decrypt.
every private key has an inverse key (the public key). It is has to compute pk from k.

#### ElGamal

noget med brøker og discrete log problem.

#### Digital signature

By signing w your private key. Authenticity can be assured by using public key to decrypt.
