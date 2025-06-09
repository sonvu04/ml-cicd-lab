# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load data
iris = load_iris()
X_train, _, y_train, _ = train_test_split(iris.data, iris.target, test_size=0.3)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
os.makedirs("artifacts", exist_ok=True)
with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Training complete. Model saved to artifacts/model.pkl")