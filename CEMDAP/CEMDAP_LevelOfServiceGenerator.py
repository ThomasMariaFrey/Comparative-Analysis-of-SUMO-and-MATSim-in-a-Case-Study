"""
Generating a levelofservice datafile for CEMDAP following the outline from the paper  Demand Generation for Multi-Agent
Transport Simulations based on an Econometric Travel Behavior Model and a Traffic-Count-based Calibration Algorithm
by Dominik Ziemke.

This generator generates the elaborate model.

Taken from the paper:
| Parameter   | Description                          | Initial Model     | Elaborate Model   |
| ----------- | ------------------------------------ | ----------------- | ----------------- |
| Origin      | TSZ zone ID - origin                 | B.3               | cf. B.3           |
| Destination | TSZ zone ID - destination            | cf. B.3           | cf. B.3           |
| samezone    | Orig. and dest. are in same zone     | 1 if yes, 0 if no | 1 if yes, 0 if no |
| Adjacent    | Orig. and dest. are adjacent         | 0                 | 0                 |
| Distance    | Distance between zones               | B.3               | cf. B.3           |
| autoIVTT    | Auto in-vehicle travel time          | 1.2  Distance    | 1.65  Distance   |
| autoOVTT    | Auto out-of-vehicle travel time      | 3.1               | 3.27              |
| Travail     | Public transp. is available          | 0                 | 0                 |
| TrIVTT      | Pub. transp. in-vehicle tr. time     | 0                 | 0                 |
| TrOVTT      | Pub. transp. out-of-vehicle tr. time | 0                 | 0                 |
| TrCost      | Public transp. cost                  | 0                 | 0                 |
| COST        | Auto cost                            | Distance / 15.0   | Distance / 13.8   |
| SRIVTT      | Shared ride travel time              | = autoIVTT        | = autoIVTT        |
| SRCOST      | Shared ride cost                     | = COST            | = COST            |

This is done in accordance to the current population and movement data as stated in
https://www.mannheim.de/de/stadt-gestalten/daten-und-fakten/bevoelkerung

The file has 4 variables where 4 are required and the remaining 0 are not relevant and set to 0.
"""
import math
import geodata


# Calculate the distance of two points
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# Compare strings with 1/0 reutnr
def compare_strings(str1, str2):
    if str1 == str2:
        return "1"
    else:
        return "0"


data = ""
i = 1
e = 0

# Calculating distances
for place1 in geodata.allPlaces:
    for place2 in geodata.allPlaces:
        sameZone = compare_strings(place1['name'], place2['name'])
        distance = haversine_distance(place1['latitude'], place1['longitude'], place2['latitude'], place2['longitude'])

        currentString = place1['name'] + "\t" + place2['name'] + "\t" + sameZone + "\t" + "0" + "\t" + str(
            round(distance, 2)) \
                        + "\t" + str(
            round(1.65 * distance)) + "\t" + "3.27" + "\t" + "0" + "\t" + "0" + "\t" + "0" + "\t" \
                        + "0" + "\t" + str(round(distance / 13.8)) + "\t" + str(round(1.65 * distance)) + "\t" + str(
            round(distance / 13.8)) \
                        + "\n"

        # postgres 9.3 doesnt like 0.0
        currentString = currentString.replace("0.0", "0")

        data = data + currentString

        # debug
        if i > 2 ** e:
            print("Iteration" + str(i))
            print("Current String:")
            print(currentString)
            e = e + 1
        i = i + 1

# Same data for all of these
with open('data/losoffpk.dat', 'w') as file:
    file.write(data)
with open('data/lospeakam.dat', 'w') as file:
    file.write(data)
with open('data/lospeakpm.dat', 'w') as file:
    file.write(data)

print("Text data has been written to losoffpk.dat, lospeakam.dat and lospeakpm.dat. It contains " + str(i) + "lines.")
