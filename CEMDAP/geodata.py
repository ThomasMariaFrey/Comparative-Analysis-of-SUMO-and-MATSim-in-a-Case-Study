"""
| Nr. | Stadtbezirk/Stadtteil | Wohnberechtigte Bevolkerung | Unter 18 Jahre | Adult Population / Centerpoint / osm_id /
| --- | --------------------------------- | --------------------------- | -------------- | ---------------- / ------------/------------ /
| 01 | Innenstadt/Jungbusch | 31.881 | 3.289 | 28.592 / (49.488888, 8.467222) / 3286563 /
| 02 | Neckarstadt-West | 20.160 | 3.196 | 16.964 / (49.502778, 8.470833) / 3286567 /
| 03 | Neckarstadt-Ost | 35.125 | 5.223 | 29.902 / (49.497222, 8.479167) / 3286566 /
| 04 | Schwetzingerstadt/Oststadt | 23.867 | 2.534 | 21.333 / (49.482778, 8.490833) / 3286571 /
| 05 | Lindenhof | 13.935 | 1.661 | 12.274 / (49.473611, 8.459444) / 3286564 /
| 06 | Sandhofen | 14.175 | 2.202 | 11.973 / (49.554167, 8.448333) / 3286570 /
| 07 | Schonau | 12.630 | 2.403 | 10.227 / (49.526944, 8.413889) / 2801254 /
| 08 | Waldhof | 25.544 | 4.696 | 20.848 / (49.528333, 8.448056) / 2801091 /
| 09 | Neuostheim/Neuhermsheim | 7.390 | 1.204 | 6.186 / (49.476944, 8.535833) / 3286568 /
| 10 | Seckenheim | 16.087 | 2.907 | 13.180 / (49.469444, 8.555833) / 3286572 /
| 11 | Friedrichsfeld | 5.612 | 841 | 4.771 / (49.440833, 8.575000) / 3286562 /
| 12 | Kafertal | 33.495 | 6.418 | 27.077 / (49.523056, 8.521944) / 2796949 /
| 13 | Vogelstang | 12.495 | 2.198 | 10.297 / (49.511111, 8.529167) / 2796746 /
| 14 | Wallstadt | 7.850 | 1.170 | 6.680 / (49.513611, 8.554444) / 270096 /
| 15 | Feudenheim | 14.218 | 2.220 | 11.998 / (49.487500, 8.539167) / 2800523 /
| 16 | Neckarau | 31.053 | 4.284 | 26.769 / (49.454722, 8.490278) / 3286565 /
| 17 | Rheinau | 25.379 | 4.076 | 21.303 / (49.426111, 8.499444) / 3286569/
| | Gesamt Mannheim | 330.896 | 50.522 | 280.374 /


nr. | Stadt | einpendelnde | auspendelnde | centerpoint / osm_id /
18 | Burstadt, Hessen | (33%) | (33%)  | (49.6425,8.4589)/ 537049 /
19 | Ludwigshafen am Rhein | (33%)  | (33%)  | (49.47765, 8.43279)/ 62347 /
20 | Heidelberg | (33%) | (33%)  | (49.39880, 8.67240)/ 285864 /

| Region Code  | Region Name                 | Auspendelnde | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Inland | Auspendelnde in das Ausland |     |
|              |                             | Insgesamt    | Insgesamt                  | Insgesamt                  | Insgesamt                  | Insgesamt                  | mannlich                   | mannlich                   | mannlich                   | mannlich                   | mannlich                   | weiblich                   | weiblich                   | weiblich                   | weiblich                   | weiblich                   |                             |     |
|              |                             | Insgesamt    | unter 25 Jahre             | 25 bis unter 45 Jahre      | 45 bis unter 67 Jahre      | 67 Jahre und mehr          | Insgesamt                  | unter 25 Jahre             | 25 bis unter 45 Jahre      | 45 bis unter 67 Jahre      | 67 Jahre und mehr          | Insgesamt                  | unter 25 Jahre             | 25 bis unter 45 Jahre      | 45 bis unter 67 Jahre      | 67 Jahre und mehr          |                             |     |
| 082220000000 | Mannheim, Universitatsstadt | 68485        | 68475                      | x                          | 34960                      | 24318                      | x                          | 40196                      | x                          | 20299                      | 14774                      | x                          | 28279                      | x                          | 14661                      | 9544                       | x                           | 10  |

| Region Code  | Region Name                 | Einpendelnde | Einpendelnde | Einpendelnde | Einpendelnde | Einpendelnde | mannlich  | mannlich       | mannlich              | mannlich              | mannlich          | weiblich  | weiblich       | weiblich              | weiblich              | weiblich          |
|              |                             | Insgesamt    | Insgesamt    | Insgesamt    | Insgesamt    | Insgesamt    | Insgesamt | unter 25 Jahre | 25 bis unter 45 Jahre | 45 bis unter 67 Jahre | 67 Jahre und mehr | Insgesamt | unter 25 Jahre | 25 bis unter 45 Jahre | 45 bis unter 67 Jahre | 67 Jahre und mehr |
| 082220000000 | Mannheim, Universitatsstadt | 137334       | x            | 60835        | 61287        | x            | 81064     | x              | 35402                 | 36988                 | x                 | 56270     | x              | 25433                 | 24299                 | x                 |
"""

