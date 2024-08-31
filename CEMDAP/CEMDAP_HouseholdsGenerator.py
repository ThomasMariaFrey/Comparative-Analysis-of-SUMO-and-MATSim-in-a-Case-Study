"""
Generating a household datafile for CEMDAP following the outline from the paper  Demand Generation for Multi-Agent
Transport Simulations based on an Econometric Travel Behavior Model and a Traffic-Count-based Calibration Algorithm
by Dominik Ziemke.

This generator generates the elaborate model.

Taken from the paper:
| Parameter | Description                   | Initial Model      | Elaborate Model    |
| --------- | ----------------------------- | ------------------ | ------------------ |
| HHID      | Household ID ascending from 1 | ascending from 1   | ascending from 1   |
| NADULT    | Number of adults              | 1                  | 1                  |
| NVEH      | Total number of hh. veh.      | 1                  | 1                  |
| HOMETSZ   | Home TSZ location             | randomly selected* | randomly selected* |
| NCHILD    | Number of children            | 0                  | 0                  |
| HHSTRUCT  | Household structure           | 1                  | 1                  |
| ...       | 26 remaining variables        | 0                  | 0                  |

This is done in accordance to the current population and movement data as stated in
https://www.mannheim.de/de/stadt-gestalten/daten-und-fakten/bevoelkerung

The file has 32 variables where 6 are required and the remaining 26 are not relevant and set to 0.
"""

import geodata
import random

data = ""

i = 1
e = 0

nonRelevantVariables = "\t0" * 26

# Handling the commuting population
while i <= geodata.totalAdultPopulation:

    weights = [place['percentageOfTotal'] for place in geodata.places]
    trafficSurveyZone = random.choices(geodata.places, weights=weights, k=1)[0]['name']

    currentString = str(i) + "\t" + "1" + "\t" + "1" + "\t" \
                    + trafficSurveyZone \
                    + "\t" + "0" + "\t" + "1" \
                    + nonRelevantVariables + "\n"

    data = data + currentString

    #Debug information
    if i > 2 ** e:
        print("Iteration" + str(i))
        print("Current String:")
        print(currentString)
        e = e + 1

    i = i + 1

#Handling the rest of the population
while i - geodata.totalAdultPopulation <= geodata.commutingIn:

    weights = [place['percentageOfTotal'] for place in geodata.commuterPlaces]
    trafficSurveyZone = random.choices(geodata.commuterPlaces, weights=weights, k=1)[0]['name']

    currentString = str(i) + "\t" + "1" + "\t" + "1" + "\t" \
                    + trafficSurveyZone \
                    + "\t" + "0" + "\t" + "1" \
                    + nonRelevantVariables + "\n"

    data = data + currentString

    # Debug information
    if i > 2 ** e:
        print("Iteration" + str(i))
        print("Current String:")
        print(currentString)
        e = e + 1

    i = i + 1

with open('data/households.dat', 'w') as file:
    file.write(data)

print("Text data has been written to households.dat. It contains " + str(i) + "lines.")
