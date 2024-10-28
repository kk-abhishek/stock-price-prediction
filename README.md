
# 📈 Stock Price Prediction App

**Stock Price Prediction App** is an interactive Streamlit application that predicts stock prices based on historical data using the **yfinance** and **Prophet** libraries. With a simple, user-friendly interface, this app lets you explore stock data, view historical prices, and generate future predictions for both Indian and international companies.

### 🌐 Access the App Online

Access the live application here: [![Streamlit](https://raw.githubusercontent.com/streamlit/streamlit/develop/docs/images/brand/logo.png)](https://your-username-streamlit-stock-prediction-app.streamlit.app)  
*(Replace with your actual deployment link)*


---

## 🚀 Features
- **Real-Time Stock Data**: 
    Retrieve live stock data directly from Yahoo Finance using yfinance.
- **Customizable Forecasting**: 
    Set the number of historical years, data interval, and prediction years to customize the forecast.
- **50+ Stock Selections**: 
    Choose from a list of top companies, including 25 Indian and 25 international firms, by their names (e.g., **Apple** for AAPL).
- **Interactive Graphs**: 
    Visualize historical and forecasted stock prices with visually appealing, interactive Plotly charts.

---
## 🔧 Project Structure

```plaintext
.
├── streamlit_app.py         # Main app script
├── requirements.txt         # Python dependencies
├── README.md       # Project description and setup
└── style.css       # Custom CSS styling for the app

```
---

## 🛠️ Setup Instructions

- **Prerequisites :**
    Python 3.7+: Ensure Python is installed on your machine.
    Git: Make sure Git is installed to clone the repository.

- **Clone the Repository:**
    Open your terminal and run: git clone **https://github.com/your-username/stock-price-prediction-app.git**
cd stock-price-prediction-app

- **Create a Virtual Environment:** (Optional but Recommended)
    To avoid conflicts with other Python packages, set up a virtual environment: 
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

- **Install Dependencies:**
    Use the following command to install all required libraries listed in requirements.txt:
    ```
    pip install -r requirements.txt** 
    ```

- **Run the Application Locally:**
    Start the Streamlit app by running:
    ```
    streamlit run streamlit_app.py
    ```
    After executing this command, a link (e.g., http://localhost:8501) will appear in the terminal. Click on the link or paste it into your browser to access the app locally.

---

## 🌐 Deploying on Streamlit Cloud

- **Sign Up/Login:**
    Go to Streamlit Cloud and sign in.
- **Create a New App:**
    Link your GitHub repository and select the correct repository (stock-price-prediction-app).
- **Set Entry Point:**
    Choose streamlit_app.py as the main file to run.
- **Deploy:**
    Click Deploy, and your app will be live on Streamlit.
---
## 🧪 How to Use
- **Select a Stock:**
    Choose a company by name from the sidebar.
- **Adjust Settings:** 
    Customize historical data period, interval, and prediction years.
- **View Results**
- **Original Data**: 
    View historical stock prices in a data frame.
- **Forecasted Data**: 
    See the projected stock prices for the selected years.
- **Interactive Graphs**:
    Visualize both historical and predicted data through dynamic, interactive charts.

---
## 📊 Technology Stack

- **Backend**: Python
- **Machine Learning**: ML
- **Frontend**: Streamlit
- **Data Source**: yfinance
- **Forecasting Model**: Prophet
- **Visualization**: Plotly

---
## 👤 Author
**Abhishek KK**  



