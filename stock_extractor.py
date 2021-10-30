import spacy
import pandas as pd
from nsetools import Nse
import requests
from bs4 import BeautifulSoup

nse = Nse()


def stock_top_gainers():
    """Extract top gainers """
    top_gainers_json_list=nse.get_top_fno_gainers()
    dfItem = pd.DataFrame.from_records(top_gainers_json_list)
    return dfItem

top_gainers=stock_top_gainers()
print(top_gainers)


rss_link="https://www.moneycontrol.com/rss/MCtopnews.xml"

def extract_text_from_rss(rss_link):
    """
    Parses the XML and extracts the headings from the
    links in a python list.
    """
    r2 = requests.get(rss_link)
    soup2 = BeautifulSoup(r2.content, features='lxml')
    headings = (soup2.findAll('title'))
    print(headings)
    return headings


heading=extract_text_from_rss(rss_link)
print(heading)
