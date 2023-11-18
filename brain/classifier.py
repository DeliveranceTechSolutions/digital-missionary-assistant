import torch
import joblib
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_20newsgroups
from skorch import NeuralNetClassifier
from skorch.helper import predefined_split
from sklearn.model_selection import GridSearchCV

# Load sample email data
emails = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Map categories to your specified labels
label_mapping = {
    'soc.religion.christian': 'prayer',
    'sci.crypt': 'discipleship',
    'rec.autos': 'thank you'
}

emails.target_names = [label_mapping.get(category, 'other') for category in emails.target_names]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(emails.data, emails.target, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Encode labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train_vec.toarray(), dtype=torch.float32)
y_train_tensor = torch.tensor(y_train_encoded, dtype=torch.long)
X_test_tensor = torch.tensor(X_test_vec.toarray(), dtype=torch.float32)
y_test_tensor = torch.tensor(y_test_encoded, dtype=torch.long)

# Define a simple neural network model
class EmailClassifier(nn.Module):
    def __init__(self, input_size, output_size):
        super(EmailClassifier, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        x = torch.sigmoid(self.fc(x))
        return x

print(X_train_tensor, y_train)
# Wrap the PyTorch model in a scikit-learn compatible wrapper
net = NeuralNetClassifier(
    module=EmailClassifier,
    module__input_size=X_train_tensor.shape[1],
    module__output_size=len(set(y_train)),
    criterion=torch.nn.CrossEntropyLoss,
    optimizer=torch.optim.Adam,
    max_epochs=10,
    batch_size=32,
    iterator_train__shuffle=True
)

# Define hyperparameters to search
param_grid = {
    'lr': [0.1, 0.01, 0.001],
    'max_epochs': [5, 10, 15],
    'batch_size': [32, 64, 128]
}

# Create GridSearchCV
grid_search = GridSearchCV(net, param_grid, cv=3, scoring='accuracy')

# Convert PyTorch tensors to NumPy arrays
X_train_numpy = X_train_tensor.numpy()
y_train_numpy = y_train_tensor.numpy()

# Fit the grid search to the data
grid_search.fit(X_train_numpy, y_train_numpy)

# Get the best hyperparameters
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Retrieve the best model from the grid search
best_model = grid_search.best_estimator_

# Save the best model
torch.save(best_model.module_.state_dict(), 'best_model.pth')

# Save the vectorizer and label_encoder to use in tuner.py
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

# Testing the model
with torch.no_grad():
    test_outputs = best_model.predict(X_test_tensor)

# Convert predictions back to original labels
predicted_labels = label_encoder.inverse_transform(test_outputs)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predicted_labels)
print(f"Accuracy: {accuracy * 100:.2f}%")
