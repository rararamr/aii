import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (replace with your actual file path and column name)
df = pd.read_csv("ShopeeScrap9.csv")
ratings = df["rating_star"]  # Replace with the appropriate column name

# Calculate the mean and standard deviation of the ratings
mean = ratings.mean()
std = ratings.std()

# Calculate z-scores for each rating in the CSV file
z_scores = (ratings - mean) / std

# Save the z-scores to a new CSV file
z_scores.to_csv("z_scores3.csv")

# Let the user know the calculation is complete
print("Z-scores have been saved to z_scores.csv")

df = pd.read_csv("z_scores3.csv")
# Adjust thresholds based on z-scores (optional)
positive_threshold = 0.20  # Adjust as needed, consider standard deviation
negative_threshold = -4.90  # Adjust as needed

# Group ratings based on z-scores

positive_count = (z_scores > positive_threshold).sum()
negative_count = (z_scores < negative_threshold).sum()
neutral_count = len(z_scores) - positive_count - negative_count

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Neutral:", neutral_count)

# Data for the histogram (group counts)
data = [positive_count, negative_count, neutral_count]

# Labels for each bar (group categories)
labels = ['Positive', 'Negative', 'Neutral']

# Plotting the histogram using group counts
plt.bar(labels, data, color=['green', 'red', 'grey'])

# Add labels and title
plt.xlabel('Rating Category')
plt.ylabel('Number of Ratings')
plt.title('Distribution of Z-Scores (Grouped)')

# Display the plot
plt.show()