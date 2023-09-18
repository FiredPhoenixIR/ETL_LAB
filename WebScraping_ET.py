# First Install :  
#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
#!mamba install bs4==4.10.0 -y
#!mamba install html5lib==1.1 -y

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

url_to_scrap="https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"
response=requests.get(url_to_scrap)
html_data=response.content

#html_data[760:783]
# You can alos use if response.status_code == 200
soup = BeautifulSoup(response.text, 'html5lib') # Or html.parser

data = pd.DataFrame(columns=["Bank Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    if len(col) >= 2: # so you dont get index error
        bank_name = col[1].text.strip()
        market_cap = col[2].text.strip()
        data = data.append({"Bank Name": bank_name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)

#First 5 lines
data_first5=data.head()

targetfile="loaded_data.json"
csv_target="loaded_data.csv"

def load(targetfile,data_to_load):
    data_to_load.to_json(targetfile)
  
def load_tocsv(targetfile,data_to_load):
    data_to_load.to_csv(targetfile,index=False)

load(targetfile,data)
load_tocsv(csv_target,data)
