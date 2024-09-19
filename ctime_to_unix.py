import pandas as pd
from datetime import datetime

# Load the data
data = pd.read_csv('modified_ratings.csv')

# Convert 'ctime' to Unix timestamp
data['ctime'] = pd.to_datetime(data['ctime'], format='%d/%m/%Y %H:%M')

# Convert to Unix timestamp
data['ctime'] = data['ctime'].astype('int64') // 10**9

# Save the modified data
data.to_csv('modified_data.csv', index=False)
