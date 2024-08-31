"""
Generating a person datafile for CEMDAP following the outline from the paper  Demand Generation for Multi-Agent
Transport Simulations based on an Econometric Travel Behavior Model and a Traffic-Count-based Calibration Algorithm
by Dominik Ziemke.

This generator generates the elaborate model.

| Parameter | Description                 | Initial Model       | Elaborate Model    |
| --------- | --------------------------- | ------------------- | ------------------ |
| HHID      | Household ID                | cf. B.1             | cf. B.1            |
| PerID     | Person ID                   | HHID + 01           | HHID + 01          |
| Aemp      | Adult is employed           | 1                   | 0 or 1***          |
| Stu       | Adult or child is a student | 0                   | 0 or 1***          |
| License   | Person is licensed to drive | 1                   | 1                  |
| WorkTSZ   | Work TSZ                    | randomly selected*  | randomly selected* |
| SchTSZ    | School TSZ                  | -99                 | randomly selected* |
| Female    | Person is female            | 1                   | 0 or 1****         |
| Age       | Age                         | randomly selected** | ?***               |
| Parent    | Parent                      | 1                   | 0                  |
| ...       | 42 remaining variables      | 0                   | 0                  |

This is done in accordance to the current population and movement data as stated in
https://www.mannheim.de/de/stadt-gestalten/daten-und-fakten/bevoelkerung

The file has 59 variables where 10 are required and the remaining 49 are not relevant and set to 0.

| Nr. | Stadtbezirk/Stadtteil             | Wohnberechtigte Bevlkerung | Unter 18 Jahre | 18 bis unter 25 Jahre | 25 bis unter 30 Jahre | 30 bis unter 65 Jahre | 65 bis unter 80 Jahre | 80 Jahre und lter |
|     | Gesamt Mannheim               | 330.896                     | 50.522         | 31.831                | 27.671                | 159.739               | 41.201                | 19.932             |
Number of adults 18+ only = 330896 - 50522 = 280374

Unemployt:
| Stadtbezirke/Stadtteile       | Arbeitslose insgesamt | unter 25 Jahre Anzahl | unter 25 Jahre % | 55 Jahre und lter Anzahl | 55 Jahre und lter % |
| Mannheim                      | 12,112                | 444                   | 3.7              | 2,577                     | 21.3                 |

unemployed % 12112 / 280374 = 0.0431994
nonstudents % 30
"""

import random
import geodata

data = ""

i = 1
e = 0

nonRelevantVariables = "\t0" * 49

random_number = random.random()

# Generate Age
population = geodata.totalAdultPopulation
age18To25 = 31831 / population
age25To30 = 27671 / population
age30To65 = 159739 / population
age65To80 = 41201 / population
age80Up = 19932 / population
age = 0
unemployedPercentage = 0.0431994
studentPercentage = 0.3
femalePercentage = 0.5


# Generate Population
while i <= geodata.totalAdultPopulation:
    # Accounting for the part of population that is commuting out of Mannheim
    if random.random() < (geodata.commutingOut / geodata.totalAdultPopulation):
        weights = [place['percentageOfTotal'] for place in geodata.commuterPlaces]
        trafficSurveyZoneWork = random.choices(geodata.commuterPlaces, weights=weights, k=1)[0]['name']
        trafficSurveyZoneSchool = random.choices(geodata.commuterPlaces, weights=weights, k=1)[0]['name']
    else:
        weights = [place['percentageOfTotal'] for place in geodata.places]
        trafficSurveyZoneWork = random.choices(geodata.places, weights=weights, k=1)[0]['name']
        trafficSurveyZoneSchool = random.choices(geodata.places, weights=weights, k=1)[0]['name']

    agePercentage = random.random()
    if agePercentage < age18To25:
        age = random.randint(18, 24)
    elif agePercentage < (age18To25 + age25To30):
        age = random.randint(25, 29)
    elif agePercentage < (age18To25 + age25To30 + age30To65):
        age = random.randint(30, 64)
    elif agePercentage < (age18To25 + age25To30 + age30To65 + age65To80):
        age = random.randint(65, 79)
    else:
        age = random.randint(80, 99)

    if random.random() > unemployedPercentage:
        employed = 1
    else:
        employed = 0

    if age < 31 and random.random() < studentPercentage:
        student = 1
    else:
        student = 0

    if random.random() > femalePercentage:
        female = 0
    else:
        female = 1

    # household id, person id, employed, student, licence, workTSZ,scoolTSC, Female, Agent, Parent
    currentString = str(i) + "\t" + str(i + 1) + "\t" + str(employed) + "\t" + str(student) + "\t" + "1" + "\t" \
                    + trafficSurveyZoneWork + "\t" + trafficSurveyZoneSchool + "\t" + str(female) + "\t" + str(age) \
                    + "\t" + "0" + nonRelevantVariables + "\n"

    data = data + currentString

    # For debug purposes
    if i > 2 ** e:
        print("Iteration" + str(i))
        print("Current String:")
        print(currentString)
        e = e + 1

    i = i + 1

# Commuting in Population
while i - geodata.totalAdultPopulation <= geodata.commutingIn:
    weights = [place['percentageOfTotal'] for place in geodata.places]
    trafficSurveyZoneWork = random.choices(geodata.places, weights=weights, k=1)[0]['name']
    trafficSurveyZoneSchool = random.choices(geodata.places, weights=weights, k=1)[0]['name']

    agePercentage = random.random()
    if agePercentage < age18To25:
        age = random.randint(18, 24)
    elif agePercentage < (age18To25 + age25To30):
        age = random.randint(25, 29)
    elif agePercentage < (age18To25 + age25To30 + age30To65):
        age = random.randint(30, 64)
    elif agePercentage < (age18To25 + age25To30 + age30To65 + age65To80):
        age = random.randint(65, 79)
    else:
        age = random.randint(80, 99)

    if random.random() > unemployedPercentage:
        employed = 1
    else:
        employed = 0

    if age < 31 and random.random() < studentPercentage:
        student = 1
    else:
        student = 0

    if random.random() > femalePercentage:
        female = 0
    else:
        female = 1

    # household id, person id, employed, student, licence, workTSZ,scoolTSC, Female, Agent, Parent
    currentString = str(i) + "\t" + str(i + 1) + "\t" + str(employed) + "\t" + str(student) + "\t" + "1" + "\t" \
                    + trafficSurveyZoneWork + "\t" + trafficSurveyZoneSchool + "\t" + str(female) + "\t" + str(age) \
                    + "\t" + "0" + nonRelevantVariables + "\n"

    data = data + currentString

    # For debug purposes
    if i > 2 ** e:
        print("Iteration" + str(i))
        print("Current String:")
        print(currentString)
        e = e + 1

    i = i + 1

# Open a file in write mode
with open('data/persons.dat', 'w') as file:
    file.write(data)

print("Text data has been written to persons.dat. It contains " + str(i) + "lines.")
