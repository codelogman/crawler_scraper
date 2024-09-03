
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from pymongo import MongoClient
import pandas as pd

class ContentClassifier:
    def __init__(self, db_client):
        self.db = db_client["crawler_database"]
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english')),
            ('classifier', MultinomialNB())
        ])
        self.load_data_and_train()

    def load_data_and_train(self):
        # Load training data from MongoDB
        data = pd.DataFrame(list(self.db.content.find()))
        if not data.empty:
            texts = data['text'].tolist()
            categories = data['category'].tolist() if 'category' in data.columns else None
            if categories:
                self.model.fit(texts, categories)

    def classify_text(self, text):
        # Classify new content
        return self.model.predict([text])[0]

    def update_keywords(self):
        # Analyze contents and update keywords based on classification results
        contents = self.db.content.find()
        for content in contents:
            category = self.classify_text(content['text'])
            self.db.keywords.update_one({'keyword': content['text']}, {'$set': {'keyword': category}}, upsert=True)

# Configuración del cliente MongoDB y del clasificador
client = MongoClient("mongodb://localhost:27017/")
classifier = ContentClassifier(client)

# Periodic retraining and updating keywords
classifier.update_keywords()
