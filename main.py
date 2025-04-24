from load_data import load_data
from sort import bubble_sort
from power_curve import plot_power_curve

# Load the data
data = load_data('activity.csv')
power_W = data['PowerOriginal']

# Sort the power data
sorted_power_W = bubble_sort(power_W)

# Plot the power curve
plot_power_curve(sorted_power_W)