import http.client, urllib.parse
import json
import pandas as pd
import datetime

conn = http.client.HTTPSConnection('api.marketaux.com')

# Read the company symbols from the excel file
df = pd.read_excel('S&P - first 50.xlsx')
symbols = df['Symbol'].tolist()

# Create an empty list to store the data
company_data_list = []

# Loop through each symbol
for symbol in symbols:
    # Make an API request to get the data
    
    params = urllib.parse.urlencode({
        'api_token': '45ah91FXtJFaVBOZcPrCQI5wGK96cXrZrohJdQTm',
        'symbols': symbol,
        'limit': 3,
        'search': 'stock + {}'.format(symbol),
        'published_after': (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%dT%H:%M')
    })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()

    data = json.loads(res.read().decode('utf-8'))

    # Parse the response and extract the required data
    titles = [article['title'] for article in data['data']]
    urls = [article['url'] for article in data['data']]

    sentiment = [article['entities'][0]['sentiment_score'] for article in data['data']]

    

    # Store the data in a dictionary
    company_data = {'symbol': symbol, 'titles': titles, 'urls': urls, 'sentiment': sentiment}
    
    # Append the data to the list
    company_data_list.append(company_data)

# Create a pandas dataframe from the list
df = pd.DataFrame(company_data_list)

# Write the dataframe to a CSV file
df.to_csv('company_data.csv', index=False)

