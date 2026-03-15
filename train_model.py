import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from feature_extraction import extract_features

# Load dataset
df = pd.read_csv('phishing_dataset.csv')

# Extract features
df['features'] = df['URL'].apply(extract_features)

# Prepare data
X = list(df['features'])
y = df['Label']

import numpy as np
X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Save model
joblib.dump(model, 'phishing_model.pkl')