import nltk

paragraph = """Natural language processing (NLP) is a fascinating field that combines linguistics, computer science, and artificial intelligence to enable computers to understand, interpret, and generate human language. It involves a variety of techniques and models to process text and speech data, making it possible for machines to perform tasks 
such as language translation, sentiment analysis, text summarization, and question answering. NLP is widely used in applications like chatbots, virtual assistants, and search engines, helping to bridge the gap between human communication and computer understanding. As the amount of digital text and spoken data continues to grow, the importance of NLP in extracting meaningful information and facilitating human-computer interaction becomes even more significant."""


import re
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer


WordNet=WordNetLemmatizer()
sentence=nltk.sent_tokenize(paragraph)

corpus=[]
for i in range(len(sentence)):
    review=re.sub('[^a-zA-Z]',' ',sentence[i])
    print("removing the (commos full stop)",review)
    review=review.lower()
    print("lowercase",review)
    review=review.split()
    print("split the words ",review)
    review=[WordNet.lemmatize(word) for word in review if not word in set(stopwords.words("english"))]
    # Join the words back into a string for CountVectorizer
    review_text = ' '.join(review)
    corpus.append(review_text)
    print("review",review_text)

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()
print(x)

