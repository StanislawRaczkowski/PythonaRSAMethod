
def Encrypting(e, n):
    # That will be propably most important function, I hope it works well.
    print(f"> Now we will begin encrypting. \nTo do this, we will need some message.\n"
          f"So now is the time for You to write us some message.\n")
    msg = input(f"> Please enter your message: ")
    code_list = []
    for char in msg:
        m = ord(char) # m will be a representation of Unicode of char, as we can only work on integers in RSA method.
        c = pow(m, e, n)
        code_list.append(c)
    print(f"> A list of encrypted numbers from Your message \n is {code_list} \n"
          f"(If your message is long, do not be surprised that the list is long. \n"
          f"Every character in your message was converted to Unicode code. \n"
          f"Then it was encrypted as following: c = m^e mod n, where \n"
          f"m is a unicode representation of single character.\n"
          f"Please note now, that if n would be lesser than 256, value \n"
          f"of m would be cutted by modulo n, making it impossible to \n"
          f"decrypt Your message precisely.")
    return code_list
# Encrypting(12, 3)