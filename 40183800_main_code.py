import random
# Random number generator
def Randomnumber():
    while (1):
        number = random.randint(32769, 65536)
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                return number


# computing GCD of 2 numbers
def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


# computing the multiplicative inverse of edmod(ϕ(n))= 1
def invmod(a, n):
    b = n
    s1, s2 = 1, 0
    while (b):
        a, (q, b) = b, divmod(a, b)
        s1, s2 = s2, s1 - q * s2
    if a != 1:
        raise ValueError('Inverse does not exist')
    return s1 if s1 >= 0 else s1 + n


def Squareandmultiply(expo, e, N):
    t = 1;
    while (e > 0):
        if (e % 2 != 0):
            t = (t * expo) % N;
        expo = (expo * expo) % N;
        e = int(e / 2);
    return t % N


# Encrypting a message
def Encryption(msg, e, N):
    chunks = [msg[i:i + 3] for i in range(0, len(msg), 3)]
    print("Message Chunks: ", chunks)
    num = [int("0x" + i.encode('utf-8').hex(), 16) for i in chunks]
    print("Integers Values:", num)
    ans = [Squareandmultiply(i, e, N) for i in num]
    return ans


# Decrypting the partner message
def Decryption(encrValues, d, N):
    dercrypt = [bytearray.fromhex(str(hex(Squareandmultiply(i, d, N)))[2:]).decode() for i in encrValues]
    return "".join(dercrypt)


# Signature of our name
def signature(msg, d, N):
    chunks = [msg[i:i + 3] for i in range(0, len(msg), 3)]
    print("Message Chunks: ", chunks)
    num = [int("0x" + i.encode('utf-8').hex(), 16) for i in chunks]
    ans = [Squareandmultiply(i, d, N) for i in num]
    return ans


# Verification of the partner signature
def verification(verVal, verText, e, N):
    decr_partner_val = Decryption(verVal, e, N)
    if (decr_partner_val == verText):
        print('Signature verification is: Success')
    else:
        print('Signature verification is: Failure')
    print(verText)


# Two large primes using Random Number Generator
P = Randomnumber()
Q = Randomnumber()
if (P == Q):
    Q = Randomnumber()

# Calculating Public Key N
N = P * Q

# Calculating ϕ(n) using 2 large primes P and Q
phi = (P - 1) * (Q - 1)

# Generating a public key e using ϕ(n)
e = random.randint(1, phi) % phi
while (GCD(e, phi) != 1):
    e = random.randint(1, phi) % phi

# private key d
d = invmod(e, phi)

print("Choose the operation!!")
print("0 for Encryption")
print("1 for Decryption")
print("2 for Signature")
print("3 for Verification")

Operation = int(input())

partner_e, partner_N = 894719009, 1462985857
my_d, my_n = 77506573, 1857792883

# Encryption
if (Operation == 0):
    msg = "This is RSA Crypto system"
    encrypMsg = Encryption(msg, partner_e, partner_N)
    print("Encrypted message is = ", encrypMsg)

# Decryption
elif (Operation == 1):
    my_d = 77506573
    partner_message = [623290021, 30838988, 1832055710, 42370594, 1287969018]
    print("Decrypted message is = ", Decryption(partner_message, my_d, my_n))

# Signature
elif (Operation == 2):
    name = "Pujitha Grandhi"
    sign = signature(name, my_d, my_n)
    print("Signature = ", sign)

# Verification
elif (Operation == 3):
    verify = [1784312, 939233908, 1374701801, 249599062]
    ver_partner_text = "adnan zuhaib"
    name = verification(verify, ver_partner_text, partner_e, partner_N)

else:
    print("Invalid Operation!")
