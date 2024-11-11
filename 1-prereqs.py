import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

#tokenize
sentence = "SASTRA University is a great place. It has amazing facilities!"
words=nltk.word_tokenize(sentence)
print(words)

#stopwords removal
stop_words = set(stopwords.words('english'))
words_1=[word for word in words if word not in stop_words]
print(words_1)

#punctuation removal
words_2= [word for word in words_1 if word not in string.punctuation]
print(words_2)

# stemming
stemmer = PorterStemmer()
words_3 = [stemmer.stem(word) for word in words_2]
print(words_3)

# lemmatization
lemmatizer = WordNetLemmatizer()
words_4 = [lemmatizer.lemmatize(word) for word in words_3]
print(words_4)