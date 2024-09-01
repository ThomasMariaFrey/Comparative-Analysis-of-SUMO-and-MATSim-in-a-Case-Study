'''
This file is used to generate the avearge activity time of the agent throughout the day.
'''
import matplotlib.pyplot as plt
import numpy as np

# Data that is to be used
hours = np.arange(0, 25)
travel_time_walk = [
    0.0, 0.0, 0.0, 16.94, 12.84, 13.02, 13.24, 13.22, 13.08, 13.26, 13.26,
    13.40, 13.37, 12.81, 12.85, 13.15, 12.89, 12.91, 13.12, 13.08,
    12.68, 14.35, 15.19, 0.0, 0.0
]
plt.figure(figsize=(10, 6))
plt.bar(hours, travel_time_walk, color='skyblue', label='BEAM')
plt.xlabel('Hour of the Day')
plt.ylabel('Travel Time in Minutes')
plt.grid(axis='y', linestyle=':', color='grey')
plt.xticks(hours)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig('data/BeamTravelTime.png', dpi=300)
plt.show()
