#!/usr/bin/env python
import argparse

gen_code = 'UNK_C4C273'
parser=argparse.ArgumentParser()
parser.add_argument('fn',type=str)
args = parser.parse_args()
mol_code = args.fn
tail = '.itp'
fp = open(mol_code + tail, 'r')

stored = []
sectionMark = False
def read_file_from():
    with open(mol_code + tail, 'r') as fp:
        for line_idx, line in enumerate(fp):
            if not line.strip(): # if meet empty lines
                continue

            linelist = list(line)
            if linelist[0] == ';':  # skip comment lines
                continue
            #  locate atomtypes
            #print(linelist[0:10])

            if linelist[0:13] == list('[ atomtypes ]'):
                print('found atomtypes')
                sectionMark = True
            if linelist[0:5] == list('[ mol'):
                sectionMark = False
                stored.append(line)
                print('section ended')
            if sectionMark:
                stored.append(line)

    #print(stored)


finalStoredList = []
notWrittenFlag = True
def read_file_2():
    notWrittenFlag = True
    with open('./oplsaa-modif.ff/ffnonbonded.itp', 'r') as fp2:
        for line_idx, line in enumerate(fp2):
            # the file starts with [ atomtypes]
            linelist = list(line)
            if linelist[0:13] == list('[ atomtypes ]'):
                continue
            finalStoredList.append(line)
            linelist = list(line)
            if line.strip() and notWrittenFlag == True:  # skip comment lines
                for line in stored:  # line is a string
                    finalStoredList.append(line)
                notWrittenFlag = False
read_file_from()
read_file_2()


with open('./ffnonbonded.itp', 'w') as fw:
    for line in finalStoredList:
        fw.write(line)

#fp2 = open('./oplsaa-modif.ff/ffnonbonded.itp')
#fw = open('ffnonbonded.itp', 'w')

#fp2.close()
#fw.close()
