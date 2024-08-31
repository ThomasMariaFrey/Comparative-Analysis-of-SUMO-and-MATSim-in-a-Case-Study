"""
Generating a zones datafile for CEMDAP following the outline from the paper  Demand Generation for Multi-Agent
Transport Simulations based on an Econometric Travel Behavior Model and a Traffic-Count-based Calibration Algorithm
by Dominik Ziemke.

This generator generates the elaborate model.

Taken from the paper:
| Parameter   | Description                  | Initial Model          | Elaborate Model        |
| ----------- | ---------------------------- | ---------------------- | ---------------------- |
| Origin zone | TSZ zone ID - origin         | municip. or LOR ID*    | municip. or LOR ID*    |
| Dest zone   | TSZ zone ID - destination    | municip. or LOR ID*    | municip. or LOR ID*    |
| Adjacent    | Orig. and dest. are adjacent | 0                      | 0                      |
| Distance    | Distance between zones       | Centroid beeline dist. | Centroid beeline dist. |

This is done in accordance to the current population and movement data as stated in
https://www.mannheim.de/de/stadt-gestalten/daten-und-fakten/bevoelkerung

The file has 45 variables where 1 is required and the remaining 44 are not relevant and set to 0.
"""

import geodata

data = ""

i = 0
e = 0

nonRelevantVariables = "\t0" * 44

#Assign Zone values
for place in geodata.allPlaces:

    currentString = place['name'] + nonRelevantVariables + "\n"

    data = data + currentString

    if (i+1 >= 2**e):
        print("Iteration " + str(i))
        print("Current String:")
        print(currentString)
        e = e + 1

    i = i + 1

# Open a file in write mode
with open('data/zones.dat', 'w') as file:
    file.write(data)

print("Text data has been written to zones.dat. It contains " + str(i) + "lines.")