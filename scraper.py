# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:42:25 2023

@author: karam
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request
url = "https://www.swimming.ca/records-catalogue/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the tables in the HTML
tables = soup.find_all('table')

# Initialize an empty list to store the data
data = []

# Iterate through each table
for table in tables:
    # Find the caption within the table
    # caption = table.find('caption')
    
    # # Extract the title (e.g., "Canadian Senior Records")
    # title = caption.find('span', class_='c1-2').text
    
    # # Extract the category (e.g., "Men, Open")
    # category = caption.find('span', class_='c2-2').text
    
    # Find all rows in the table's tbody
    rows = table.find('tbody').find_all('tr')
    
    for row in rows:
        columns = row.find_all('td')
        
        # Extract data if there are 7 columns (you can adjust this condition)
        # if len(columns) == 7:
        event = columns[0].text
        athlete = columns[1].find('a').text
        birth_year = columns[2].text
        club = columns[3].text
        time = columns[4].find('a').find('time').text
        date = columns[5].find('time').text
        location = columns[6].find('a').text
        
        # Append the data to the list
        data.append([title, category, event, athlete, birth_year, club, time, date, location])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=["Title", "Category", "Event", "Athlete", "Birth Year", "Club", "Time", "Date", "Location"])

# Display the DataFrame
print(df)
