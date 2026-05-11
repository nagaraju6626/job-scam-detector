import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

import pickle

# Load real dataset
data = pd.read_csv("fake_job_postings.csv")

# Remove empty values
data = data[['description', 'fraudulent']].dropna()

# Inputs and labels
X = data['description']

y = data['fraudulent']

# AI model
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train model
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Real Dataset Model Trained Successfully")