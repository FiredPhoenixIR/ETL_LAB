import glob
import pandas as pd
from datetime import datetime

# Get Files : 
'''
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_1.json
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_2.json
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/exchange_rates.csv
'''
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe
  
#columns=['Name','Market Cap (US$ Billion)']

def extract(jsonfile):
    extracted_data= pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
    for jsonfile in glob.glob(jsonfile):
        extracted_data= extracted_data.append(extract_from_json(jsonfile),ignore_index=True)
    return extracted_data
#extracted_data=extract('./bank_market_cap_1.json')

def extract_csv(csvfile):
    extracted_data= pd.DataFrame (columns=['Rates']) #,'Rates'])
    for csvfile in glob.glob(csvfile):
        extracted_data= extracted_data.append(extract_from_csv(csvfile),ignore_index=True)
    extracted_data.columns.values[1] = 'Currency'
    return extracted_data
  
extracted_csvdata=extract_csv('./exchange_rates.csv')
extracted_csvdata=extracted_csvdata[['Currency','Rates']]


def exhchange_rate(currency_symbol):
    rate=extracted_csvdata[extracted_csvdata['Currency'] == currency_symbol]
    return rate

#exhchange_rate('GBP') as dataframe

def transform(first_symbol,second_symbol):
    rate_first=exhchange_rate(first_symbol)
    rate_first=rate_first['Rates'].to_list()
    rate_second=exhchange_rate(second_symbol)
    rate_second=rate_second['Rates'].to_list()
    rate_to_rate=rate_first[0]/rate_second[0]
    return rate_to_rate

#transform('USD','GBP') as number

#load dataframe to csv
def load_to_csv(tagetfilename,data_to_load):
    targetfile=tagetfilename
    data_to_load.to_csv(targetfile,index=False)

#load_to_csv('./bank_market_cap_gbp.csv',exhchange_rate('GBP'))

#Logging
def log(message):
    timestamp_format='%Y-%h-%d-%H:%M:%S'
    now= datetime.now()
    timestamp= now.strftime(timestamp_format)
    with open ("logfile.txt", "a") as f:
        f.write (timestamp + ',' + message + '\n')
