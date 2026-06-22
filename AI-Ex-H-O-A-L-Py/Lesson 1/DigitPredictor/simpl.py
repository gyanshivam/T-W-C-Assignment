"""
Simple Digit Predictor using a Multi-Layer Perceptron (Neural Network)
with scikit-learn. No TensorFlow required.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
import time

# 1. Load MNIST dataset (handwritten digits)
print("Loading MNIST dataset...")
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False, parser='auto')

# Convert to float and scale pixel values to [0,1]
X = X / 255.0
y = y.astype(int)  # targets as integers

# 2. Split into train (60k) and test (10k)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10000, random_state=42, stratify=y)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# 3. Build a simple neural network with one hidden layer (100 neurons)
#    Activation: ReLU, solver: adam, max iterations: 10 (for quick demo)
print("\nBuilding the neural network...")
mlp = MLPClassifier(
    hidden_layer_sizes=(100,),   # one hidden layer with 100 neurons
    activation='relu',
    solver='adam',
    max_iter=10,
    random_state=42,
    verbose=True
)

# 4. Train the model
print("\nTraining the model (this may take 1-2 minutes)...")
start = time.time()
mlp.fit(X_train, y_train)
end = time.time()
print(f"Training completed in {end - start:.2f} seconds")

# 5. Evaluate on test set
y_pred = mlp.predict(X_test)
accuracy = mlp.score(X_test, y_test)
print(f"\nTest accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

# Confusion matrix (optional: visualisation)
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion matrix (first 5x5):")
print(cm[:5, :5])

# 6. Make predictions and show some examples
print("\n--- Visualizing predictions on test images ---")
fig, axes = plt.subplots(3, 5, figsize=(12, 8))
axes = axes.ravel()

for i in range(15):
    axes[i].imshow(X_test[i].reshape(28, 28), cmap='gray')
    axes[i].set_title(f"True: {y_test[i]}\nPred: {y_pred[i]}")
    axes[i].axis('off')
plt.tight_layout()
plt.show()

# 7. Additional: show a single prediction in detail
sample_idx = 0
sample_image = X_test[sample_idx].reshape(28, 28)
predicted = mlp.predict([X_test[sample_idx]])[0]
true_label = y_test[sample_idx]
print(f"\nSingle image prediction: True = {true_label}, Predicted = {predicted}")

# Optional: display probability distribution (for the first test sample)
if hasattr(mlp, 'predict_proba'):
    probs = mlp.predict_proba([X_test[sample_idx]])[0]
    plt.figure(figsize=(8, 4))
    plt.bar(range(10), probs)
    plt.title(f"Probability distribution for test sample {sample_idx} (true digit: {true_label})")
    plt.xlabel("Digit")
    plt.ylabel("Probability")
    plt.show()

print("\nDone! This simple neural network learned to recognise handwritten digits.")