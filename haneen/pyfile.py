import nltk
nltk.download('punkt')
file2 = open('HP Lovecraft’s Beyond the Wall of Sleep.txt', 'rt', encoding="utf8")
text = file2.read()
file2.close()



from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

tokens = [w.lower() for w in tokens]

import nltk
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]


words = [word for word in stripped if word.isalpha()]



nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]


file2 = open('Jane-Austin’s-Pride-and-Prejudice.txt', 'rt', encoding="utf8")
text = file2.read()
file2.read()
file2.close()



from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

tokens = [w.lower() for w in tokens]

import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

m = [word for word in stripped if word.isalpha()]






from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
m = [w for w in m if not w in stop_words]



import numpy as np
arr=np.array([])
tt=np.intersect1d(m,words)
print(tt)
len(tt)