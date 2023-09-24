# As a data scientist working for a hedge fund, you will extract the profit data for Tesla and GameStop and build a dashboard to compare the price of the stock vs the profit for the hedge fund.
'''
!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y
!pip install nbformat==4.2.0
'''
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define Graphing Function
# It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

tesla=yf.Ticker("TSLA")
''' tesla.history(period="max") '''
tesla_data.reset_index(inplace=True)
'''tesla_data.head()'''
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url).text
soup = BeautifulSoup(html_data,"html.parser")
tr_data=soup.find_all('tr')
#tr_data #.find_all(name='th') #.find_all('th')
#tr_data[1].find_all("td")
tesla_annual_revenue=pd.DataFrame(columns=['Date','Revenue'])
tesla_quarterly_revenue=pd.DataFrame(columns=['Date','Revenue'])
new_columns = ['Date','Revenue']
tables=pd.read_html(html_data)
tesla_annual_revenue=tables[0]
tesla_quarterly_revenue=tables[1]
tesla_annual_revenue.columns=new_columns
tesla_quarterly_revenue.columns=new_columns

