#!/usr/bin/env python
# command line input:  a list of Names of the molecules in the box
import argparse

def write_pack_inp(molNumber, namelist):
    # parameters: molNumber: list of number of each molecule in "namelist"
    tolerance = 2.0
    boxSideMargin = 1.1  # Angstrom
    molNumber = molNumber
    boxLengthX = 50
    print("open file")
    print(str(namelist))
    with open('pack_test.inp', 'w') as fp:
        fp.write('tolerance ' + str(tolerance) + '\n')
        fp.write('filetype pdb\n')
        fp.write('output box.pdb\n')
        fp.write('add_box_sides ' + str(boxSideMargin) + '\n\n')

        for idx, name in enumerate(namelist):
            fp.write('structure ' + str(name) + '.pdb\n')
            fp.write('\t number ' + str(molNumber[idx]) + '\n')
            fp.write('\t inside box 0. 0. 0. ' + (str(boxLengthX)+' ')*3 + '\n')
            fp.write('end structure\n')


# main
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
    args = parser.parse_args()
    namelist = args._get_kwargs()[0][1]
    #molNumber = calc_conc()
    molNumber = [279, 60, 75, 15]
    print(namelist)

    write_pack_inp(molNumber, namelist)
