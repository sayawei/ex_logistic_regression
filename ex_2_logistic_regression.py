import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

jobs = pd.read_csv(r"C:/Users/User/Desktop/high_growth_jobs.csv")

print(jobs.head())

jobs['Label'] = (jobs['Projected Growth by 2030'] > 100).astype(int)

print("Unique classes in Label:", jobs['Label'].unique())

X = jobs[['Projected Growth by 2030']].values
y = jobs['Label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Unique classes in y_train:", np.unique(y_train))
print("Unique classes in y_test:", np.unique(y_test))

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

X_test_sorted = np.sort(X_test, axis=0)
y_prob = model.predict_proba(X_test_sorted)[:, 1]

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Classes')
plt.plot(X_test_sorted, y_prob, color='red', label='Logistic Curve')
plt.xlabel("Projected Growth by 2030")
plt.ylabel("Probability of High Growth (Class 1)")
plt.title("Logistic Regression: Probability of High Growth vs Projected Growth by 2030")
plt.legend()
plt.show()