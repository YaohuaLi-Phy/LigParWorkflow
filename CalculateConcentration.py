#!/usr/bin/env python
import math

def calc_conc():
    """
    calculate the number of molecules to construct the Box, output the number of each
    molecule
    """
    # components: solvent, LiPF6 0.8M, additional: dfob- 0.2M

    concMain = 0.7  # concentration of main salt in mol/L
    concLi = 1.0 # concentration of secondary salt
    solventDensity = 820 # estimated molar density of main solvent
    solventMW = 221
    solventConc = solventDensity / solventMW #mol/L
    boxLengthX = 50 # in Angstrom
    N_Av = 0.602  # Avgadro's constant
    vol = boxLengthX ** 3 / 1000 # nm3
    addSaltConc = [0.3]
    numAddSalt = [round(conc * vol * N_Av) for conc in addSaltConc]
    additiveConc = [] # concontration of aditives, will round up in actual calculation
    numAddComponents = [round(conc * vol * N_Av) for conc in additiveConc]
    numSol = vol *  solventConc * N_Av
    numSaltMain = concMain * vol * N_Av
    #numSaltLi = concLi * vol * N_Av  # might cause non neutral charge
    numSaltLi = numSaltMain + sum(numAddSalt)
    outputList = ([int(numSol), round(numSaltLi), round(numSaltMain)])


    outputList = outputList + numAddSalt + numAddComponents
    return outputList


if __name__ == '__main__':
    printlist = calc_conc()
    print(printlist)
