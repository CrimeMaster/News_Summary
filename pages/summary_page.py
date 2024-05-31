import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from NewSummary import allNews
from Text_Summarization import summarizer


def show_summary_page():
    # Create a text input box for the URL
    url = st.text_input('Enter the URL')

    # Create a button for the search action
    if st.button('Search'):
        try:
            news_title, news = allNews(url)
            summary, doc, scores_df, len_doc, lens_summary = summarizer(news)
            st.title(news_title)
            st.write(summary)
            
            # dataframe to display with total number of sentences and thier 
            #respective scores
            st.dataframe(scores_df)
            

        except Exception as e:
            st.write(f"An error occurred: {e}")

        