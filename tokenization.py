import nltk

paragraph = """Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human language. Applications of NLP include language translation, sentiment analysis, and chatbots."""

sentences = nltk.sent_tokenize(paragraph)

words = nltk.word_tokenize(paragraph)

print(words)
print("len of words",len(words))







