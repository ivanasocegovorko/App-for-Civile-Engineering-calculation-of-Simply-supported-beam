import re

def main():

    length = (input("Beam length [m]: ")).strip()
    while not re.search(r"^[1-9][0-9]*\.?[0-9]*", length):
        print ("Lenght must be a positive number")
        length = (input("Beam length [m]: ")).strip()

    load = (input("Line load [kN/m']: ")).strip()
    while not re.search(r"^\-?[1-9][0-9]*\.?[0-9]*", load):
        print ("Load must be number")
        load = (input("Line load [kN/m']: ")).strip()

    E = (input("Modulus of elasticity [kN/cm2]: ")).strip()
    while not re.search(r"^[1-9][0-9]*", E):
        print ("Modulus of elasticity must be a positive number")
        E = (input("Modulus of elasticity [kN/cm2]: ")).strip()
        # For steel E = 21000 kN/cm2

    Iy = (input("Area moment of inertia [cm4]: ")).strip()
    while not re.search(r"^[1-9][0-9]*", Iy):
        print ("Area moment of inertia must be a positive number")
        Iy = (input("Area moment of inertia [cm4]: ")).strip()
        # For steel profile UPE 140 Iy = 630 cm4


    """ printing beam model in usual civile engineering way of represetation """
    print()
    print("Beam model:")
    print("           " + " " + ("|")*30 + " " + load + "kN/m'")
    print("           " + " " + ("ˇ")*30)
    print("           " + "△" + ("‾")*30 + "△")
    print("           " + " " + (" ")*30 + "‾‾")
    print("           " + (" ")*12 + "l = " + length + "m")
    print()

    print(f"Shear force = {shear_force(length, load)} kN")
    print(f"Bending moment = {bending_moment(length, load)} kNm")
    print(f"Support reaction = Ra = Rb = {support_reactions(length, load)} kN")
    print(f"Max deflection = {max_deflection(length, load, E, Iy)} mm")
    print()


def shear_force(length, load):
    s_force = (float(load) * float(length)) / 2
    return s_force


def bending_moment(length, load):
    b_moment = (float(load) * float(length)** 2) / 8
    return b_moment


def support_reactions(length, load):
    s_reaction = (float(load) * float(length)) / 2
    return s_reaction


def max_deflection(length, load, E, Iy):
    m_deflection = round(((5 / 384) * (float(load) * float(length)**4) / ((float(E)*10000) * (float(Iy)/100000000))) * 1000, 4)
    return m_deflection


if __name__ == "__main__":
    main()
