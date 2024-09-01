import pandas as pd

file_paths = [
    r"D:\MATSimOutput\outputFinal1\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal2\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal3\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal4\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal5\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal6\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal7\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal8\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal9\ITERS\it.100\100.legHistogram.txt",
    r"D:\MATSimOutput\outputFinal10\ITERS\it.100\100.legHistogram.txt"
]

cumulative_df = None
#prepare the file data for calculation
for file_path in file_paths:
    df = pd.read_csv(file_path, delimiter="\t")
    if cumulative_df is None:
        cumulative_df = df[['time', 'departures_all']].copy()
    else:
        cumulative_df['departures_all'] += df['departures_all']

cumulative_df['departures_all'] /= len(file_paths)

average_departures_list = list(zip(cumulative_df['time'], cumulative_df['departures_all']))

print(average_departures_list)

data = average_departures_list

hourly_sums = {}
hourly_counts = {}

for time_str, value in data:
    hour = time_str.split(":")[0]
    if hour not in hourly_sums:
        hourly_sums[hour] = 0.0
        hourly_counts[hour] = 0
    hourly_sums[hour] += value
    hourly_counts[hour] += 1

hourly_averages = []
for hour in sorted(hourly_sums.keys()):
    average = hourly_sums[hour] / hourly_counts[hour]
    hourly_averages.append((hour, average))

hourly_averages = hourly_averages[:25]

total_sum = sum(value for _, value in hourly_averages)

hourly_averages = [(key, value, value / total_sum) for key, value in hourly_averages]
print(hourly_averages)

with open('data/departureTime.txt', 'w') as file:
    for time_str, avg, relfrq in hourly_averages:
        file.write(f"{time_str}: {avg:.2f}, {relfrq}\n")
