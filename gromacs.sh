#!/bin/bash
#SBATCH -N 1
#SBATCH -p c-16-1
#SBATCH -n 16
#SBATCH -c 1
#SBATCH -e slurmErr-%A_.out.txt
#SBATCH -o output.%A_.txt


cd $SLURM_SUBMIT_DIR

module add GROMACS/2019.6-intel-2019b  
gmx grompp  -f em.mdp  -c box.pdb -p all.top -o em.tpr -maxwarn 37
mpiexec -v gmx_mpi mdrun -v -deffnm em
gmx grompp  -f nvt.mdp  -c em.gro  -p all.top -o nvt.tpr -maxwarn 37
mpiexec -v gmx_mpi mdrun -v -deffnm nvt
#gmx grompp  -f npt_NU.mdp  -c nvt.gro  -p all.top -o npt.tpr -maxwarn 37
#gmx grompp -f npt_NU2.mdp  -c npt.gro -p all.top -o npt2.tpr -maxwarn 37

#mpiexec -v gmx_mpi mdrun -v -deffnm npt2
#gmx grompp -f npt_NU.mdp -c npt2.gro -p all.top -o npt3.tpr -maxwarn 37

#mpiexec -v gmx_mpi mdrun -v -deffnm npt3

#gmx grompp  -f nvt3.mdp  -c npt3.gro  -p all.top -o nvt3.tpr -maxwarn 37

#mpiexec -v gmx_mpi mdrun -v -deffnm nvt3
