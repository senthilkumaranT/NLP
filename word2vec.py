import nltk
import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

paragraph = """
Good morning to all. I am Dr. A.P.J. Abdul Kalam. Today, I want to talk to you about dreams and the power of perseverance. Dreams are not what you see when you sleep. Dreams are those that do not let you sleep. Each one of you has a unique talent and a special role to play in building our nation. Never give up on your dreams, no matter how difficult the journey may seem.

When I was a young boy in Rameswaram, I had many challenges. But I worked hard, learned from my teachers, and never lost hope. Education and dedication helped me become a scientist and later, the President of India. I believe that with hard work, honesty, and courage, you can achieve anything.

Let us all work together to make India a developed nation. Let us spread love, peace, and knowledge. Remember, the future of our country is in your hands. Dream big, aim high, and never stop learning.

Thank you.
"""

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)


#preparing data set
sentence = nltk.sent_tokenize(text)

sentence =[nltk.word_tokenize(sentences) for sentences in sentence]

print(sentence)

for i in range(len(sentence)):
    sentence[i]=[word for word in sentence[i] if word not in stopwords.words('english')]


print(sentence)


model =Word2Vec(sentence,min_count=1)

# Get the vocabulary using the new API
words = list(model.wv.key_to_index.keys())

print(words)