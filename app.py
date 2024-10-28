import streamlit as st
import yfinance as yf
from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# CSS styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Define stock options with original company names
company_names = {
    'Adobe': 'ADBE',
    'Amazon': 'AMZN',
    'American Express': 'AXP',
    'Apple': 'AAPL',
    'Asian Paints': 'ASIANPAINT.NS',
    'Axis Bank': 'AXISBANK.NS',
    'Bajaj Finance': 'BAJFINANCE.NS',
    'Bank of America': 'BAC',
    'Berkshire Hathaway': 'BRK-B',
    'Bharti Airtel': 'BHARTIARTL.NS',
    'Cisco': 'CSCO',
    'Coca-Cola': 'KO',
    'Colgate-Palmolive': 'CL',
    'Disney': 'DIS',
    'Facebook (Meta)': 'FB',
    'Ford': 'F',
    'General Electric': 'GE',
    'General Motors': 'GM',
    'Goldman Sachs': 'GS',
    'Google': 'GOOGL',
    'HCL Technologies': 'HCLTECH.NS',
    'HDFC Bank': 'HDFCBANK.NS',
    'Hero MotoCorp': 'HEROMOTOCO.NS',
    'Hindustan Unilever': 'HINDUNILVR.NS',
    'Honda': 'HMC',
    'ICICI Bank': 'ICICIBANK.NS',
    'Indian Oil Corporation': 'IOC.NS',
    'Infosys': 'INFY',
    'ITC': 'ITC.NS',
    'Johnson & Johnson': 'JNJ',
    'JPMorgan Chase': 'JPM',
    'Larsen & Toubro': 'LT.NS',
    'Mahindra & Mahindra': 'M&M.NS',
    'Maruti Suzuki': 'MARUTI.NS',
    'Mastercard': 'MA',
    'McDonald\'s': 'MCD',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Oracle': 'ORCL',
    'PepsiCo': 'PEP',
    'Pfizer': 'PFE',
    'Procter & Gamble': 'PG',
    'Reliance Industries': 'RELIANCE.NS',
    'Samsung Electronics': '005930.KS',
    'Siemens': 'SIEGY',
    'Sony': 'SONY',
    'State Bank of India': 'SBIN.NS',
    'Sun Pharmaceutical': 'SUNPHARMA.NS',
    'Tata Consultancy Services': 'TCS.NS',
    'Tata Motors': 'TATAMOTORS.NS',
    'Tesla': 'TSLA',
    'Toyota': 'TM',
    'Unilever': 'UL',
    'Visa': 'V',
    'Vodafone Idea': 'IDEA.NS',
    'Walmart': 'WMT',
    'Wipro': 'WIPRO.NS',
    'Zoom Video': 'ZM'
}


# Sidebar options
# st.sidebar.header('> Stock Price Prediction App <')
# Add a styled header with custom color

# st.sidebar.markdown('<h2 style="color: #007B00; text-align: left; font-weight: bold; text-transform: uppercase;">STOCK PRICE PREDICTION APP</h2>', unsafe_allow_html=True)

st.sidebar.markdown(
    '''
    <h2 style="
        color: #000000;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 29px;
        font-family: 'Roboto', sans-serif;
        margin-bottom: 10px;
    ">
        STOCK PRICE PREDICTION
    </h2>
    ''',
    unsafe_allow_html=True
)




# Add an icon image at the top of the sidebar
st.sidebar.image("icon1.png", use_column_width=True)
stock_options = st.sidebar.selectbox('Select a Stock', [''] + sorted(company_names.keys()))
historical_years = st.sidebar.slider('Select Historical Data Years', 1, 10)
selected_interval = st.sidebar.selectbox('Select Data Interval', ['1d', '1wk', '1mo'])
prediction_years = st.sidebar.slider('Select Number of Years to Predict', 1, 5)

