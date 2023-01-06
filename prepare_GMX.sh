#!/bin/bash

molCode="UNK_C4C273"
newName="SiN3"

python CutForcefield.py $molCode
python RenameResidue.py $molCode
python WriteInp.py ${newName}.pdb
mv ${molCode}.pdb ${newName}.pdb
mv ${molCode}.itp ${newName}.itp
