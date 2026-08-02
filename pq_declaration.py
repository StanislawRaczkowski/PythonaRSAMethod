from math import sqrt
import random

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def getpq():
    print("Please, insert two distinct prime numbers, or if You wish \n"
          "to choose random p and q, insert RANDOM: \n"
          "(Note that those random chosen numbers \n"
          "will be from between 2^4 and 2^16. Also note that\n"
          "inserting RANDOM for one input will make both numbers random. Also\n"
          "make sure, that the product of p and q is greater than 256, as \n"
          "later parts of the program will need You to write a message to be encrypted \n"
          "and letters from Your message will be in converted to ASCII/Unicode which contains up to\n"
          "256 characters, and in order for RSA method to work, in later parts m must be\n"
          "lesser than n):")
    while True:
        p = input("Please, insert p: ").strip()
        q = input("Please, insert q: ").strip()
    #     Losowanie wpierw:
        if p == "RANDOM" or q == "RANDOM":
            p = random.randint(2 ** 4, 2 ** 16)
            while not isPrime(p):
                p = random.randint(2 ** 4, 2 ** 16)
            q = random.randint(2 ** 4, 2 ** 16)
            while not isPrime(q):
                q = random.randint(2 ** 4, 2 ** 16)
            while p == q:
                q = random.randint(2 ** 4, 2 ** 16)
            n = p * q
            print(f"> Selected primes: p = {p}, q = {q}, n = p*q = {n}")
            return p, q, n
    #     Opcja wpisania normalnie:
        if (p and q) != "RANDOM":
            try:
                p_val = int(p)
                q_val = int(q)
            except ValueError:
                print("That's not an int! Please try again.\n")
                continue
            if isPrime(p_val) is False or p_val == q_val or isPrime(q_val) is False:
                print("Wrong input, numbers are not prime or are equal.")
                continue
            elif q_val * p_val < 256:
                print("Your p and q are too small and there will be problems with decrypting. \n However if You wish, You can"
                      "continue and see for yourself, if You encounter something strange.")
                permission = input("If You want to proceed with given p and q\n write Yes. Any other input will\n start p and q declaration again. \n")
                if str(permission) == "Yes":
                    n = int(p) * int(q)
                    print(f"> Selected primes: p = {p}, q = {q}, n = p*q = {n}")
                    return int(p), int(q), int(n)

                else:
                    continue
            else:
                n = int(p) * int(q)
                print(f"> Selected primes: p = {p}, q = {q}, n = p*q = {n}")

                return int(p), int(q), int(n)


# getpq()