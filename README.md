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
Please make sure to note the comments in the scripts explaining the way they work.

## Structure
1. [CEMDAP](#1-cemdap)
2. [CaDyTS](#2-cadyts)
3. [MATSim](#3-matsim)
4. [Results](#4-results)

## 1. CEMDAP  
CEMDAP is used to create the *population.xml* file which is used as a central input for the MATSim scenario.  
The software tool can be downloaded here: [CEMDAP Download](https://www.caee.utexas.edu/prof/bhat/cemdap.htm).  
How the input data, that is being created by the following scripts, can be imported into CEMDAP and how the activity plans are generated is described in detail in the CEMDAP user manual. This manual is found in the download link.  

The directory *CEMDAP* contains all files necessary for the creation of the input data. The five creation files, noted by the CEMDAP_ at the beginning of the filename, are used to create output files in the *data* directory. The output files correspond in name to the creation files, except for *CEMDAP_LevelOfServiceGenerator.py* which generates the output files *losoffpk.dat*, *lospeakam.dat* and *lospeakpm.dat*. Data sources are provided in the geodata.py file. 

The output of CEMDAP can not immediately be used as an population.xml file for MATSim.
For this, the software tool [CEMDAP2MATsim](https://github.com/fzenoni/matsim/tree/f4958b063b76ddef2f2fc4b5fa68e1ed8346bf84/playgrounds/dziemke/src/main/java/playground/dziemke/cemdapMatsimCadyts/cemdap2matsim) has to be used.

## 2. CaDyTS  
CaDyTS is used to create the *counts.xml* file that can calibrate the MATSim scenario.
How this works is described here: [CaDyTS in MATSim](https://github.com/matsim-org/matsim-libs/blob/master/contribs/cadytsIntegration/README.md).

The directory *CaDyTS* contains one file that is used to transform the induction loop data into a format that can be transferred into the _counts.xml_ file.
All data sources for the 16.05.2023 are present in the _CaDyTS_Transformer.py_ file.

## 3. MATSim  

Note: The network file of this scenario was created with [JOSM](https://josm.openstreetmap.de/) and [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis#Downloading). To include public transport 
https://github.com/matsim-org/pt2matsim/tree/master

## 4. Results  
The _Results_ directory contains scripts that I used to extract information and generate graphs for the presentation in my thesis. 
Many files have not been included as they contain references to individual movement data. 
Therefore only scripts that consider MATSim, not SUMO or the Survey are included.
These files are not relevant for the generation of the MATSim scenario.


