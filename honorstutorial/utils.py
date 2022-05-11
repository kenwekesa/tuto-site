import requests
import pandas as pd


def get_data(from_symbol, to_symbol, API_KEY):
    APIKEY = RRKMAMVFQD2U5T6Y
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey='+ APIKEY
    #r = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=' + from_symbol + '&to_symbol=' + to_symbol + '&apikey=' + API_KEY)
    r = requests.get(url)
    
    dataIntraday = r.json()

    return dataIntraday['Time Series FX (Daily)']



def convert_to_df(data):
    """Convert the result JSON in pandas dataframe"""

    df = pd.DataFrame.from_dict(data, orient='index')

    df = df.reset_index()

    #Rename columns

    df = df.rename(index=str, columns={"index": "date", "1. open": "open",
    "2. high": "high", "3. low": "low", "4. close": "close"})

    #Change to datetime

    df['date'] = pd.to_datetime(df['date'])

    #Sort data according to date

    df = df.sort_values(by=['date'])

    #Change the datatype

    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)

    #Checks
    df.head()
    df.info()

    return df