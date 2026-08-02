import welcome_file
import Phi
import pq_declaration
import dcalc
import CryptingFunctions


def main():
    welcome_file.welcome()
    p, q, n = pq_declaration.getpq()
    Phi_val = Phi.Phi(p, q)
    e_val = Phi.SearchE(Phi_val)
    d_val = dcalc.dcalc(e_val, Phi_val)
    print(f"> So far we have a public key ({n}, {e_val}) and a private key ({n}, {d_val})")
    crypting_list = CryptingFunctions.Encrypting(e_val, n)
if __name__ == "__main__":
    main()