import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup

# importing nse from nse tools
from nsetools import Nse

nse = Nse()


def stock_top_gainers():
    top_gainers_json_list=nse.get_top_fno_gainers()
    dfItem = pd.DataFrame.from_records(top_gainers_json_list)
    return dfItem

st.title('Financial Dashboard')
ticker_input = st.text_input('Please enter your company ticker:')
search_button = st.button('Search')


def global_stock_analysis():
    response = requests.get('https://www.moneycontrol.com/markets/global-indices/')
    page_content = BeautifulSoup(response.content, "html.parser")
    st.text(page_content)



top_gain_df=stock_top_gainers()
st.dataframe(top_gain_df)
global_stock_analysis()