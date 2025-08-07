import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
messages = pd.read_csv(
    "F:/NLP/NLP/projects/spam_classifier/data/SMSSpamCollection.txt",
    sep="\t",
    names=["label", "messages"]
)

# Text preprocessing
lemmatizer = WordNetLemmatizer()
corpus = []
stop_words = set(stopwords.words('english'))

for message in messages["messages"]:
    review = re.sub('[^a-zA-Z]', ' ', message)
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in stop_words]
    corpus.append(' '.join(review))

# Feature extraction
vectorizer = CountVectorizer(max_features=5000)
X = vectorizer.fit_transform(corpus).toarray()

# Labels
y = pd.get_dummies(messages['label'], drop_first=True).values.ravel()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", conf_matrix)
print("Accuracy:", accuracy)