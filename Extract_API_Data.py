import requests
import pandas as pd

exchangeratesapi_url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=831145c303697d0406b480c8d5cfcca4" #API Key added #Base is already set
apilayer_url = "https://api.apilayer.com/exchangerates_data/4t8Lhjpk66dFDGAlPBapSNsgbrfYOfez"

# Turn the data into a dataframe
try:
    # Send an HTTP GET request to the API
    response = requests.get(exchangeratesapi_url)
    # Data is like this :
    '''
    {'success': True,
     'timestamp': 1695060783,
     'base': 'EUR',
     'date': '2023-09-18',
     'rates': {'AED': 3.924366,
      'AFN': 84.406036,
      'ALL': 106.469081,
    '''
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Assuming the API response is in JSON format
        api_data = response.json()

        # Extract currency names (keys of the 'rates' dictionary)
        currency_names = list(api_data['rates'].keys())
        # Create a DataFrame from the currency rates
        df = pd.DataFrame({#'Currency': currency_names,
                           'Rate': list(api_data['rates'].values())}, index=currency_names)


        # Drop unnecessary columns (if any)
        #df.drop(['timestamp' , 'success' , 'date' , 'base' ], axis=1, inplace=True)

        # Rename columns if needed (optional)
        # df.rename(columns={'OriginalColumn1': 'NewColumn1', 'OriginalColumn2': 'NewColumn2'}, inplace=True)

        # Now, the 'df' DataFrame should have 'Currency' as the index and 'Rate' as the column
        print(df)

    else:
        print(f"API request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#Double Check
columns_to_drop = ['timestamp', 'success', 'date', 'base']
for column in columns_to_drop:
    if column in df.columns:
        df.drop(column, axis=1, inplace=True)

csv_targetfile="exchange_data.csv"

def load(targetfile,data_to_load):
    #column_names = ['Counter_Currency', 'Exchange Rate']
    data_to_load.to_csv(targetfile)

load(csv_targetfile,df)

