#Digital Signature: the following program signs a message and then verifies it's signature using RSA

#helpers
def gcd(m, n): return m if (n == 0) else gcd(n, m % n)
def swap(old, q, current): return current, old - q * current

#MULTIPLICATIVE INVERSE
def extended_euclidean(x, y):
    old_r, current_r = x, y
    old_s, current_s = 1, 0
    old_t, current_t = 0, 1
    while (current_r):
        quotient = old_r // current_r
        old_r, current_r = swap(old_r, quotient, current_r)
        old_s, current_s = swap(old_s, quotient, current_s)
        old_t, current_t = swap(old_t, quotient, current_t)
    return old_s, old_t, old_r

def modular_inverse(a, m):
    x, y, g = extended_euclidean(a, m)
    if g == 1: return x % m
    else: print("modular_inverse: it doesn't exist")

class RSA:
    def __init__(self, p, q, e = 3):
        self.p = p
        self.q = q
        self.e = int(e)
    def generate_keys(self):
        self.n = self.q * self.p
        self.phi = (self.p - 1) * (self.q - 1)
        self.d = modular_inverse(self.e, self.phi)
        if (self.phi % self.e == 0): print("choose different keys")
    def private_key(self): return (self.d, self.n)
    def public_key(self): return (self.e, self.n)

#SIGNING ALGORITHM
def sign_message(message, private_key):
    return (message**private_key[0]) % private_key[1]

def unsign_message(signature, public_key):
    return (signature**public_key[0]) % public_key[1]

def verify_signature(message, signature, public_key):
    return message == unsign_message(signature, public_key)

message = 324343

rsa = RSA(823, 953, 313)
rsa.generate_keys()

private_key = rsa.private_key()
public_key = rsa.public_key()

signature = sign_message(message, private_key)

if (verify_signature(message, signature, public_key)):
    print("the message has been verified")
else:
    print("the message can't be verified")
