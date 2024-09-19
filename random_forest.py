import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load your data
data_path = 'modified_data.csv'
data = pd.read_csv(data_path)

# Convert 'ctime' from Unix to datetime and then to numeric format
data['ctime'] = pd.to_datetime(data['ctime'], unit='s')
reference_date = pd.Timestamp("1970-01-01")
data['ctime'] = (data['ctime'] - reference_date).dt.total_seconds()

# Encode categorical variables (if necessary)
label_enc = LabelEncoder()
data['shopid'] = label_enc.fit_transform(data['shopid'])

# Split the data into features and target
X = data[['shopid', 'ctime']]
y = data['rating_star']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_clf = RandomForestClassifier(random_state=42, n_estimators=100)
rf_clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf_clf.predict(X_test)
print(classification_report(y_test, y_pred))
