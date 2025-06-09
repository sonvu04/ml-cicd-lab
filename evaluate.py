# evaluate.py
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
_, X_test, _, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

# Load model
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

# Predict and evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")
