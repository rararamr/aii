import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file containing the ratings and timestamps
df = pd.read_csv("ShopeeScrap13.csv")

# Assuming your ratings are in a column named "rating" and timestamps in "timestamp"
ratings = df["rating_star"]
timestamps = df["ctime"]

# Ensure timestamps are in datetime format
if not pd.api.types.is_datetime64_dtype(df["ctime"]):
    df["ctime"] = pd.to_datetime(df["ctime"])  # Convert if necessary

# Set timestamp as index
df = df.set_index("ctime")


# Resample data by desired time period (e.g., monthly)
resampled_data = df["rating_star"].resample('M').mean()  # Monthly average


# Plotting the time series
plt.plot(resampled_data.index, resampled_data.values)
plt.xlabel('Date')
plt.ylabel('Average Rating')
plt.title('Customer Satisfaction Over Time (Monthly Average)')

# Optional: Add rolling average or other smoothing techniques
# plt.plot(resampled_data.rolling(window=3).mean(), label='Rolling Average (3 Months)')

plt.legend()  # Show labels if using rolling average or other plots
plt.show()
