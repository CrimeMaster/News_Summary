import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from summary_page import show_summary_page

page = st.sidebar.selectbox("Summary Or Analyse", ("Summary", "Analyse"))


st.title("News Summary")

if page == "Summary":
    show_summary_page()