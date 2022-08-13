# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:55:12 2021

@author: Zulfiqar
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
table = soup.find('table', {'summary':'Standings - Detailed View'})

header=[]
for i in table.find_all('th'):
    header.append(i.text.strip())
    
df = pd.DataFrame(columns=header)

#gets all our data within the table and adds it to our dataframe
for row in table.find_all('tr')[1:]:
    #line below fixes the formatting issue we had with the team names
    first_td = row.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length = len(df)
    df.loc[length] = row_data

    


df.to_csv('nfl_table.csv')