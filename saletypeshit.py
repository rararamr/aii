import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df_combined = pd.read_csv('combined_processed_data.csv')

# Display the first 5 rows
print(df_combined.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_combined.info())

# Convert the `ctime` column to datetime
df_combined['ctime'] = pd.to_datetime(df_combined['ctime'])

# Calculate minimum and maximum ctime values
min_ctime = df_combined['ctime'].min()
max_ctime = df_combined['ctime'].max()

print(min_ctime, max_ctime)
# Generate 50 random sale dates within the range
num_sale_dates = 50
sale_dates = pd.to_datetime(
    np.random.randint(min_ctime.value, max_ctime.value, size=num_sale_dates), unit='ns'
)

# Create a new column `is_sale`
df_combined['is_sale'] = df_combined['ctime'].isin(sale_dates).astype(int)

# Encode satisfaction_label to numerical values
satisfaction_mapping = {'Very Satisfied': 1, 'Satisfied': 0, 'Neutral': -1, 'Dissatisfied': -2}
df_combined['satisfaction_label_encoded'] = df_combined['satisfaction_label'].map(satisfaction_mapping)

# Calculate correlation between `is_sale` and `satisfaction_label_encoded`
correlation = df_combined['is_sale'].corr(df_combined['satisfaction_label_encoded'])

# Display the calculated correlation
print(f"Correlation between sale and satisfaction: {correlation:.3f}")

