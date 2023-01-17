#!/usr/bin/env python
import math


def calc_conc():
    """
    calculate the number of molecules to construct the Box, output the number of each
    molecule
    """
    concMain = 0.8  # concentration of main salt in mol/L
    concMinor = 0.2 # concentration of secondary salt
    solventDensity = 800 # estimated molar density of main solvent
    solventMW = 100
    solventConc = solventDensity / solventMW #mol/L
    boxLengthX = 50 # in Angstrom
    N_Av = 0.602  # Avgadro's constant
    vol = boxLengthX ** 3 / 1000 # nm3
    additionalComponents = [0.01, 0.01] # concontration of aditives, will round up in actual calculation
    numSol = vol *  solventConc * N_Av
    numSaltMain = concMain * vol * N_Av
    numSaltMinor = concMinor * vol * N_Av
    outputList = ([int(numSol), math.ceil(numSaltMain), math.ceil(numSaltMinor)])
    outputList += [math.ceil(conc * vol * N_Av) for conc in additionalComponents]
    return outputList


if __name__ == '__main__':
    printlist = calc_conc()
    print(printlist)
