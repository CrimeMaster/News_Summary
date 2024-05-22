import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from NewSummary import allNews
from Text_Summarization import summarizer

st.title("News Summary")

# Create a text input box for the URL
url = st.text_input('Enter the URL')

# Create a button for the search action
if st.button('Search'):
    try:
        news_title, news = allNews(url)
        summary, doc, len_doc, lens_summary = summarizer(news)
        st.title(news_title)
        st.write(summary)
    except Exception as e:
        st.write(f"An error occurred: {e}")
