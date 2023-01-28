#!/usr/bin/env python
import sys
import argparse
import math
import numpy as np
from WriteInp import write_pack_inp
from WriteAllTop import write_all_top
from CalculateConcentration import calc_conc

# define cross-functional constants
#molNumber = calc_conc()


class SimulationSystem(object):
    def __init__(self, salt, conc, namelist):
        self.newName = 'SN3' # name of the new forcefield molecule
        self.salt = salt
        self.additionalComponents = namelist  # list of name of additives
        self.boxLengthX = 55  # Angstrom

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
    #numberList = [400, 20, 20]
    numberList = calc_conc() # todo: pass parameters
    write_pack_inp(numberList, namelist)
    write_all_top(numberList)
    print(numberList)

    #sys = SimulationSystem(saltMain, concMain, namelist)
    #sys.print_info()

    # write packmol input file
    write_pack_inp(numberList, namelist)
