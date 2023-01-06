#!/bin/bash

molCode="UNK_C4C273"
newName="SN3"

python CutForcefield.py $molCode
python RenameResidue.py $molCode $newName
python WriteInp.py ${newName}
mv ${molCode}.pdb ${newName}.pdb
mv ${molCode}.itp ${newName}.itp

packmol < pack_test.inp
