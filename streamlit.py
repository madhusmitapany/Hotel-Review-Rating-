import pandas as pd
import streamlit as st 
from pickle import load
from sklearn import svm

st.title('Hotel Sentiment Classifier')
st.header('Text')
Str = st.text_input('Plese write your Review')
st.sidebar.header('Description')
st.sidebar.write( ' This web application is designed specifically for hotel review analysis.' )
st.sidebar.write('It can tell you about the sentiment behind the hotel reviews that are posted by travelers.')
st.sidebar.subheader('Instructions')
st.sidebar.write("Simply write or copy-paste the review in the 'Text' column and hit 'Get Sentiment' to see if the review is - Positive, Neutral or Negative.")
review = [(Str)]
def sentiment(score):
    if pred == 0:
        return 'Neutral'
    elif pred == 1:
        return 'Negative'
    else:
        return 'Positive'

model = load(open('svm_sav', 'rb'))
pred = model.predict(review)
prediction = sentiment(pred)
button = st.button('Get Sentiment')
x = st.write(prediction)