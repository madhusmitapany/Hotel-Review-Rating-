from multiprocessing.spawn import import_main_path


import pandas as pd
import numpy as np
import pickle
from pickle import dump
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import svm
data = pd.read_excel('D:\hotel_reviews.xlsx')
def rating_analysis(rating):
  if rating < 3:
    return 1
  elif rating == 3:
    return 0
  else:
    return 2
data['Sentiment'] = data['Rating'].apply(rating_analysis)
x_train, x_test, y_train, y_test = train_test_split(data['Review'], data['Sentiment'], 
                                                    stratify= data['Sentiment'], test_size=0.20, random_state = 24)
svm = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', svm.LinearSVC())])
svm.fit(x_train, y_train)
#dump(svm,open('svm_sav','wb'))
print(svm.predict('Hotel was good'))
