
# Now we proceed to calculate a d, where d * e = 1 mod Phi(n)
def dcalc(e, Phi):
    d = pow(e, -1, Phi)
    # pow is a power function, build in python. With a power of -1 and a Phi as a third argument, it
    # computes a modular multiplivative inverse of e modulo Phi(n).
    return d
# print(dcalc(5, 2))