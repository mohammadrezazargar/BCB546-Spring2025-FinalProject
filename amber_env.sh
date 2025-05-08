#!/bin/bash

#SBATCH --time=00:30:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=8   # 8 processor core(s) per node
#SBATCH --mem=64G   # maximum memory per node
#SBATCH --gres=gpu:a100:1
#SBATCH --output="amber.out" # job standard output file (%j replaced by job id)
#SBATCH --error="amber.err" # job standard error file (%j replaced by job id)
#SBATCH --mail-user=[insert email] 
#SBATCH --mail-type=BEGIN,END,FAIL

# v-- change to your directory, double check that the path is correct
cd /work/this/here/gmx_MMPBSA
export MAMBA_ROOT_PREFIX=/work/ratul1/hannah/gmx_MMPBSA/micromamba

module purge
module load micromamba

micromamba env create -n amber_env python=3.11 ambertools=23.3 -c conda-forge -y

eval "$(micromamba shell hook --shell=bash)"
export MAMBA_ROOT_PREFIX=/work/this/here/gmx_MMPBSA/micromamba
micromamba env list
micromamba activate amber_env

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user

micromamba install -c conda-forge "mpi4py=4.0.1" "ambertools<=23.3" -y -q
micromamba install -c conda-forge "numpy=1.26.4" "matplotlib=3.7.3" "scipy=1.14.1" "pandas=1.5.3
" "seaborn=0.11.2" -y -q
python -m pip install "pyqt6==6.7.1"
micromamba install -c conda-forge "gromacs<=2023.4" pocl -y -q

# Check if AmberTools and MCPB.py are available
which MCPB.py
which python

# Check if pymsmt is installed
python -c "import pymsmt" || echo "Error: pymsmt module missing"

micromamba deactivate
