import welcome_file
import Phi
import pq_declaration
import dcalc


def main():
    welcome_file.welcome()
    p, q, n = pq_declaration.getpq()
    Phi_val = Phi.Phi(p, q)
    e_val = Phi.SearchE(Phi_val)
    dcalc.dcalc(e_val, Phi_val)
if __name__ == "__main__":
    main()