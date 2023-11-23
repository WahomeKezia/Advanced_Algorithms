import matplotlib.pyplot as plt
import numpy as np

# Assuming n varies from 1 to 100 for illustration
n_values = np.arange(1, 101)

# T(n) and R(n) functions
bubble_sort_time = n_values**2
selection_sort_time = n_values**2

# Plotting the graphs
plt.plot(n_values, bubble_sort_time, label='Bubble Sort')
plt.plot(n_values, selection_sort_time, label='Selection Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time')
plt.legend()
plt.show()
