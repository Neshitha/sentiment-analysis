from transformers import pipeline
import streamlit as st 

pipe = pipeline('text-classification') 


st.title("sentiment analysis")

txt_input = st.text_input("Enter the text")

if st.button("Prediction"):
    if txt_input:
        output = pipe(txt_input)
        
        st.write("sentiment analysis",output)