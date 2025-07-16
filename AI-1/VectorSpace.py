# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# sentences = ["I love data science", "I enjoy learning data"]
# vectorizer = CountVectorizer()
# vectors = vectorizer.fit_transform(sentences)
# similarity = cosine_similarity(vectors[0], vectors[1])
# print("Cosine Similarity:", similarity[0][0])

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # New sentences
# sentences = ["Artificial intelligence is fascinating", "Machine learning is a part of AI"]

# vectorizer = CountVectorizer()
# vectors = vectorizer.fit_transform(sentences)

# similarity = cosine_similarity(vectors[0], vectors[1])
# print("Cosine Similarity:", similarity[0][0])

# from transformers import pipeline

# # Example: Sentiment analysis
# classifier = pipeline("sentiment-analysis")
# result = classifier("I love using transformers library!")
# print(result)

# from transformers import pipeline

# classifier = pipeline("sentiment-analysis")
# print(classifier("Transformers in VS Code is awesome!"))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
sentences = ["Machine learning is amazing", "Deep learning is a part of AI"]
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentences)
similarity = cosine_similarity(vectors[0], vectors[1])
print("Cosine Similarity:", similarity[0][0])