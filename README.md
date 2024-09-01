# Comparative-Analysis-of-SUMO-and-MATSim-in-a-Case-Study
This repository was submitted on the 02.09.2024 together with the master thesis "Comparative Analysis of SUMO and MATSim in a Case Study".  
Author: Thomas Maria Frey

## Description
The files in this repository allow for the complete recreation of the MATSim scenario as outlined in the methodology section of the thesis.
The repository is split up into four parts as outlined in the structure below.
CEMDAP contains scripts that are used to create the input data for the CEMDAP software.
CaDyTS contains scripts that are used to create the input data for the CADYTS extension of MATSIM.
MATSim contains the input data relevant to the creation of the scenario for the city of Mannheim.
Results contain the scripts that are used to extract output data.  
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

The directory *CEMDAP* contains all files necessary for the creation of the input data. The five creation files, noted by the CEMDAP_ at the beginning of the filename, are used to create output files in the *data* directory. The output files correspond in name to the creation files, except for *CEMDAP_LevelOfServiceGenerator.py* which generates the output files *losoffpk.dat*, *lospeakam.dat*, and *lospeakpm.dat*. Data sources are provided in the geodata.py file. 

The output of CEMDAP can not immediately be used as a population.xml file for MATSim.
For this, the software tool [CEMDAP2MATsim](https://github.com/fzenoni/matsim/tree/f4958b063b76ddef2f2fc4b5fa68e1ed8346bf84/playgrounds/dziemke/src/main/java/playground/dziemke/cemdapMatsimCadyts/cemdap2matsim) has to be used.

## 2. CaDyTS  
CaDyTS is used to create the *counts.xml* file that can calibrate the MATSim scenario.
How this works is described here: [CaDyTS in MATSim](https://github.com/matsim-org/matsim-libs/blob/master/contribs/cadytsIntegration/README.md).

The directory *CaDyTS* contains one file that is used to transform the induction loop data into a format that can be transferred into the _counts.xml_ file.
All data sources for the 16.05.2023 are present in the _CaDyTS_Transformer.py_ file.

## 3. MATSim  
The MATSim framework is used to run the created simulation.
To run the simulation you must setup the framework yourself and import the provided data sources.
In the following paragraph, I will explain one tested way how this can be done.

Go to the [MATSim Org](https://github.com/matsim-org) and import the [matsim-libs](https://github.com/matsim-org/matsim-libs) repository into IntelliJ IDEA.
Set up the MATSim Framework as outlined on the MATSim Org page.
Copy the files from this repository, placed in the _MATSim/matsim-libs_ directory, into the imported MATSim project. 
Make sure to follow the directory structure that is present in this repository for the placement of the files.
You will now be able to run the Mannheim scenario by running either _Mannheim10.java_ or _Mannheim100.java_.

_Mannheim10.java_ runs the scenario with a 10% sample of the population. This means that all parameters for the network, such as road capacity and all parameters for the counts are also scaled down to 10%.
_Mannheim100.java_ runs the full scenario.

Important: The network.xml and the full-size population.xml files are too large to be uploaded to this repository. 
You can find these files either in this [drive link](https://drive.google.com/drive/folders/1TnH8Uwsgix9OJhB_5pLKDX3D8Q1G59kZ?usp=sharing) or in the USB stick that was submitted on the 05.09.2024. 
To run the scenario place the network.xml and population.xml files at the location where the network.txt and population.txt files are placed currently.

Note: The network file of this scenario was created with [JOSM](https://josm.openstreetmap.de/) and [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis#Downloading). 
To include public transport [PT2MATSim](https://github.com/matsim-org/pt2matsim/tree/master) was used.

The BEAM scenario is used to explore the reinforcement learning capacities of MATSim.
To run the simulation you must also setup the framework yourself and import the provided data sources.
Import and set up the framework from the [Beam Repository](https://github.com/LBNL-UCB-STI/beam).
Follow the tutorial present on the webpage to do this.
Copy the files from this repository, placed in the _MATSim/beam/_ directory, into the imported BEAM project.
Also, make sure that the directory structure that is present is followed for the placement.
A conversion of the Mannheim scenario is not necessary, as this has already been done.
The Mannheim scenario can now be run like one of the other scenarios.

## 4. Results  
The _Results_ directory contains scripts that I used to extract information and generate graphs for the presentation in my thesis. 
Many files have not been included as they contain references to individual movement data. 
Therefore only scripts that consider MATSim and BEAM, not MATSim in combination with SUMO and the Survey are included.
These files are not relevant for the generation of the MATSim scenario.


