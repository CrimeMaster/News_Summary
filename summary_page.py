import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from NewSummary import allNews
from Text_Summarization import summarizer


def show_summary_page():

    # Create a text input box for the URL
    url = st.text_input('Enter the URL')
    summary_len = st.slider("Enter Number of Words :", 100, 1500, 100)
    
    # Create a button for the search action
    if st.button('Search'):
        try:
            news_title, news = allNews(url)
            summary, doc, scores_df, len_doc, lens_summary = summarizer(news, summary_len)
            
            
            st.title(news_title)
            st.write(summary)
            st.write("Length of Summary ", lens_summary)
            #st.write(words)

            # dataframe to display with total number of sentences and thier 
            #respective scores
            st.dataframe(scores_df)

            return scores_df
         

        except Exception as e:
            st.write(f"An error occurred: {e}")

