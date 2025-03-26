import dash
from dash import dcc, html
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd
import dash
from dash.dependencies import Input, Output
import time

# Create the Dash app
app = dash.Dash(__name__)

# Stock ticker to monitor
stock_symbol = "AAPL"

# Set up the layout of the app
app.layout = html.Div([
    html.H1(f'Real-Time Stock Chart for {stock_symbol}'),
    dcc.Graph(id='live-stock-chart'),
    dcc.Interval(
        id='interval-component',
        interval=60000,  # Update every 60 seconds
        n_intervals=0
    )
])

# Function to fetch stock data
def get_stock_data(ticker):
    data = yf.download(ticker, period='1d', interval='1m')  # 1 minute interval
    return data

# Function to update the chart
@app.callback(
    Output('live-stock-chart', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Get the latest stock data
    df = get_stock_data(stock_symbol)

    # Create the figure
    figure = {
        'data': [
            go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color='green',
                decreasing_line_color='red',
            )
        ],
        'layout': go.Layout(
            title=f'{stock_symbol} Real-Time Stock Price',
            xaxis={'rangeslider': {'visible': False}},
            yaxis={'title': 'Stock Price (USD)'},
            showlegend=False,
            plot_bgcolor='rgb(18, 18, 18)',
            paper_bgcolor='rgb(18, 18, 18)',
            font={'color': 'white'},
        )
    }
    return figure

# Run the app
if __name__ == '__main__':
    app.run(debug=True)