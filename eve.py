g   = 666
p   = 6661
bPk = 2227

print("Enter Alice's public key")
aPk = int(input())
print("Enter cipher-text")
c = int(input())

x = 0 # Bobs private key
for i in range(p):
    if( (g ** i ) % p == bPk):
            x = i
            break

m = int (c / ((aPk ** x) % p))
print("message: " + str(m))
