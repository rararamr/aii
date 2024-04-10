import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file containing the ratings
df = pd.read_csv("ShopeeScrap10.csv")

# Assuming your ratings are in a column named "rating"
ratings = df["rating_star"]

# Calculate statistics
mean_rating = ratings.mean()
median_rating = ratings.median()
mode_rating = ratings.mode()[0]  # Get the first mode if there are multiple
std_dev = ratings.std()

# Print the results
print("Mean Rating:", mean_rating)
print("Median Rating:", median_rating)
print("Mode Rating:", mode_rating)
print("Standard Deviation:", std_dev)

# Distribution analysis (histogram)
plt.hist(ratings, bins=20, edgecolor='black')  # Adjust bins as needed
plt.xlabel('Rating Score')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Ratings')
plt.show()
