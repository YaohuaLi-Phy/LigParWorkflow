#!/usr/bin/env python
# function: write the top file for the simulation system
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()
namelist = args._get_kwargs()[0][1]

def write_all_top():
    # parameters
    molNumber = [400, 20, 20]  # write as class

    with open('all.top', 'w') as fp:
        fp.write('#include "./oplsaa-modif.ff/forcefield.itp"\n')
        fp.write('#include "./atp.itp"\n')

        for name in namelist:
            fp.write('#include "./' + str(name) + '.itp' + '"\n')

        fp.write('\n[ system ]\n')
        fp.write('; Name \n')
        fp.write('Box1\n\n')
        fp.write('[ molecules ]\n')
        for idx, name in enumerate(namelist):
            fp.write(str(name)+'\t' + str(molNumber[idx]) + '\n')


write_all_top()
