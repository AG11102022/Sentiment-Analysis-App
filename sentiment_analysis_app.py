import streamlit as st
from transformers import pipeline

st.title('Sentiment Analysis App')

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline('sentiment-analysis')

model = load_model()

user_input = st.text_area("Enter text to analyze")

if st.button('Analyze'):
    result = model(user_input)
    st.write(result)
