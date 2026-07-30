import random
def Phi(p,q):
    Phi = (p-1)*(q-1)
    return Phi
# It is called Eulre's function and has its uses in modular arithmetics.
# In order to find gcd (NWD in polish) we will use Euclides alghoritm.
def GCD(p,q):
    while q != 0:
        o = p % q
        p = q
        q = o
    return p

def SearchE(Phi):
    # Value of e should be 1 < e < Phi(n)
    e = random.randint(2,Phi - 1)
    while GCD(e, Phi) != 1:
        e = random.randint(1,Phi)
    return e


print(Phi(7,92), GCD(Phi(432,14),74654), SearchE(Phi(42,321)))
