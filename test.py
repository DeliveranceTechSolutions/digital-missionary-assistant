import torch
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from classifier import EmailClassifier

# Assuming you have saved your model as 'email_classifier_model.pth'
# and have the vectorizer and label_encoder objects from your training script
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Load the best model
best_model = EmailClassifier(
    self.vectorizer.get_feature_names_out().__len__(), 
    len(self.label_encoder.classes_),
)
best_model.load_state_dict(torch.load('best_model.pth'))
best_model.eval()

# Assuming you have new_data as a list of email texts
new_data_vec = vectorizer.transform(new_data)
new_data_tensor = torch.tensor(new_data_vec.toarray(), dtype=torch.float32)

# Make predictions
with torch.no_grad():
    new_data_outputs = best_model(new_data_tensor)
    _, predicted = torch.max(new_data_outputs, 1)

# Inverse transform predicted labels
predicted_labels = label_encoder.inverse_transform(predicted.numpy())

# Print the predictions
for data, label in zip(new_data, predicted_labels):
    print(f"Email: {data}\nPredicted Label: {label}\n")