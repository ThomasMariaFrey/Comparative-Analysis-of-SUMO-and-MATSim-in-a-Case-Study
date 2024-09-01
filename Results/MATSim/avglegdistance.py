import pandas as pd


def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


# place your file paths here
file_paths = [
    r"D:\MATSimOutput\outputFinal1\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal2\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal3\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal4\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal5\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal6\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal7\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal8\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal9\ITERS\it.100\100.legs.csv.gz",
    r"D:\MATSimOutput\outputFinal10\ITERS\it.100\100.legs.csv.gz"
]

# these are used to calculate the average over 10 runs
sum_distances = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}
count_distances = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}

sum_trav_times = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}
count_trav_times = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}

for file_path in file_paths:
    data = pd.read_csv(file_path)
    # The data has to be split here so that it can be further processed.
    data_split = data[
        'person;trip_id;dep_time;trav_time;wait_time;distance;mode;start_link;start_x;start_y;end_link;end_x;end_y;access_stop_id;egress_stop_id;transit_line;transit_route;vehicle_id'].str.split(
        ';', expand=True)
    data_split.columns = [
        'person', 'trip_id', 'dep_time', 'trav_time', 'wait_time',
        'distance', 'mode', 'start_link', 'start_x', 'start_y',
        'end_link', 'end_x', 'end_y', 'access_stop_id',
        'egress_stop_id', 'transit_line', 'transit_route', 'vehicle_id'
    ]
    # Transfer to the correct format here.
    data_split['distance'] = pd.to_numeric(data_split['distance'], errors='coerce')
    data_split['trav_time'] = data_split['trav_time'].apply(time_to_seconds)
    for mode in ['car', 'pt', 'walk', 'bike']:
        mode_data = data_split[data_split['mode'] == mode]
        sum_distances[mode] += mode_data['distance'].sum()
        count_distances[mode] += mode_data['distance'].count()
        sum_trav_times[mode] += mode_data['trav_time'].sum()
        count_trav_times[mode] += mode_data['trav_time'].count()


average_traveled_distances = {mode: (sum_distances[mode] / count_distances[mode]) if count_distances[mode] > 0 else None
                              for mode in sum_distances}
average_travel_times = {mode: (sum_trav_times[mode] / count_trav_times[mode]) if count_trav_times[mode] > 0 else None
                        for mode in sum_trav_times}

#Outputcheck
print("The average traveled distance for rows where the main mode is 'Car':", average_traveled_distances['car'])
print("The average travel time for rows where the main mode is 'Car':", average_travel_times['car'])
print("The average traveled distance for rows where the main mode is 'PT':", average_traveled_distances['pt'])
print("The average travel time for rows where the main mode is 'PT':", average_travel_times['pt'])
print("The average traveled distance for rows where the main mode is 'Walk':", average_traveled_distances['walk'])
print("The average travel time for rows where the main mode is 'Walk':", average_travel_times['walk'])
print("The average traveled distance for rows where the main mode is 'Bike':", average_traveled_distances['bike'])
print("The average travel time for rows where the main mode is 'Bike':", average_travel_times['bike'])
# Write the resultsFull to a text file
with open(r"data/average_legdistance_and_time.txt", "w") as file:
    file.write(
        f"The average traveled distance for rows where the main mode is 'Car': {average_traveled_distances['car']}\n")
    file.write(f"The average travel time for rows where the main mode is 'Car': {average_travel_times['car']}\n\n")
    file.write(
        f"The average traveled distance for rows where the main mode is 'PT': {average_traveled_distances['pt']}\n")
    file.write(f"The average travel time for rows where the main mode is 'PT': {average_travel_times['pt']}\n\n")
    file.write(
        f"The average traveled distance for rows where the main mode is 'Walk': {average_traveled_distances['walk']}\n")
    file.write(f"The average travel time for rows where the main mode is 'Walk': {average_travel_times['walk']}\n\n")
    file.write(
        f"The average traveled distance for rows where the main mode is 'Bike': {average_traveled_distances['bike']}\n")
    file.write(f"The average travel time for rows where the main mode is 'Bike': {average_travel_times['bike']}\n")