print("Initializing Geodata")

totalAdultPopulation = 0
commutingOut = 68485
commutingIn = 137334
commutingAreas = 3

# Name is the osm_id of the district of the dbf file of the shapefile of the administrative boundary of Mannheim
# Population of people commuting in (Einpendelnde) is placed the 3 Administraive areas of Heidelberg, Ludwigshafen am Rhein
# Burstadt
places = [
    {"name": "3286563", "latitude": 49.489100, "longitude": 8.466940, "adultPopulation": 28592},
    # osm_id of Innenstadt / Jungbusch
    {"name": "3286567", "latitude": 49.502778, "longitude": 8.470833, "adultPopulation": 16964},
    # osm_id of Neckarstadt-West
    {"name": "3286566", "latitude": 49.497222, "longitude": 8.479167, "adultPopulation": 29902},
    # osm_id of Neckarstadt-Ost
    {"name": "3286571", "latitude": 49.482778, "longitude": 8.490833, "adultPopulation": 21333},
    # osm_id of Schwetzingerstadt/Oststadt
    {"name": "3286564", "latitude": 49.473611, "longitude": 8.459444, "adultPopulation": 12274},  # osm_id of Lindenhof
    {"name": "3286570", "latitude": 49.554167, "longitude": 8.448333, "adultPopulation": 11973},  # osm_id of Sandhofen
    {"name": "2801254", "latitude": 49.526944, "longitude": 8.413889, "adultPopulation": 10227},  # osm_id of Schonau
    {"name": "2801091", "latitude": 49.528333, "longitude": 8.448056, "adultPopulation": 20848},  # osm_id of Waldhof
    {"name": "3286568", "latitude": 49.476944, "longitude": 8.535833, "adultPopulation": 6186},
    # osm_id of Neuostheim/Neuhermsheim
    {"name": "3286572", "latitude": 49.469444, "longitude": 8.555833, "adultPopulation": 13180},  # osm_id of Seckenheim
    {"name": "3286562", "latitude": 49.440833, "longitude": 8.575000, "adultPopulation": 4771},
    # osm_id of Friedrichsfeld
    {"name": "2796949", "latitude": 49.523056, "longitude": 8.521944, "adultPopulation": 27077},  # osm_id of Kafertal
    {"name": "2796746", "latitude": 49.511111, "longitude": 8.529167, "adultPopulation": 10297},  # osm_id of Vogelstang
    {"name": "270096", "latitude": 49.513611, "longitude": 8.554444, "adultPopulation": 10297},  # osm_id of Wallstadt
    {"name": "2800523", "latitude": 49.487500, "longitude": 8.539167, "adultPopulation": 11998},  # osm_id of Feudenheim
    {"name": "3286565", "latitude": 49.454722, "longitude": 8.490278, "adultPopulation": 26769},  # osm_id of Neckarau
    {"name": "3286569", "latitude": 49.426111, "longitude": 8.499444, "adultPopulation": 21303}  # osm_id of Rheinau
]

commuterPlaces = [
    {"name": "537049", "latitude": 49.6425, "longitude": 8.4589, "adultPopulation": (commutingIn / commutingAreas),
     "percentageOfTotal": (1 / commutingAreas)},  # osm_id of Burstadt
    {"name": "62347", "latitude": 49.47765, "longitude": 8.43279, "adultPopulation": (commutingIn / commutingAreas),
     "percentageOfTotal": (1 / commutingAreas)},  # osm_id of Ludwigshafen am Rhein
    {"name": "285864", "latitude": 49.39880, "longitude": 8.67240, "adultPopulation": (commutingIn / commutingAreas),
     "percentageOfTotal": (1 / commutingAreas)}  # osm_id of Heidelberg
]

allPlaces = places + commuterPlaces

for place in places:
    totalAdultPopulation += place['adultPopulation']

for place in places:
    percentage = (place['adultPopulation'] / totalAdultPopulation) * 100
    place['percentageOfTotal'] = percentage

# debug
print("Total adult population: " + str(totalAdultPopulation))
for place in places:
    print(place)
for place in commuterPlaces:
    print(place)
for place in allPlaces:
    print(place)
