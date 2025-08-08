import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Elon flew to Mars yesterday. He carries biryani masala with him.")

for token in doc:
    print(token, "!", token.pos_ ,token.tag_ ,spacy.explain(token.pos_))