import dash
from dash import dcc, html
import yfinance as yf
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)


# Function to fetch stock data for the past 1 year
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    return data


# Function to calculate daily percentage change
def calculate_percentage_change(data):
    data['Pct_Change'] = data['Close'].pct_change() * 100
    data = data.dropna(subset=['Pct_Change'])
    return data


# Ticker symbols
wipro_ticker = "WIPRO.NS"
persistent_ticker = "PERSISTENT.NS"
icici_ticker = "ICICIBANK.NS"
hdfc_ticker = "HDFCBANK.NS"
krn_ticker = "KRN.NS"

# App layout
app.layout = html.Div(
    style={'height': '100vh', 'backgroundColor': '#1e1e1e'},
    children=[
        html.H1("Stock Price Percentage Change (Last 1 Year)",
                style={'textAlign': 'center', 'color': 'white'}),

        dcc.Graph(
            id='stock-price-graph',
            style={'height': '100vh'},  # Full-height graph
            config={
                'scrollZoom': True,  # Allow scrolling to zoom
                'displayModeBar': True,
                'displaylogo': False
            }
        )
    ]
)


# Callback to update graph
@app.callback(
    dash.dependencies.Output('stock-price-graph', 'figure'),
    [dash.dependencies.Input('stock-price-graph', 'id')]
)
def update_graph(_):
    # Fetch and process stock data
    wipro_data = calculate_percentage_change(get_stock_data(wipro_ticker))
    persistent_data = calculate_percentage_change(get_stock_data(persistent_ticker))
    icici_data = calculate_percentage_change(get_stock_data(icici_ticker))
    hdfc_data = calculate_percentage_change(get_stock_data(hdfc_ticker))
    krn_data = calculate_percentage_change(get_stock_data(krn_ticker))

    # Create the figure
    figure = {
        'data': [
            # Wipro
            go.Scatter(x=wipro_data.index, y=wipro_data['Pct_Change'], mode='lines',
                       name='Wipro', line={'color': 'blue'}),

            # Persistent
            go.Scatter(x=persistent_data.index, y=persistent_data['Pct_Change'], mode='lines',
                       name='Persistent', line={'color': 'red'}),

            # ICICI
            go.Scatter(x=icici_data.index, y=icici_data['Pct_Change'], mode='lines',
                       name='ICICI Bank', line={'color': 'green'}),

            # HDFC
            go.Scatter(x=hdfc_data.index, y=hdfc_data['Pct_Change'], mode='lines',
                       name='HDFC Bank', line={'color': 'pink'}),

            # KRN Heatexchanger
            go.Scatter(x=krn_data.index, y=krn_data['Pct_Change'], mode='lines',
                       name='KRN Heatexchanger', line={'color': 'yellow'}),
        ],
        'layout': go.Layout(
            title="Stock Price Percentage Change (Last 1 Year)",
            xaxis={
                'title': 'Date',
                'rangeslider': {'visible': True},  # Add a range slider for x-axis
                'showgrid': False,
                'color': 'white'
            },
            yaxis={
                'title': 'Percentage Change (%)',
                'fixedrange': False,  # Enable dynamic zooming along the y-axis
                'showgrid': True,
                'color': 'white'
            },
            dragmode='pan',  # Enable panning
            plot_bgcolor='#2e2e2e',
            paper_bgcolor='#1e1e1e',
            font={'color': 'white'}
        )
    }
    return figure


# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
