import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import requests
# import streamlit as st

def balance_sheet_extraction(index_symbol):
    url_is = 'https://finance.yahoo.com/quote/' + index_symbol + '/financials?p=' + index_symbol
    try:
        response = requests.get(url_is, headers={'User-Agent': 'Mozilla/5.0'})
        print(response)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

    soup_is = BeautifulSoup(response.content, 'lxml')

    ls = []  # Create empty list
    for l in soup_is.find_all('div'):

        # Find all data structure that is 'div'
        ls.append(l.string)  # add each element one by one to the list

    ls = [e for e in ls if e not in ('Operating Expenses', 'Non-recurring Events')]  # Exclude those columns
    # print(ls)

    new_ls = list(filter(None, ls))
    # print(new_ls)

    new_ls = new_ls[12:]
    print(new_ls)

    is_data = list(zip(*[iter(new_ls)] * 6))
    Income_st_df = pd.DataFrame(is_data[0:])
    print(Income_st_df)
    getTicker('Wipro')
    return Income_st_df


def getTicker (company_name):
    url = "https://s.yimg.com/aq/autoc"
    parameters = {'query': company_name, 'lang': 'en-US'}
    response = requests.get(url = url, params = parameters)
    data = response.json()
    company_code = data['ResultSet']['Result'][0]['symbol']
    return company_code


if __name__ == '__main__':
    balance_sheet_extraction('MSFT')
    # index_sym=st.textbox('insert the stock index symbol')
