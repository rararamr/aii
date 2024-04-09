# Import libraries
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Load your data from a CSV file
data = pd.read_csv("your_data.csv")

# Load your data (replace with your data loading logic)
X = ...  # Features (e.g., order details, customer demographics)
y = data["satisfaction_score"]  # Customer satisfaction labels (e.g., satisfied/dissatisfied)

# Encode categorical features (if any)
le = LabelEncoder()
for col in X.columns:
  if X[col].dtype == 'object':
    X[col] = le.fit_transform(X[col])

# Scale numerical features (if necessary)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create and train the decision tree model
model = DecisionTreeClassifier(max_depth=5)  # Adjust hyperparameters as needed
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# (Optional) Feature Importance Analysis
# Use model.feature_importances_ to analyze which features influenced predictions
