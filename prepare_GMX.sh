#!/bin/bash

molCode="UNK_C4C273"
newName="SN3"

python CutForcefield.py $molCode
python RenameResidue.py -l $molCode $newName
python WriteInp.py ${newName}
mv ${molCode}.pdb ${newName}.pdb
mv ${molCode}.itp ${newName}.itp
mv ffnonbonded.itp oplsaa-modif.ff/

packmol < pack_test.inp
