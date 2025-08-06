import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


paragraph = """Natural language processing (NLP) is a fascinating field that combines linguistics, computer science, and artificial intelligence to enable computers to understand, interpret, and generate human language. It involves a variety of techniques and models to process text and speech data, making it possible for machines to perform tasks 
such as language translation, sentiment analysis, text summarization, and question answering. NLP is widely used in applications like chatbots, virtual assistants, and search engines, helping to bridge the gap between human communication and computer understanding. As the amount of digital text and spoken data continues to grow, the importance of NLP in extracting meaningful information and facilitating human-computer interaction becomes even more significant."""

sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = " ".join(words)
print(sentences)







