#!/bin/bash
#SBATCH -N 1
#SBATCH -p c-8-1
#SBATCH -n 8
#SBATCH -c 1
#SBATCH -e slurmErr-%A_.out.txt
#SBATCH -o output.%A_.txt


cd $SLURM_SUBMIT_DIR

module add GROMACS/2019.6-intel-2019b
#gmx grompp  -f mdps/em.mdp  -c box.pdb -p all.top -o em.tpr -maxwarn 57
#mpiexec -v gmx_mpi mdrun -v -deffnm em
gmx grompp  -f mdps_Tao/nvt.mdp  -c em.gro  -p all.top -o nvt.tpr -maxwarn 57
mpiexec -v gmx_mpi mdrun -v -deffnm nvt
gmx grompp  -f mdps_Tao/npt.mdp  -c nvt.gro  -p all.top -o npt.tpr -maxwarn 57
mpiexec -v gmx_mpi mdrun -v -deffnm npt

# production run
gmx grompp  -f mdps_Tao/run.mdp  -c npt.gro  -p all.top -o run.tpr -maxwarn 57
mpiexec -v gmx_mpi mdrun -v -deffnm run
