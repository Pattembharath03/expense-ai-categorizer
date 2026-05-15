import pandas as pd

# Convert text into vectors
from sklearn.feature_extraction.text import TfidfVectorizer

# ML algorithm
from sklearn.naive_bayes import MultinomialNB

# Pipeline combines steps
from sklearn.pipeline import Pipeline

# Save model
import pickle

# Load dataset
data = pd.read_csv("../dataset/expenses.csv")

# Input text
X = data['text']

# Categories
y = data['category']

# Create AI pipeline
model = Pipeline([

    ('tfidf', TfidfVectorizer()),

    ('classifier', MultinomialNB())

])

# Train model
model.fit(X, y)

# Save trained model
pickle.dump(model, open('model.pkl', 'wb'))

print("AI Model Trained Successfully!")