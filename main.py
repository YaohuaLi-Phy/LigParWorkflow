#!/usr/bin/env python
import sys
import argparse
import math
import numpy as np
from WriteInp import  write_pack_inp
from CalcConc import calc_conc


#molNumber = calc_conc()
molNumber = [400, 20, 20]
# define cross-functional constants
concMain = 0.8
saltMain = 'pf6-'

class SimulationSystem(object):
    def __init__(self, salt, conc, namelist):
        self.newName = 'SN3' # name of the new forcefield molecule
        self.salt = salt
        self.additionalComponents = namelist  # list of name of additives
        self.boxLengthX = 50  # Angstrom
    def print_info(self):
        print(self.salt)
        print(self.additionalComponents)


if __name__ == '__main__':

    parser=argparse.ArgumentParser()
    parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
    args = parser.parse_args()
    molCode = args._get_kwargs()[0][1][0]
    newName = args._get_kwargs()[0][1][1]
    namelist = args._get_kwargs()[0][1]
    numberList = [400, 20, 20]
    #numberList = calc_conc() # todo: pass parameters

    sys = SimulationSystem(saltMain, concMain, namelist)
    sys.print_info()

    # write packmol input file
    write_pack_inp(numberList, namelist)
