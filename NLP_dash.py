import pandas as pd
from nsetools import Nse
import yahoo_fin.stock_info as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from nse_stock_search import stock_top_gainers
import requests
from bs4 import BeautifulSoup

import dash
import dash_html_components as html

import spacy
from spacy.displacy.render import DEFAULT_LABEL_COLORS


# Initialize the application
app = dash.Dash(__name__)


def entname(name):
    return html.Span(name, style={
        "font-size": "0.8em",
        "font-weight": "bold",
        "line-height": "1",
        "border-radius": "0.35em",
        "text-transform": "uppercase",
        "vertical-align": "middle",
        "margin-left": "0.5rem"
    })


def entbox(children, color):
    return html.Mark(children, style={
        "background": color,
        "padding": "0.45em 0.6em",
        "margin": "0 0.25em",
        "line-height": "1",
        "border-radius": "0.35em",
    })


def entity(children, name):
    if type(children) is str:
        children = [children]

    children.append(entname(name))
    color = DEFAULT_LABEL_COLORS[name]
    return entbox(children, color)


def render(doc):
    children = []
    last_idx = 0
    for ent in doc.ents:
        children.append(doc.text[last_idx:ent.start_char])
        children.append(
            entity(doc.text[ent.start_char:ent.end_char], ent.label_))
        last_idx = ent.end_char
    children.append(doc.text[last_idx:])
    return children

def extract_text_from_rss(rss_link):
    """
    Parses the XML and extracts the headings from the
    links in a python list.
    """
    headings = []

    # r1 = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    r2 = requests.get(rss_link)
    # soup1 = BeautifulSoup(r1.content, features='lxml')
    soup2 = BeautifulSoup(r2.content, features='lxml')
    # headings1 = soup1.findAll('title')
    headings2 = (soup2.findAll('title'))
    print(headings2)
    # headings = headings1 + headings2
    headings=headings2

    return headings



# fin_headings = extract_text_from_rss(user_input)

text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Entities:", doc.ents)

# define de app
app.layout = html.Div(
    children=render(doc)
)

# app.layout = html.Div([
#     dcc.Textarea(
#         placeholder='Enter a value...',
#         value='This is a TextArea component',
#         style={'width': '100%'}
#     )
# ])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
