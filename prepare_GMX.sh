#!/bin/bash

molCode="UNK_D556B1"
newName="CH5"

python CutForcefield.py $molCode
python RenameResidue.py -l $molCode $newName
python WriteInp.py ${newName}
python WriteAllTop.py ${newName}
mv ${molCode}.pdb ${newName}.pdb
mv ${molCode}.itp ${newName}.itp
mv ffnonbonded.itp oplsaa-modif.ff/

packmol < pack_test.inp
