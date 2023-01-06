#!/usr/bin/env python
import argparse
# rename the residue name in PDB from UNK to the desired new name

genCode = 'UNK_C4C273'
newName = 'SN3'  # 3 letter-number combination recommended
parser=argparse.ArgumentParser()
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()

molCode = args._get_kwargs()[0][1][0]
newName = args._get_kwargs()[0][1][1]
print(molCode)
print(newName)
tail = '.itp'
tail2 = '.pdb'

with open(molCode + tail, 'r') as fp:
    filedata = fp.read()

filedata = filedata.replace('UNK', newName)

with open(molCode + tail, 'w') as fp:
    fp.write(filedata)


# ==============================================
with open(molCode + tail2, 'r') as fp:
    filedata = fp.read()

filedata = filedata.replace('UNK', newName)

with open(molCode + tail2, 'w') as fp:
    fp.write(filedata)
