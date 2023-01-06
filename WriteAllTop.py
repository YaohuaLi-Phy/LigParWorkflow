#!/usr/bin/env python
# function: write the top file for the simulation system
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('fn',type=str)
args = parser.parse_args()
newName = args.fn

def write_all_top():
    # parameters
    molNumber = 400

    with open('all.top', 'w') as fp:
        fp.write('#include "./oplsaa-modif.ff/forcefield.itp"\n')
        fp.write('#include "./' + str(newName) + '.itp' + '"\n\n')
        fp.write('[ system ]\n')
        fp.write('; Name \n')
        fp.write('Box1\n\n')
        fp.write('[ molecules ]\n')
        fp.write(str(newName)+'\t' + str(molNumber) + '\n')

write_all_top()
