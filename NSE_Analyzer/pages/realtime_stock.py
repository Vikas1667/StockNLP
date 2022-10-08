#Import the libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
# Data Source
import yfinance as yf

# Data viz
import plotly.graph_objs as go

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from nsepy import get_history
import datetime
from datetime import date
import streamlit as st
st.set_page_config(layout="wide")

if __name__ == "__main__":
    symbol = st.text_input("Enter symbol of stock\n")
    today = datetime.date.today()
    start_date = st.sidebar.date_input('Start date')
    end_date = st.sidebar.date_input('End date',today)

    # df = get_history(symbol=symbol, start=start_date, end=date.today())
    # st.table(df)
    # df['Date'] = df.index

    fig=plt.figure(figsize=(16,8))

    #title for the plot
    plt.title('Stocks Close Price Analysis')

    #interactive area plot with matplotlib
    # cols=df.columns.tolist()
    # x_axis = st.sidebar.selectbox("X-Axis", cols)
    # y_axis = st.sidebar.selectbox("Y-Axis", cols,index=1)
    #
    # if x_axis and y_axis:
    #     plt.fill_between(df[x_axis],df[y_axis], color="skyblue", alpha=0.2)
    #     plt.plot(df[x_axis], df[y_axis], color="skyblue", alpha=0.6)
    #
    #
    #     #x-axis and y-axis labels
    #     plt.xlabel('Time/Date',fontsize=18)
    #     plt.ylabel('Stock Close Price',fontsize=18)
    #
    #     st.pyplot(fig)


    # Interval required 1 minute
    data = yf.download(tickers=symbol, period='1d', interval='1m')

    # declare figure
    fig = go.Figure()

    # Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))

    # Add titles
    fig.update_layout(
        title='live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    # Show
    # st.pyplot(fig)
    fig.show()