# Baari
# OPTIMIZED
import pandas as pd
import string
import nltk
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict

# Load data
df = pd.read_csv("Bank.csv")
train_data = df.iloc[0:93, :]
test_data = df.iloc[94:, :]
stop_words = set(stopwords.words('english'))

# Initialize counters
fin_class = riv_class = 0
fin_word_freq = defaultdict(int)
riv_word_freq = defaultdict(int)

# Preprocess and count word occurrences per class
for _, row in train_data.iterrows():
    tokens = [word for word in word_tokenize(row['Sentence']) if word not in stop_words and word not in string.punctuation]
    
    if row['Class'] == 'Financial Institution':
        fin_class += 1
        for word in tokens:
            fin_word_freq[word] += 1
    elif row['Class'] == 'River Border':
        riv_class += 1
        for word in tokens:
            riv_word_freq[word] += 1

# Calculate prior probabilities
tot_class = fin_class + riv_class
prior_fin_class = math.log2(fin_class / tot_class)
prior_riv_class = math.log2(riv_class / tot_class)

# Vocabulary size
vocab = set(list(fin_word_freq.keys()) + list(riv_word_freq.keys()))
V = len(vocab)

# Test phase
for _, row in test_data.iterrows():
    tokens = [word for word in word_tokenize(row['Sentence']) if word not in stop_words and word not in string.punctuation]

    score_fin = prior_fin_class
    score_riv = prior_riv_class
    
    for word in tokens:
        score_fin += math.log2(fin_word_freq[word] + 1) - math.log2(fin_class + V)
        score_riv += math.log2(riv_word_freq[word] + 1) - math.log2(riv_class + V)

    print("Sense is Financial Institution" if score_fin > score_riv else "Sense is River Border")
