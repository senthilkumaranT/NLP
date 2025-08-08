import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Print available pipeline components
print("Available pipeline components:", nlp.pipe_names)

# Sample text for NER
text = "My name is John Doe. I live in New York City and work for Google. Last week, I visited the Statue of Liberty with my friend Sarah."

# Process the text
doc = nlp(text)

print(f"\nNamed Entities found in: '{text}'\n")
print("Entity Text | Label | Description")
print("-" * 50)

for ent in doc.ents:
    # Get the explanation for the entity label
    explanation = spacy.explain(ent.label)
    
    # Handle cases where explanation is None
    if explanation is None:
        explanation = f"Unknown label: {ent.label}"
    
    print(f"{ent.text:<20} | {ent.label:<5} | {explanation}")

print(f"\nTotal entities found: {len(doc.ents)}")

# Additional analysis - show all tokens with their POS tags
print(f"\nDetailed token analysis:")
print("Token | POS | Tag | Dep | Is Entity")
print("-" * 50)

for token in doc:
    is_entity = "Yes" if token.ent_type_ else "No"
    print(f"{token.text:<15} | {token.pos_:<4} | {token.tag_:<4} | {token.dep_:<4} | {is_entity}")