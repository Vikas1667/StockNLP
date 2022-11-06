import pandas as pd
import numpy as np
import yfinance
import  streamlit as st
from mpl_finance import candlestick_ohlc
from sklearn.cluster import KMeans
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go


ticker_sym = st.text_input('Insert the Ticker sysmbol')
start_date = st.date_input('start date')
end_date = st.date_input('end date')

ticker = yfinance.Ticker(ticker_sym)
df = ticker.history(interval="1h", start=start_date, end=end_date)

df['Date'] = pd.to_datetime(df.index)
df['Date'] = df['Date'].apply(mpl_dates.date2num)
df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
# st.table(df)

#### Kmeans
# st.table(df)
# Convert adjusted closing price to numpy array
btc_prices = np.array(df["Close"])
# st.write("BTC Prices:\n",btc_prices)

# Perform cluster analysis
K = 5
kmeans = KMeans(n_clusters=5).fit(btc_prices.reshape(-1, 1))
# predict which cluster each price is in
clusters = kmeans.predict(btc_prices.reshape(-1, 1))
print("Clusters:\n", clusters)
# st.write(clusters)

if st.button('Cluster_plot'):
    # Assigns plotly as visualization engine
    pd.options.plotting.backend = 'plotly'
    # Arbitrarily 6 colors for our 6 clusters
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
    # Create Scatter plot, assigning each point a color based
    # on it's grouping where group_number == index of color.
    fig = df.plot.scatter(
        x=df.index,
        y="Close",
        color=[colors[i] for i in clusters],
    )
    # Configure some styles
    layout = go.Layout(
        plot_bgcolor='#efefef',
        showlegend=False,
        font_family='Monospace',
        font_color='#000000',
        font_size=20,
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ))
    )
    fig.update_layout(layout)

    # Display plot in local browser window
    fig.show()


###########
if st.button('Cluster minimum and max values'):
    # Create list to hold values, initialized with infinite values
    min_max_values = []
    for i in range(6):
        # Add values for which no price could be greater or less
        min_max_values.append([np.inf, -np.inf])
    # Print initial values
    print(min_max_values)
    # Get min/max for each cluster
    for i in range(len(btc_prices)):
        # Get cluster assigned to price
        cluster = clusters[i]
        # Compare for min value
        if btc_prices[i] < min_max_values[cluster][0]:
            min_max_values[cluster][0] = btc_prices[i]
        # Compare for max value
        if btc_prices[i] > min_max_values[cluster][1]:
            min_max_values[cluster][1] = btc_prices[i]
    # Print resulting values
    print(min_max_values)

    # Again, assign an arbitrary color to each of the 6 clusters
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
    # Create Scatter plot, assigning each point a color where
    # point group = color index.
    fig = df.plot.scatter(
        x=df.index,
        y="Close",
        color=[colors[i] for i in clusters],
    )
    # Add horizontal lines
    for cluster_min, cluster_max in min_max_values:
        fig.add_hline(y=cluster_min, line_width=1, line_color="blue")
        fig.add_hline(y=cluster_max, line_width=1, line_color="blue")
    # Add a trace of the price for better clarity
    fig.add_trace(go.Trace(
        x=df.index,
        y=df['Close'],
        line_color="black",
        line_width=1
    ))
    # Make it pretty
    layout = go.Layout(
        plot_bgcolor='#efefef',
        showlegend=False,
        # Font Families
        font_family='Monospace',
        font_color='#000000',
        font_size=20,
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ))
    )

    fig.update_layout(layout)
    fig.show()

if st.button('Consolidating Boundry lines'):
    print("Initial Min/Max Values:\n", min_max_values)
    # Create container for combined values
    output = []
    # Sort based on cluster minimum
    s = sorted(min_max_values, key=lambda x: x[0])
    # For each cluster get average of
    for i, (_min, _max) in enumerate(s):
        # Append min from first cluster
        if i == 0:
            output.append(_min)
        # Append max from last cluster
        if i == len(min_max_values) - 1:
            output.append(_max)
        # Append average from cluster and adjacent for all others
        else:
            output.append(sum([_max, s[i+1][0]]) / 2)
    print("Sorted Min/Max Values:\n", output)

    # Add horizontal lines
    for cluster_avg in output[1:-1]:
        fig.add_hline(y=cluster_avg, line_width=1, line_color="blue")

    fig.update_layout(layout)
    fig.show()

if st.button('Determine right clusters'):
    ###Determining the Right Number of Clusters
    # create a list to contain output values
    values = []
    # Define a range of cluster values to assess
    K = range(1, 10)
    # Performa a clustering using each value, save inertia_ value from each
    for k in K:
        kmeans_n = KMeans(n_clusters=k)
        kmeans_n.fit(btc_prices.reshape(-1, 1))
        values.append(kmeans_n.inertia_)

    # Create initial figure
    fig = go.Figure()
    # Add line plot of inertia values
    fig.add_trace(go.Trace(
        x=list(K),
        y=values,
        line_color="black",
        line_width=1
    ))
    # Make it pretty
    layout = go.Layout(
        plot_bgcolor='#efefef',
        showlegend=False,
        # Font Families
        font_family='Monospace',
        font_color='#000000',
        font_size=20,
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ))
    )
    fig.update_layout(layout)
    fig.show()
    st.pyplot(fig)
