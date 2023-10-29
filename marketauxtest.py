import http.client, urllib.parse
import json
import pandas as pd
import datetime

conn = http.client.HTTPSConnection('api.marketaux.com')

# Read the company symbols from the excel file
df = pd.read_excel('SP_500_Companies.xlsx')
symbols = df['Symbol'].tolist()

# Loop through each symbol
for symbol in symbols:
    # Make an API request to get the data
    
    params = urllib.parse.urlencode({
        'api_token': '45ah91FXtJFaVBOZcPrCQI5wGK96cXrZrohJdQTm',
        'symbols': symbol,
        'limit': 3,
        'search': 'stock + {}'.format(symbol),
        'published_after': (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M')
    })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()

    data = json.loads(res.read().decode('utf-8'))

    # Parse the response and extract the required data
    titles = [article['title'] for article in data['data']]
    urls = [article['url'] for article in data['data']]

    # Store the data in a dictionary
    company_data = {'symbol': symbol, 'titles': titles, 'urls': urls}

    print(company_data)



    