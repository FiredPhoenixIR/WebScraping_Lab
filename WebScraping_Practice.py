'''
Required :
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0
'''
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

# We can use the method prettify() to display the HTML in the nested structure
#print(soup.prettify())
tag_object=soup.title
#print("tag object:",tag_object)
#print("tag object type:",type(tag_object)) #we can see the tag type bs4.element.Tag
tag_object=soup.h3
#tag_object
tag_child =tag_object.b
#tag_child

#If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest. You can access a tag’s attributes by treating the tag like a dictionary
'''tag_child['id'] '''
#ou can access that dictionary directly as attrs
'''tag_child.attrs'''
#We can also obtain the content if the attribute of the tag using the Python get() method
'''tag_child.get('id')'''

parent_tag=tag_child.parent
'''parent_tag''' # And tag_object parent is the body element.
sibling_1=tag_object.next_sibling
'''sibling_1 ''' #tag_object sibling is the paragraph element here
sibling_2=sibling_1.next_sibling
'''sibling_2'''
tag_string=tag_child.string
#tag_string #A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the NavigableString class to contain this text
'''type(tag_string) : ''' #bs4.element.NavigableString
# A NavigableString is just like a Python string or Unicode string, to be more precise. 
# The main difference is that it also supports some BeautifulSoup features. We can covert it to sting object in Python
unicode_string = str(tag_string)
'''unicode_string'''

#Filters allow you to find complex patterns, the simplest filter is a string. 
#In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string. 
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")
table_rows=table_bs.find_all('tr')  #he find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
# The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

# table_rows
first_row =table_rows[0]
'''first_row'''
'''print(type(first_row)) : <class 'bs4.element.Tag'>'''
'''first_row.td'''
#If we iterate through the list, each element corresponds to a row in the table
'''
for i,row in enumerate(table_rows):
    print("row",i,"is",row)
'''
'''
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
'''
list_input=table_bs .find_all(name=["tr", "td"])
'''list_input'''
# For example, the first td elements have a value of id of flight, therefore we can filter based on that id value
table_bs.find_all(id="flight") #:[<td id="flight">Flight No</td>]
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
'''list_input'''
table_bs.find_all(href=True) #If we set the  <code>href</code> attribute to True, regardless of what the value is, the code finds all tags with <code>href</code> value
'''soup.find_all(id='boldest')'''
'''table_bs.find_all(string="Florida")'''
# if you are looking for one element you can use the find() method to find the first element in the document
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
'''two_tables_bs.find("table")''' #We can find the first table using the tag name table
'''two_tables_bs.find("table",class_='pizza')'''

#---------------------------
url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
'''
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))
'''
'''
for imagelink in soup.find_all('img'):# in html image is represented by the tag <img>
    print(imagelink)
    print(imagelink.get('src'))
'''

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
'''
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code)) # ***
'''
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
'''len(tables)'''
# Assume that we are looking for the 10 most densly populated countries table, 
#we can look through the tables list and find the right one we are look for based on the data in each table 
#or we can search for the table name if it is in the table but this option might not always work
'''
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
'''
'''
print(tables[table_index].prettify())
'''
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
'''
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data
'''
pd.read_html(str(tables[table_index]), flavor='bs4')
# We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4
population_data_read_html = pd.read_html(str(tables[table_index]), flavor='bs4')[0]
'''
population_data_read_html
'''
dataframe_list = pd.read_html(url, flavor='bs4')
'''len(dataframe_list)'''
'''dataframe_list[7]'''
'''pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]'''
