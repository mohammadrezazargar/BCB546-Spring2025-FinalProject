# BCB 546 Final Project

This project is based on the study performed by __[Misra, Manas, and Anil Kumar Yadav. "Assessment of available AMBER force fields to model DNA-ligand interactions." Biointerface Res. Appl. Chem 13 (2022): 156.](https://biointerfaceresearch.com/wp-content/uploads/2022/03/BRIAC132.156.pdf)__

We provide a comprehensive methodolgy for performing Molecular Dynamics (MD) simulations utilizing various different Amber embedded forecfields that are in the GROMACS software for a DNA-small moelcule system. Although this project is built to be executed using HPC, it can easily be adapted to your local machine.

### **Necessary Software/ Packages**:
+ AmberTools
+ AutDock + AutoDock Vina
+ Any software to perform geometry optimization
+ GROMACS

### **Amber Environment**:
For HPC, we provide a batch script that builds a AmberTools environment using micromamba to allow for additional packages to be installed. This script is called *"amber_env.sh"*

### **Ligand Data**:
The starting ligand structure (.pdb, .mol, & .txt format) and the final docked pose can be found in *"complex_info"*.

### **DFT Data**:
DFT Calculations were performed on a carbazole derivative both in vaccuum and in water. 
+ This data can be found in *"ligand_water"* and *"ligand_vac"*.
+ These directories contain the functional and basis set utilized for this project as well as a batch script to run the job.

### **Docking Information**:
The docking results can be found in *"docking_files"*.
+ This directory contains the docking scores from AutoDock4 and the parameters used to dock the ligand to DNA
+ Contains the final docked complex in .pdbqt format

### **MD Simulations**:
Due to space limitations in github, ***all*** MD related data is located in a external google drive where can be downloaded via .zip file.
*Data Availability*: Molecular Dynamics Simulations __[Full Dataset](https://drive.google.com/drive/folders/1CRN-luRf_2fc7RL20XiKStWz-GhJgUZv?usp=sharing)__.
Each directory includes all the MD information for each forcefield tested where each forcefield folder is labeled to their respective forcefield. Each folder within this directory contains >>>
+ Batch Scripts for ...
    - Paramterization of ligand and DNA > ff_param.sh
    - MD set up and production run > full_jobscript.sh
    - MD analysis > sys_analysis.sh
+ Output MD System Information with updated coordinates and trajectories
+ Final analysis of MD: RMSD, RMSF, Radius of Gyration, and Hydrogen Bonding in .xvg format

### **System Analysis**:
Graphing the .xvg data was performed using Python and R. The raw data in .xvg format can be found in *"data_analysis"*. Additionally, within this directory there is ...
+ "codes" File: This folder contains all codes utilized to produce the necessay plots
+ "plots" File: This folder contains all the plots in .png format


