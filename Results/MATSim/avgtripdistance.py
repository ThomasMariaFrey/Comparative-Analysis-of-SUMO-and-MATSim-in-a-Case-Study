
import pandas as pd

# put your own file here
file_paths = [
    r"D:\MATSimOutput\outputFinal1\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal2\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal3\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal4\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal5\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal6\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal7\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal8\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal9\ITERS\it.100\100.trips.csv.gz",
    r"D:\MATSimOutput\outputFinal10\ITERS\it.100\100.trips.csv.gz"
]

# this is used for the summing of the files to calculate the avereage
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

sum_trav_time = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}
count_trav_time = {
    'car': 0,
    'pt': 0,
    'walk': 0,
    'bike': 0
}


# Function to convert time in HH:MM:SS format to total seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


# Process each file
for file_path in file_paths:
    data = pd.read_csv(file_path)
    data_split = data[
        'person;trip_number;trip_id;dep_time;trav_time;wait_time;traveled_distance;euclidean_distance;main_mode;longest_distance_mode;modes;start_activity_type;end_activity_type;start_facility_id;start_link;start_x;start_y;end_facility_id;end_link;end_x;end_y;first_pt_boarding_stop;last_pt_egress_stop'].str.split(
        ';', expand=True)

    # Rename the columns for furthre transformation
    data_split.columns = [
        'person', 'trip_number', 'trip_id', 'dep_time', 'trav_time', 'wait_time',
        'traveled_distance', 'euclidean_distance', 'main_mode', 'longest_distance_mode',
        'modes', 'start_activity_type', 'end_activity_type', 'start_facility_id',
        'start_link', 'start_x', 'start_y', 'end_facility_id', 'end_link',
        'end_x', 'end_y', 'first_pt_boarding_stop', 'last_pt_egress_stop'
    ]
    data_split['traveled_distance'] = pd.to_numeric(data_split['traveled_distance'], errors='coerce')
    data_split['trav_time'] = data_split['trav_time'].apply(time_to_seconds)
    for mode in ['car', 'pt', 'walk', 'bike']:
        mode_data = data_split[data_split['main_mode'] == mode]
        sum_distances[mode] += mode_data['traveled_distance'].sum()
        count_distances[mode] += mode_data['traveled_distance'].count()

        sum_trav_time[mode] += mode_data['trav_time'].sum()
        count_trav_time[mode] += mode_data['trav_time'].count()


average_traveled_distances = {mode: (sum_distances[mode] / count_distances[mode]) if count_distances[mode] > 0 else None
                              for mode in sum_distances}
average_travel_times = {mode: (sum_trav_time[mode] / count_trav_time[mode]) if count_trav_time[mode] > 0 else None for
                        mode in sum_trav_time}

# Output the resultsFull
print("The average traveled distance for rows where the main mode is 'Car':", average_traveled_distances['car'])
print("The average travel time for rows where the main mode is 'Car':", average_travel_times['car'])

print("The average traveled distance for rows where the main mode is 'PT':", average_traveled_distances['pt'])
print("The average travel time for rows where the main mode is 'PT':", average_travel_times['pt'])

print("The average traveled distance for rows where the main mode is 'Walk':", average_traveled_distances['walk'])
print("The average travel time for rows where the main mode is 'Walk':", average_travel_times['walk'])

print("The average traveled distance for rows where the main mode is 'Bike':", average_traveled_distances['bike'])
print("The average travel time for rows where the main mode is 'Bike':", average_travel_times['bike'])
with open(r"data/average_trip_distances_and_times.txt", "w") as file:
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
