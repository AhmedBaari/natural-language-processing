#Exp 2: ttest
import pandas as pd
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import bigrams


def unigram_fun(sentence):
    sentence=sentence.lower()
    tokens=word_tokenize(sentence)
    token_1=[token for token in tokens if token not in string.punctuation and token not in stop_words]
    return token_1

def bigram_fun(sentence):
    sentence=sentence.lower()
    tokens=word_tokenize(sentence)
    token_1=[token for token in tokens if token not in string.punctuation and token not in stop_words]
    bigram_list=list(bigrams(token_1))
    return bigram_list


df=pd.read_csv('sastralines.csv')
df_new = df.iloc[:,0]
df_new_list = df_new.tolist()
stop_words=set(stopwords.words('english'))
unigrams=[unigram_fun(sentence) for sentence in df_new_list]
bigrams=[bigram_fun(sentence) for sentence in df_new_list]
print(df_new_list)

#Calculaing the length of the corpus
N=0
for line in df_new_list:
    N=N+len(line)

print("The length of the corpus is:",N)


#unigram_dict
unigram_dict={}
for line in unigrams:
    for word in line:
        unigram_dict[word]=0
for line in unigrams:
    for word in line:
        unigram_dict[word]=unigram_dict[word]+1

#bigram_dict
bigram_dict={}
for line in bigrams:
    for word in line:
        bigram_dict[word]=0
for line in bigrams:
    for word in line:
        bigram_dict[word]=bigram_dict[word]+1


a=input("Enter the 1st word:")
b=input("Enter the 2nd word:")
cv=float(input("Enter the critical value:"))

#observerd mean
O=(bigram_dict[(a,b)]/N) 

#Expected mean
E=((unigram_dict[a]/N)*(unigram_dict[b]/N))

#variance
variance=E

ttest = (O-E)/np.sqrt((variance/N))
print(ttest)

if(ttest<cv):
    print("Accept H0")
else:
    print("Reject H0")

# Credit: Raghavender