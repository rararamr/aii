import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("z_scores1.csv")

# Generate random data for the histogram
data = df["rating_star"]

# Plotting a basic histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Data from CSV')

# Display the plot
plt.show()
