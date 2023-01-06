#!/usr/bin/env python
# command line input: newName of the molecule
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('fn',type=str)
args = parser.parse_args()
newName = args.fn
print(newName)
def write_pack_inp():
    # parameters
    tolerance = 2.0
    boxSideMargin = 1.1  # Angstrom
    molNumber = 400
    boxLengthX = 60

    with open('pack_test.inp', 'w') as fp:
        fp.write('tolerance ' + str(tolerance) + '\n')
        fp.write('filetype pdb\n')
        fp.write('output box.pdb\n')
        fp.write('add_box_sides' + str(boxSideMargin) + '\n\n')
        fp.write('structure ' + str(newName) + '.pdb\n')
        fp.write('\t number ' + str(molNumber) + '\n')
        fp.write('\t inside box 0. 0. 0.' + (str(boxLengthX)+'')*3 + '\n')
        fp.write('end structure\n')

# main
write_pack_inp()
