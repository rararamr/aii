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
z_scores.to_csv("z_scores2.csv")

# Let the user know the calculation is complete
print("Z-scores have been saved to z_scores.csv")
