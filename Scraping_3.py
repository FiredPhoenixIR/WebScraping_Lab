# Extracting Stock Data Using a Web Scraping
'''
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y 
!pip install lxml==4.6.4
#!pip install plotly==5.3.1
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
''' print(data) '''
soup = BeautifulSoup(data, 'html5lib')
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
'''
These are the following tags which are used while creating HTML tables.

    <table> tag: This tag is root tag used to define the start and end of the table. All the content of the table is enclosed within these tags.

    <tr> tag: This tag is used to define a table row. Each row of the table is defined within this tag.

    <td> tag: This tag is used to define a table cell. Each cell of the table is defined within this tag. You can specify the content of the cell between the opening and closing tags.

    <th> tag: This tag is used to define a header cell in the table. The header cell is used to describe the contents of a column or row. By default, the text inside a tag is bold and centered.

    <tbody> tag: This is the main content of the table, which is defined using the tag. It contains one or more rows of elements.
'''

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
''' netflix_data.head() '''

# Extracting data using pandas library
read_html_pandas_data = pd.read_html(url) #returns a list of all the tables found on the webpage
read_html_pandas_data = pd.read_html(str(soup)) #convert the BeautifulSoup object to a string
netflix_dataframe = read_html_pandas_data[0]
'''netflix_dataframe.head()'''