# Sidebar footer with contact details and icons
st.sidebar.markdown('''
---
<div style="text-align: center;">
    Created with ❤️ and late-night ideas 💡 by <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/" target="_blank">Abhishek KK</a>
</div>
<div style="text-align: center; margin-top: 10px;">
    <h4 style="color: #999; opacity: 2;">Connect with Me</h4>
<div style="text-align: center; margin-top: 10px;">
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="margin-right: 10px;">
    </a>
    <a href="https://github.com/kk-abhishek" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="20" style="margin-right: 10px;">
    </a>
    <a href="mailto:kkabhishek100@gmail.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="20">
    </a>
</div>
''', unsafe_allow_html=True)

# Only continue if a stock is selected
if stock_options:
    # Fetch the stock symbol
    stock_symbol = company_names[stock_options]
    
    # Fetch historical data with selected interval
    data = yf.download(stock_symbol, period=f'{historical_years}y', interval=selected_interval)

    # Check for sufficient data
    if data.dropna().shape[0] < 2:
        st.warning("Insufficient data for the selected period and interval. Try selecting a shorter period or a broader interval.")
    else:
        # Prepare data for Prophet
        df = data[['Close']].reset_index()
        df.columns = ['ds', 'y']
        df['ds'] = pd.to_datetime(df['ds']).dt.date

        # Prophet model setup and forecast
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=prediction_years * 365)
        future['ds'] = pd.to_datetime(future['ds']).dt.date
        forecast = model.predict(future)

        # Rename columns for readability and styling forecast table
        forecast.rename(columns={
            'ds': 'Date',
            'yhat': 'Predicted Stock Price ($)',
            'yhat_lower': 'Lower Confidence Interval ($)',
            'yhat_upper': 'Upper Confidence Interval ($)'
        }, inplace=True)

        # Display Raw Data, Data for Prophet, and Forecasted Data in 4:2:4 layout
        col1, col2, col3 = st.columns([4.5, 2, 3.5])

        with col1:
            st.markdown('### Raw Data')
            st.dataframe(data.style.set_properties(**{
                'background-color': '#E6F7FF',
                'color': 'black',
                'font-weight': 'bold',
                'border-color': '#47C7DA'
            }).highlight_max(color='grey'))

        with col2:
            st.markdown('### Prophet-D')
            st.dataframe(df.style.set_properties(**{
                'background-color': '#FFF3E6',
                'color': 'black',
                'font-weight': 'bold',
                'border-color': '#DAA520'
            }).highlight_max(color='grey'))

        with col3:
            st.markdown('### Forecasted Data')
            st.dataframe(forecast[['Date', 'Predicted Stock Price ($)', 'Lower Confidence Interval ($)', 'Upper Confidence Interval ($)']].style.set_properties(**{
                'background-color': '#F2E6FF',
                'color': 'black',
                'font-weight': 'bold',
                'border-color': '#7D3FD2'
            }).highlight_max(color='grey'))

        # Plot Raw data
        st.markdown('### Raw Data Plot')
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Raw Data'))
        fig1.update_layout(title=f"{stock_options} Raw Stock Data", xaxis_title="Date", yaxis_title="Price")
        fig1.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig1)

        # Plot forecasted data
        st.markdown('### Forecasted Data Plot')
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=forecast['Date'], y=forecast['Predicted Stock Price ($)'], mode='lines', name='Predicted Price'))
        fig2.add_trace(go.Scatter(x=forecast['Date'], y=forecast['Upper Confidence Interval ($)'], mode='lines', name='Upper Confidence Interval', line=dict(dash='dash')))
        fig2.add_trace(go.Scatter(x=forecast['Date'], y=forecast['Lower Confidence Interval ($)'], mode='lines', name='Lower Confidence Interval', line=dict(dash='dash')))
        fig2.update_layout(title=f"{stock_options} Stock Price Prediction", xaxis_title="Date", yaxis_title="Price")
        fig2.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig2)
