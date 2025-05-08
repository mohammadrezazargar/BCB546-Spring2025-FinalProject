#!/bin/bash
#SBATCH --job-name=g16_bcb
#SBATCH --time=168:00:00  # Adjust the wall time limit as necessary
#SBATCH -N 1
#SBATCH --ntasks=1        # Number of tasks
#SBATCH --mem=64GB        # Memory request
#SBATCH --mail-user=hgates@iastate.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

# Load Gaussian16 module
module purge
module load gaussian/16-C.01-3yzt2xl
export OMP_NUM_THREADS=1

# Geometry Optimization for the Carbazole
echo "Running geometry optimization for the carbazole model..."
g16 < carbazole_compound.txt > carbazole_compound.log

# Check if the optimization was successful
if [ $? -ne 0 ]; then
    echo "Geometry optimization failed for small model, exiting."
    exit 1
fi


# Convert the checkpoint file to fchk format for the carbazole model
echo "Converting checkpoint file to fchk format for the small model..."
formchk carbazole_compound.chk carbazole_compound.fchk

# Check if the formchk conversion was successful
if [ $? -ne 0 ]; then
    echo "Formchk conversion failed, exiting."
    exit 1
fi

echo "All Gaussian16 calculations completed successfully."

