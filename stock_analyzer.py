import pandas as pd
import requests
import spacy
import streamlit as st
from datetime import date
import spacy_streamlit
from spacy import displacy
from bs4 import BeautifulSoup
import yfinance as yf
import re
from datetime import datetime
import calendar

month_list = list(calendar.month_name)
week_list = list(calendar.day_name)
print(week_list)

# from spacy_streamlit import visualize_ner
# import matplotlib
import altair as alt

def text_cleaning(text):
    clean_text = re.sub('<[^<]+>', '', str(text))
    return clean_text

def text_cleansing(text):

    list_of_remove =['per cent','Losers','Gainers','Sensex','Nifty','week','US','Over']+month_list+week_list
    # clean_text = text.lower()
    clean_text = re.sub(r'[^a-zA-Z\s]', '', str(text), re.I | re.A)
    big_regex = re.compile('|'.join(map(re.escape, list_of_remove)))
    clean_text = big_regex.sub("", str(clean_text))
    clean_text=re.sub("\s.*",'',clean_text)
    return clean_text


## get data from RSS feed
def extract_text_from_rss(rss_link):
    """
    Parses the XML and extracts the headings from the
    links in a python list.
    """
    headings = []

    r1 = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    r2 = requests.get(rss_link)
    soup1 = BeautifulSoup(r1.content, features='lxml')
    soup2 = BeautifulSoup(r2.content, features='lxml')
    headings1 = soup1.findAll('title')
    headings2 = (soup2.findAll('title'))
    print(headings2)
    headings = headings1 + headings2
    return headings



def stock_info(headings):
    """
    Goes over each heading to find out the entities
    and link it with the nifty 500 companies data.
    Extracts the data
    """

    stocks_df = pd.read_csv("./stock_data/ind_nifty500list.csv")

    for title in headings:
        doc = nlp(title.text)

        for token in doc.ents:
            if token.label_ == "ORG":
                try:
                    if stocks_df['Company Name'].str.contains(token.text).sum():
                        symbol = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Symbol'].values[0]
                        org_name = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Company Name'].values[0]
                        token_dict['Org'].append(org_name)
                        print(symbol + ".NS")
                        token_dict['Symbol'].append(symbol)
                        stock_info = yf.Ticker(symbol + ".NS").info
                        token_dict['currentPrice'].append(stock_info['currentPrice'])
                        token_dict['dayHigh'].append(stock_info['dayHigh'])
                        token_dict['dayLow'].append(stock_info['dayLow'])
                        token_dict['forwardPE'].append(stock_info['forwardPE'])
                        token_dict['dividendYield'].append(stock_info['dividendYield'])
                    else:
                        pass
                except:
                    pass
    output_df = pd.DataFrame(token_dict)

    return output_df

# @st.cache(suppress_st_warning=True)
def stock_info_opt(headings):
    """
    Goes over each heading to find out the entities
    and link it with the nifty 500 companies data.
    Extracts the data
    """

    global output
    stocks_df = pd.read_csv("./stock_data/ind_nifty500list.csv")
    headings = [text_cleaning(i) for i in headings]
    print('\nHeadings\n',headings)

    for title in headings:
        doc = nlp(title)
        entities=text_cleansing(str(doc.ents))
        if entities:
            print('entity',entities,len(entities))
            if stocks_df['Company Name'].str.contains(entities).sum():
                try:
                    for token in doc.ents:
                        print('\nTOKEN\n',token)
                        symbol = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Symbol'].values[0]
                        org_name = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Company Name'].values[0]
                        token_dict['Org'].append(org_name)
                        print('\nSymbol\n',symbol + ".NS")
                        token_dict['Symbol'].append(symbol)
                        stock_info = yf.Ticker(symbol + ".NS").info
                        token_dict['currentPrice'].append(stock_info['currentPrice'])
                        token_dict['dayHigh'].append(stock_info['dayHigh'])
                        token_dict['dayLow'].append(stock_info['dayLow'])
                        token_dict['forwardPE'].append(stock_info['forwardPE'])
                        token_dict['dividendYield'].append(stock_info['dividendYield'])
                except:
                    pass
    output_df = pd.DataFrame(token_dict)
    print(output_df)

    return output_df


if __name__ == "__main__":

    token_dict = {
        'Org': [],
        'Symbol': [],
        'currentPrice': [],
        'dayHigh': [],
        'dayLow': [],
        'forwardPE': [],
        'dividendYield': []
    }
    nlp = spacy.load("en_core_web_sm")

    # st.title('Buzzing Stocks :zap:')
    today_date = date.today()

    ## add an input field to pass the RSS link
    # user_input = st.text_input("Add your RSS link here!", "https://www.moneycontrol.com/rss/buzzingstocks.xml")
    user_input="https://www.moneycontrol.com/rss/buzzingstocks.xml"

    ## get the financial  headings
    fin_headings = extract_text_from_rss(user_input)

    ## output the financial info through a dataframe
    output_df = stock_info_opt(fin_headings)
    output_df.drop_duplicates(inplace=True)
    # print(output_df)
    st.dataframe(output_df)
    d1 = today_date.strftime("%d/%m/%Y")

    # output_df.to_csv('./stock_data/stock_data.csv')
    chart = alt.Chart(output_df).mark_line().encode(
        x=alt.X('dayHigh:N'),
        y=alt.Y('currentPrice:Q'),
        color=alt.Color("Symbol:N")).properties(title="current_price").interactive()

    print('Chart',chart)
    st.altair_chart(chart.interactive(), use_container_width=True)
    st.line_chart(output_df['Symbol'].values,output_df['currentPrice'].values)

    # display the news in an expander section
    with st.expander("Expand for Financial News!"):
        for h in fin_headings:
            st.markdown("* " + h.text)

