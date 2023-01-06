#!/usr/bin/env python
import argparse

genCode = 'UNK_C4C273'
newName = 'SiN3'
parser=argparse.ArgumentParser()
parser.add_argument('fn',type=str)
args = parser.parse_args()
molCode = args.fn
tail = '.itp'

with open(molCode + tail, 'r') as fp:
    filedata = fp.read()

filedata = filedata.replace('UNK', newName)

with open(molCode + '.pdb', 'w') as fp:
    fp.write(filedata)

with open(molCode + tail, 'r') as fp:
    filedata = fp.read()

filedata = filedata.replace('UNK', newName)

with open(molCode + '.pdb', 'w') as fp:
    fp.write(filedata)
