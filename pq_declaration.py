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
          "inserting RANDOM for one input will make both numbers random):\n")
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
            if isPrime(p_val) is False or p == q or isPrime(q_val) is False:
                print("Wrong input, numbers are not prime or are equal.")
                continue
            else:
                n = int(p) * int(q)
                print(f"> Selected primes: p = {p}, q = {q}, n = p*q = {n}")

                return p, q, n


# getpq()