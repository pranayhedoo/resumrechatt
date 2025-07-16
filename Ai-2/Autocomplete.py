from nltk import bigrams
from collections import defaultdict, Counter

corpus = "I love natural language processing and machine learning.".lower().split()
bigram_counts = defaultdict(Counter)

for w1, w2 in bigrams(corpus):
    bigram_counts[w1][w2] += 1

prev_word = "love"
if prev_word in bigram_counts:
    next_word = max(bigram_counts[prev_word], key=bigram_counts[prev_word].get)
    print(f"Autocomplete suggestion: {prev_word} {next_word}")
else:
    print("No suggestion available.")
