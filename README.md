# Comparative-Analysis-of-SUMO-and-MATSim-in-a-Case-Study
This repository was submitted on the 02.09.2024 together with the master thesis "Comparative Analysis of SUMO and MATSim in a Case Study".  
Author: Thomas Maria Frey

## Description
The files in this repository allow for the complete recreation of the MATSim scenario as outlined in the methodology section of the thesis.
The repository is split up into four part as outlined in the structure below.
CEMDAP contains scripts that are used to create the input data for the CEMDAP software.
CaDyTS contains scripts that are used to create the input data for the CADYTS extension of MATSIM.
MATSim contains the input data relevant for the creation of the scenario for the city of Mannheim.
Results contains the scripts that are used to extract output data.  

## Structure
1. [CEMDAP](#cemdap)
2. [CaDyTS](#cadyts)
3. [MATSim](#matsim)
4. [Results](#results)

## 1. CEMDAP  
CEMDAP is used to create the *population.xml* file which is used as the input for the MATSim scenario.  
The software tool can be downloaded here: [CEMDAP Download](https://www.caee.utexas.edu/prof/bhat/cemdap.htm).  
How the input data, that is being created by the following scripts, can be imported in to CEMDAP is described in detail in the CEMDAP user manual. This manual is found in the download link.  

The directory *CEMDAP* contains all files necessary for the creation of the input data. The five creation files, noted by the CEMDAP_ at the beginning of the filename, are used to create output files in the *data* directory. The output files correspond in name to the creation files, except for *CEMDAP_LevelOfServiceGenerator.py* which generates the output files *losoffpk.dat*, *lospeakam.dat* and *lospeakpm.dat*. Additional data is provided in the geodata.py file. 

## 2. CaDyTS  

## 3. MATSim  

## 4. Results  
