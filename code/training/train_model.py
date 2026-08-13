import os

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

DATASET = "data/dataset"
MODEL_PATH = "models/sign_dual_model.pkl"

X, y, labels = [], [], []

for idx, sign in enumerate(sorted(os.listdir(DATASET))):
    sign_dir = os.path.join(DATASET, sign)
    if not os.path.isdir(sign_dir):
        continue

    labels.append(sign)
    for filename in os.listdir(sign_dir):
        if filename.endswith(".npy"):
            data = np.load(os.path.join(sign_dir, filename))
            if len(data) == 126:
                X.append(data)
                y.append(idx)

X = np.asarray(X)
y = np.asarray(y)

if len(X) == 0:
    raise RuntimeError("No valid 126-feature .npy samples found in data/dataset.")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=25,
    n_jobs=-1,
    random_state=42,
)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test) * 100
print(f"Accuracy: {accuracy:.2f}%")

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump((model, labels), MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
