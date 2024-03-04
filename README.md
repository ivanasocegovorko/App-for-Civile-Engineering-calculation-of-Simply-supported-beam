    # SIMPLY SUPPORTED BEAM WITH LINE LOAD - CALCULATIONS
    #### Video Demo:  <https://youtu.be/eRUpPJlKDKY>

    #### Prerequisites:
    For program project.py to run you need to have regex installed.
    To instal it use: pip install regex

    For program test_project.py to run you need to have regex installed.
    To instal it use: pip install pytest

    #### Description:
    Since I have masters in Civil Engineering (structural engineering) in my final project
    I wanted to incorporate what I have learned in CS50 Python with what I use everyday in my structural calculations.

    My project.py calculates all necessary information for a simply supported line beam
    that has even line load.
    #### Calculation are:
        1. Shear force (shearing forces are unaligned forces acting on one part of a body in a specific direction, and another part of the body in the opposite direction)
        2. Bending moment (a bending moment is the reaction induced in a structural element when an external force or moment is applied to the element, causing the element to bend)
        3. Support reaction (reactions in beam supports - in this case supports at the beginning and at the end of the beam)
        4. Max deflection (the deflection of the beam towards in a particular direction when force is applied to it)

    To calculate these first the program prompts the user for few key informations:
        1. Beam length in m
        2. Line load in kN/m
        3. Modulus of elasticity in kN/cm2
        4. Area moment of inertia in cm4

    #### shear_force(length, load)
    To calculate shear force program project.py calls function shear_force(length, load).
    Function shear_force(length, load) take in 2 arguments: length and line load.
    Length is in m, and line load is in kN/m.
    End result is returned in kN.

    #### bending_moment(length, load)
    To calculate bending moment program project.py calls function bending_moment(length, load).
    Function bending_moment(length, load) take in 2 arguments: length and line load.
    Length is in m, and line load is in kN/m.
    End result is returned in kNm.

    #### support_reactions(length, load)
    To calculate support reactions program project.py calls function support_reactions(length, load).
    Function bending_moment(length, load) take in 2 arguments: length and line load.
    Length is in m, and line load is in kN/m.
    End result is returned in kN.

    #### max_deflection(length, load, E, Iy)
    To calculate max deflection program project.py calls function max_deflection(length, load, E, Iy).
    Function max_deflection(length, load, E, Iy) take in 4 arguments: length, line load, E Modulus of elasticity and Iy Area moment of inertia.
    Length is in m, line load is in kN/m, Modulus of elasticity is in kN/cm2 and Area moment of inertia is in cm4.
    End result is returned in mm.

    If the user did not input these informations in right format (such as number, or positive number)
    the user is prompted again with the same input question until the user writes the right format.

    After that the program prints the beam model as it is used in structural engineering.
    And after that program calculates and prints all the wanted calculation.

    #### test_project.py
    In the test_project.py we test all of the functions used in project.py:
        - shear_force(length, load)
        - bending_moment(length, load)
        - support_reactions(length, load)
        - max_deflection(length, load, E, Iy)

    In test_shear_force() test_project tests if shear_force(length, load) returns 50 when argument are:
    length = 10 and load = 10.
    Than in test_shear_force() test_project tests if shear_force(length, load) returns -50 when argument are:
    length = 10 and load = -10.

    In test_bending_moment() test_project tests if bending_moment(length, load) returns 125 when argument are:
    length = 10 and load = 10.
    Than in test_bending_moment() test_project tests if bending_moment(length, load) returns -125 when argument are:
    length = 10 and load = -10.

    In test_support_reactions() test_project tests if support_reactions(length, load) returns 1 when argument are:
    length = 1 and load = 2.
    Than in test_support_reactions() test_project tests if support_reactions(length, load) returns -100000 when argument are:
    length = 100 and load = -2000.

    In test_support_reactions() test_project tests if support_reactions(length, load) returns 1 when argument are:
    length = 1 and load = 2.
    Than in test_support_reactions() test_project tests if support_reactions(length, load) returns -100000 when argument are:
    length = 100 and load = -2000.

    In test_max_deflection() test_project tests if max_deflection(length, load, E, Iy) returns 0.1968 when argument are:
    length = 1, load = 2, E = 21000, Iy = 630.

    #### Author
    Ivana Soče Govorko, MS Civile Engineering
