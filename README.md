
# 📈 Stock Price Prediction App

**Stock Price Prediction App** is an interactive Streamlit application that predicts stock prices based on historical data using the **yfinance** and **Prophet** libraries. With a simple, user-friendly interface, this app lets you explore stock data, view historical prices, and generate future predictions for both Indian and international companies.

---

## 📹 APP Demo
Check out the demo of the app to see its features in action:
    [![Demo Video](https://raw.githubusercontent.com/kk-abhishek/stock-price-prediction-app/main/images/demo_thumbnail.png)](https://www.loom.com/share/28ce91ac5291450397fa5c773d078b2b?sid=08206dc2-8869-4986-827c-296adf1c51a0)

---

## 🌐 Access the App Online

Access the live application here:
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-savvy-by-kk.streamlit.app/)



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

- **Backend**: Python,ML 
- **Frontend**: Streamlit
- **Data Source**: yfinance
- **Forecasting Model**: Prophet by facebook
- **Visualization**: Plotly & Pandas.

<p align="left">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python"/>
  </a>
  <a href="https://facebook.github.io/prophet/">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Prophet"/>
  </a>
  <a href="https://plotly.com/">
    <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  </a>
</p>

---
## 👤 Author
**Abhishek KK**  

<div>
  <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/kk-abhishek">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="kkabhishek100@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</div>



