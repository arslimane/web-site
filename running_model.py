import pickle
import re
import qalsadi.lemmatizer
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from nltk.tokenize import RegexpTokenizer
lemmer = qalsadi.lemmatizer.Lemmatizer()
import asyncio

stopwordsfile = 'stopwords.txt'
with open(stopwordsfile, encoding="utf8") as f:
    stwords = f.readlines()
i = 0

for word in stwords:
    stwords[i] = word.replace("\n", "")
    i = i+1

f = open('svmmodel.pickle', 'rb')
nb = pickle.load(f)
f.close()


def pre1(x):
  tokenizer = RegexpTokenizer(r'\w+')
  f = tokenizer.tokenize(x)
  resultwords = [word for word in f if word not in stwords and  len(word)<=11]
  if(len(resultwords)!=0):
       result = ' '.join(resultwords)
       text_nonum = re.sub(r'\d+', '', result)
       text_no_doublespace = re.sub('\s+', ' ', text_nonum).strip()
       return text_no_doublespace
  else: return ""

my_tags=["Negative","Neutral","Positive"]

async def p(lemmas):
    print('in coroutine')
    words=[]
    for j in lemmas:
        if (type(j) is tuple):
                if (j[1] != "stopword" and j[1] != "all"):
                         words.append(j[0])
    return words
    


def predict(x):
    y=nb.predict([x]) 
    return my_tags[y[0]]

async def lemx(x):
    print('in coroutine')
    return lemmer.lemmatize_text(x, return_pos=True)


