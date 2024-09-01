'''
This file is used to create a graph representing the amount of activities taken over 24 hours.
'''

import matplotlib.pyplot as plt
import numpy as np

# Data source that are used
hours = np.arange(0, 25)
home_values = [
    37900, 37900, 37900, 37900, 37894, 37833, 37354, 35287, 29417, 19640,
    9549, 3091, 695, 415, 1686, 5931, 14473, 24971, 32874, 36562,
    37662, 37882, 37899, 37899, 37900
]
work_values = [
    0, 0, 0, 3, 47, 361, 1934, 6888, 15934, 26339,
    33758, 36909, 37754, 37830, 37442, 35627, 30506, 21222, 10867, 3863,
    946, 143, 12, 1, 1
]
fig, ax1 = plt.subplots(figsize=(10, 6))
# values where the home is considered
ax1.plot(hours, home_values, 'o-', color='red', label='Home')
ax1.set_xlabel('Hour of Departure', color='black')
ax1.set_ylabel('Amount of Agents at Activity', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelcolor='black')
# values where the work is considered
ax1.plot(hours, work_values, 'o-', color='blue', label='Work')
ax1.title.set_color('black')
ax1.xaxis.label.set_color('black')
ax1.yaxis.label.set_color('black')
ax1.spines['left'].set_color('black')
ax1.spines['bottom'].set_color('black')

# show all hours on x axis
ax1.set_xticks(hours)

# Adding light grey lines
for ytick in ax1.get_yticks():
    ax1.axhline(y=ytick, color='lightgrey', linestyle=':', linewidth=1)
plt.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.9)
ax1.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.savefig('data/Relative_Frequency_Departure_Time.png', dpi=300)
plt.show()
