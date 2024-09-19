import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the original dataset (replace 'your_original_dataset.csv' with your actual file name)
df = pd.read_csv('ShopeeScrap11.csv')

# Convert 'ctime' to datetime in df
df['ctime'] = pd.to_datetime(df['ctime'], unit='s')


# 1. Create a new DataFrame `df_new` with the same number of rows as `df`
df_new = pd.DataFrame(index=range(len(df)))

# 2. Generate random integer values between 1 and 4 (inclusive) for the `rating_star` column
df_new['rating_star'] = np.random.randint(1, 5, size=len(df))  # 1 to 4 (inclusive)

# 3. Generate unique datetime values for the `ctime` column
min_ctime = pd.Timestamp(df['ctime'].min()) - pd.DateOffset(years=1)  # Convert to Timestamp
max_ctime = pd.Timestamp(df['ctime'].max()) + pd.DateOffset(years=1)  # Convert to Timestamp
df_new['ctime'] = pd.to_datetime(
    np.random.randint(min_ctime.value, max_ctime.value, dtype=np.int64, size=len(df))
)

# Ensure unique `ctime` values
while not df_new['ctime'].is_unique:
    df_new['ctime'] = pd.to_datetime(
        np.random.randint(min_ctime.value, max_ctime.value, size=len(df))
    )

# 4. Combine the original and new DataFrames
df_combined = pd.concat([df, df_new], ignore_index=True)

# 5. Extract time-based features
df_combined['hour'] = df_combined['ctime'].dt.hour
df_combined['dayofweek'] = df_combined['ctime'].dt.dayofweek
df_combined['month'] = df_combined['ctime'].dt.month

# 6. Drop the original `ctime` column
df_combined.drop('ctime', axis=1, inplace=True)

# 7. Split the data into features (X) and target variable (y)
X = df_combined.drop('satisfaction_label', axis=1)
y = df_combined['satisfaction_label']

# 8. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 9. Define the parameter grids (same as before)
dt_param_grid = {
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 10. Create GridSearchCV objects
dt_model = DecisionTreeClassifier(random_state=42)
rf_model = RandomForestClassifier(random_state=42)
dt_grid_search = GridSearchCV(estimator=dt_model, param_grid=dt_param_grid, cv=5)
rf_grid_search = GridSearchCV(estimator=rf_model, param_grid=rf_param_grid, cv=5)

# 11. Fit the GridSearchCV objects
dt_grid_search.fit(X_train, y_train)
rf_grid_search.fit(X_train, y_train)

# 12. Get the best models
best_dt_model = dt_grid_search.best_estimator_
best_rf_model = rf_grid_search.best_estimator_

# 13. Make predictions
best_dt_predictions = best_dt_model.predict(X_test)
best_rf_predictions = best_rf_model.predict(X_test)

# 14. Evaluate the accuracy
best_dt_accuracy = accuracy_score(y_test, best_dt_predictions)
best_rf_accuracy = accuracy_score(y_test, best_rf_predictions)

print(f'Best Decision Tree Accuracy (Combined Data): {best_dt_accuracy:.2f}')
print(f'Best Random Forest Accuracy (Combined Data): {best_rf_accuracy:.2f}')
