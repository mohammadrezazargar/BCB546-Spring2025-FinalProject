# Original study
The objective is to assess seven available AMBER force fields (namely AMBER03 , AMBER94, AMBER96 , AMBER99, AMBER99SB, AMBER99SB-ILDN , and AMBERGS) integrated within the GROMACS software, used to model the interactions between DNA and a minor groove binding ligand to aid drug design strategies.
Here are the steps involved.
* Obtaining the structures for DNA and ligand (from RCSB PDB)
* Molecular geometry optimization of the ligand using DFT and Gaussian
* Molecular docking to predict the DNA-ligand binding groove (AutoDock)
* Molecular dynamics (MD) simulation to study the stability  and trajectories of the complex for each force field
  1. The protein-ligand box is solvated and charge-neutralized
  2. Energy minimisation of the structure
  3. NVT and NPT equilibration
  4. 100ns MD simulation
* Analysis of the trajectories (Results)
1. Radius of Gyration
2. Root mean square deviation
3. Root mean square fluctuation
4. Hydrogen bonds


# Replication of Analysis
Since the original study did not include any documentation on the box dimensions, the version of the software used or the UNIX commands used to run the simulation, we followed the standard protocol used in protein-ligand simulation. /n
* Obtained DNA structure from [RCSB PDB](https://www.rcsb.org/structure/195D)  server for the PDB ID 195D, cleaned to remove water molecules with PyMOL software.
* The ligand structure was loaded to [WebMO](https://www.webmo.net/) to export to .pdb format and converted to Gaussian16 readable PDB format using [OpenBabel](https://openbabel.org/)
* The ligand geometry is optimised with Gaussian 16 using the SCRF (Self consistent reaction field) and PCM (Polarizable Continuum Model) with B3LYP functional and 6-31G Basis set
* The optimized structures are docked using AutoDock Vina 1.1.2 with a box dimensions of 40 x 40 x 40 A
* The ligand parameters are obtained using  ANTECHAMBER, parmchk2, and the Amber Tools embedded code acpype.py (Batch script provided)
* The parameterised DNA and ligand coodinated are combined to a single complex file, which is then solvated and neutralized.
* Energy minimization is carried out for 50000 steps, followed by NVT and NPT equilibration (100 ps each) at 300 K
* A production molecular dynamics run was executed for 100 nanoseconds

# Replication of Results
A batch script is made with GROMACS UNIX commands to extract .xvg files for Radius of Gyration, RMSD, RMSF and hydrogen bonds for each force field.\n
We wrote python scripts to plot radius of gyration, RMSD and RMSF for different forcefields with the matplotlib package.
An R markdown file is provided for obtaining the Hydrogen bonds trend using ggplot ppackage.

