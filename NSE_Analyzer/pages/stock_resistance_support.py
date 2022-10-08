import pandas as pd
import numpy as np
import yfinance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [56, 16]
plt.rc('font', size=14)

# from NSE_Analyzer.pages.technical_analysis import BollingerBands,RSIIndicator,MACD
import streamlit as st


def isSupport(df, i):
    support = df['Low'][i] < df['Low'][i - 1] < df['Low'][i - 2] and df['Low'][i] < df['Low'][i + 1] < df['Low'][i + 2]
    return support


def isResistance(df, i):
    resistance = df['High'][i] > df['High'][i - 1] > df['High'][i - 2] and df['High'][i] > df['High'][i + 1] > df['High'][i + 2]
    return resistance


def plot_all(df):
    levels = []
    fig, ax = plt.subplots()

    for i in range(2, len(df) - 2):
        print(i, len(df))
        if isSupport(df, i):
            levels.append((i, df['Low'][i]))
        elif isResistance(df, i):
            levels.append((i, df['High'][i]))

    candlestick_ohlc(ax, df.values, width=0.05, colorup='green', colordown='red', alpha=0.8)
    date_format = mpl_dates.DateFormatter('%d %b %Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()

    for level in levels:
        plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='blue',
                   label='support_and_resistance')
    st.pyplot(fig)


if __name__ == '__main__':
    st.title('STOCK Daily analysis')
    # with st.expander("How to start ewith python")
    ticker_sym = st.text_input('Insert the Ticker sysmbol')
    start_date = st.date_input('start date')
    end_date = st.date_input('end date')
    ticker = yfinance.Ticker(ticker_sym)
    df = ticker.history(interval="1h", start=start_date, end=end_date)
    print(df)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    # st.table(df)
    plot_all(df)

    option_df = yfinance.download(ticker_sym, start=start_date, end=end_date, interval='5m', progress=False)

    # # Bollinger Bands
    # indicator_bb = BollingerBands(df['Close'])
    # bb = df
    # bb['bb_h'] = indicator_bb.bollinger_hband()
    # bb['bb_l'] = indicator_bb.bollinger_lband()
    # bb = bb[['Close', 'bb_h', 'bb_l']]
    # st.write('Stock Bollinger Bands')
    # st.line_chart(bb)
    # macd = MACD(df['Close']).macd()
    #
    # progress_bar = st.progress(0)
    #
    # rsi = RSIIndicator(df['Close']).rsi()
    #
    # # Plot MACD
    # st.write('Stock Moving Average Convergence Divergence (MACD)')
    # st.area_chart(macd)
    #
    # # Plot RSI
    # st.write('Stock RSI ')
    # st.line_chart(rsi)
    #
    # # Data of recent days
    # st.write('Recent data ')
    # st.dataframe(df.tail(10))
    #
