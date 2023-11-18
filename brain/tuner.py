import torch
import joblib
from classifier import EmailClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

class EmailClassifierTester:
    def __init__(self, model_filename, vectorizer, label_encoder):
        self.model_filename = model_filename
        self.vectorizer = vectorizer
        self.label_encoder = label_encoder
        self.loaded_model = self.load_model()

    def load_model(self):
        model = EmailClassifier(
            self.vectorizer.get_feature_names_out().__len__(), 
            len(self.label_encoder.classes_),
        )
        model.load_state_dict(torch.load(self.model_filename))
        model.eval()
        return model

    def preprocess_data(self, new_data):
        new_data_vec = self.vectorizer.transform(new_data)
        new_data_tensor = torch.tensor(new_data_vec.toarray(), dtype=torch.float32)
        return new_data_tensor

    def predict(self, new_data):
        new_data_tensor = self.preprocess_data(new_data)

        with torch.no_grad():
            outputs = self.loaded_model(new_data_tensor)
            _, predicted = torch.max(outputs, 1)

        predicted_labels = self.label_encoder.inverse_transform(predicted.numpy())
        return predicted_labels
    
# Assuming you have saved your model as 'email_classifier_model.pth'
# and have the vectorizer and label_encoder objects from your training script
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Initialize the EmailClassifierTester
tester = EmailClassifierTester('./training_data.pth', vectorizer, label_encoder)

# Test new data
new_data = ["This is a new email.", "Thank you for your message.", "Prayer request for a friend."]
predicted_labels = tester.predict(new_data)
print(predicted_labels)
# Print the predictions
for data, label in zip(new_data, predicted_labels):
    print(f"Email: {data}\nPredicted Label: {label}\n")