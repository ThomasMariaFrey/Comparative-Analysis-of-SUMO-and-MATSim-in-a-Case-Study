"""
Generating a zone2zone datafile for CEMDAP following the outline from the paper  Demand Generation for Multi-Agent
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

The file has 4 variables where 4 are required and the remaining 0 are not relevant and set to 0.
"""
import math
import geodata


# Distance in meters between two coordinate points
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance


data = ""
i = 1
e = 0

# Generate zone values
for place1 in geodata.allPlaces:
    for place2 in geodata.allPlaces:
        currentString = place1['name'] + "\t" + place2['name'] + "\t" + "0" + "\t" \
                        + str(
            haversine_distance(place1['latitude'], place1['longitude'], place2['latitude'], place2['longitude'])) \
                        + "\n"

        data = data + currentString

        # debug
        if i > 2 ** e:
            print("Iteration" + str(i))
            print("Current String:")
            print(currentString)
            e = e + 1
        i = i + 1

# Open a file in write mode
with open('data/zone2zone.dat', 'w') as file:
    file.write(data)

print("Text data has been written to zone2zone.dat. It contains " + str(i) + "lines.")
