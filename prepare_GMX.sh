#!/bin/bash

molCode="UNK_C4C273"
newName="CN3"
name2="li"
name3="pf6-"


#python CutForcefield.py $molCode
#python RenameResidue.py -l $molCode $newName

#python main.py -l $newName $name2 $name3
 # change to main.py
python WriteInp.py -l ${newName} $name2 $name3
python WriteAllTop.py -l ${newName} $name2 $name3
mv ${molCode}.pdb ${newName}.pdb
mv ${molCode}.itp ${newName}.itp
mv ffnonbonded.itp oplsaa-modif.ff/

packmol < pack_test.inp
