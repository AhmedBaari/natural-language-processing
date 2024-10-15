# Credit: Raghavender
#Exp2: chisquare test
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from nltk.corpus import stopwords
import string
stop_words=set(stopwords.words('english'))

def bigram_fun(bigram_count,sentence):
    sentence=sentence.lower()
    tokens=word_tokenize(sentence)
    tokens_new=[token for token in tokens if token not in stop_words and token not in string.punctuation]
    bigram_list=list(bigrams(tokens_new))
    for bigram in bigram_list:
        bigram_count[bigram]=bigram_count.get(bigram,0)+1
        
sentences = [
    "I love studying data science.",
    "Data science is an interesting field.",
    "Science requires data for analysis.",
    "Data is key in modern science.",
    "Data science helps in business decision-making."
]

bigram_count={}
for sentence in sentences:
    bigram_fun(bigram_count,sentence)

word1=input("Enter the word1:")
word2=input("Enter the word2:")
# contingency matrix
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Updating contingency matrix based on word1 and word2
for units in bigram_count:
    if units[0] == word1 and units[1] == word2:
        C[0][0] += bigram_count[units]  # word1 and word2
    elif units[0] == word1 and units[1] != word2:
        C[0][1] += bigram_count[units]  # word1 and not word2
    elif units[0] != word1 and units[1] == word2:
        C[1][0] += bigram_count[units]  # not word1 and word2
    else:
        C[1][1] += bigram_count[units]  # not word1 and not word2

# total matrix
# Updating contingency matrix based on word1 and word2
C[0][2] = C[0][0] + C[0][1]  
C[1][2] = C[1][0] + C[1][1] 
C[2][0] = C[0][0] + C[1][0]  
C[2][1] = C[0][1] + C[1][1] 
tot = C[2][0] + C[2][1]

print("Contingency matrix:")
for row in C:
    print(" ".join(str(val) for val in row))

# expected matrix
E = [[0, 0], [0, 0]]

# Calculate expected values based on contingency matrix and total occurrences
E[0][0] = (C[0][2] * C[2][0]) / tot  # expected occurrences of word1 and word2
E[0][1] = (C[0][2] * C[2][1]) / tot  # expected occurrences of word1 and not word2
E[1][0] = (C[1][2] * C[2][0]) / tot  # expected occurrences of not word1 and word2
E[1][1] = (C[1][2] * C[2][1]) / tot  # expected occurrences of neither word1 nor word2

print("Expected matrix:")
for row in E:
    print(" ".join(f"{val:.2f}" for val in row))

obs_mat = [C[0][0], C[0][1], C[1][0], C[1][1]]
exp_mat = [E[0][0], E[0][1], E[1][0], E[1][1]]

chi2test=0
for i in range(4):
    chi2test+=(obs_mat[i]-exp_mat[i])**2/exp_mat[i] #summation of O-E whole square by E

cric_val=float(input("Enter critical value:"))

if(chi2test>cric_val):
    print("Reject H0")
else:
    print("Accept H0")

