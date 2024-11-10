# Ahmed Baari 
# OPTIMIZED VERSION 
# WARNING: CHECK WITH VALID TESTCASES
import nltk
import math
import string
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams

# Input for preposition, noun, and verb
prep = input("Enter the preposition: ").lower()
noun = input("Enter the noun: ").lower()
verb = input("Enter the verb: ").lower()

# Stopwords and punctuation setup
stop_words = set(stopwords.words('english'))

# Using defaultdict to avoid manual key checking
unigram_dict = defaultdict(int)
bigram_dict = defaultdict(int)

# List of sentences to analyze
sentences = [
    "Saw the phone with me.",
    "Went to the meeting yesterday.",
    "Told the man to wait.",
    "Gave the book to her.",
    "Saw the cat with her."
]

# Processing each sentence
for sentence in sentences:
    tokens = word_tokenize(sentence)
    tokens_cleaned = [token.lower() for token in tokens if token not in string.punctuation]
    
    # Counting unigrams
    for word in tokens_cleaned:
        unigram_dict[word] += 1
    
    # Counting bigrams
    for bg in bigrams(tokens_cleaned):
        bigram_dict[bg] += 1

# Default values for unseen bigrams/unigrams
p_noun_prep = bigram_dict[(noun, prep)] / unigram_dict[noun] if unigram_dict[noun] != 0 else 0
p_verb_prep = bigram_dict[(verb, prep)] / unigram_dict[verb] if unigram_dict[verb] != 0 else 0
p_0_n = 1 - p_noun_prep

# Ensure that the log argument is valid
if p_noun_prep > 0 and p_verb_prep * p_0_n > 0:
    lammbda = math.log2((p_verb_prep * p_0_n) / p_noun_prep)
    print("Attached with Verb." if lammbda >= 0 else "Attached with Noun.")
else:
    print("No valid attachments.")
