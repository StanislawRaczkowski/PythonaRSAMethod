import random
def Phi(p,q):
    Phi = (p-1)*(q-1)
    print(f"> A function Phi(n), which \n is calculated as (p-1)*(q-1), has value of: {Phi}")
    return Phi
# It is called Eulre's function and has its uses in modular arithmetics.
# In order to find gcd (NWD in polish) we will use Euclides alghorithm.
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
    print(f"> A randomly selected value of e, which must \n satisfy the condition 1 < e < Phi(n)\n and must be relatively prime to Phi(n) is e = {e}")
    return e


print(Phi(7,92), GCD(Phi(432,14),74654), SearchE(Phi(42,321)))
