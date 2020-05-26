import random

g   = 666
p   = 6661
bPk = 2227
y   = random.randint(1,g)

print("1: Alice's private key (y) = " + str(y))

aBk = (g ** y) % p
print("2: Alice's public key      = " + str(aBk))

privKey = (bPk ** y) % p
print("3: Shared private key      = " + str(privKey))

c = privKey * 2000
print("4: Cipher-text             = " + str(c))
