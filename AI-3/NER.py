import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Shridhar want to buy Apple phone in India on 5 Jan 2022." 

# Process the text
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    print(ent.text, "→", ent.label_)
