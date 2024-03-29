import http.client, urllib.parse
import json
import pandas as pd
import datetime

conn = http.client.HTTPSConnection('api.marketaux.com')

# Read the company symbols from the excel file
df = pd.read_excel('S&P - demo.xlsx')
symbols = df['Symbol'].tolist()

# Create an empty list to store the data
company_data_list = []

df_symbols = pd.read_excel('SP_500_Companies.xlsx')

# Create a dictionary to store the symbol-name mapping
symbol_name_dict = dict(zip(df_symbols.iloc[:, 0], df_symbols.iloc[:, 1]))

# Loop through each symbol
for symbol in symbols:
    # Make an API request to get the data
    company_name = symbol_name_dict.get(symbol, 'Unknown')


    
    
    params = urllib.parse.urlencode({
        'api_token': '45ah91FXtJFaVBOZcPrCQI5wGK96cXrZrohJdQTm',
        'symbols': symbol,
        'limit': 3,
        #'search': 'stock + {}'.format(symbol),
        #'search': company_name,
        #'published_on': '2023-11-9'
        'published_after': (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%dT%H:%M'),
        'domain': 'finance.yahoo.com'
    })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()

    data = json.loads(res.read().decode('utf-8'))

    print(data)

    # Parse the response and extract the required data
    titles = [article['title'] for article in data['data']]
    urls = [article['url'] for article in data['data']]

    sentiment = [article['entities'][0]['sentiment_score'] for article in data['data']]

    for article in data['data']:
        highlights = []
        for section in article['entities'][0]['highlights']:
            highlights.append(section['highlight'])
    
    print(highlights)

    #highlights = [article['entities'][0]['highlights'][] for article in data['data']]
    

    # Store the data in a dictionary
    company_data = {'symbol': symbol, 'titles': titles, 'urls': urls, 'sentiment': sentiment, 'highlights': highlights}
    
    # Append the data to the list
    company_data_list.append(company_data)

# Create a pandas dataframe from the list
df = pd.DataFrame(company_data_list)

# Write the dataframe to a CSV file
df.to_csv('company_data5.csv', index=False)
    

















# Read the excel file


# Loop through each symbol
    # Get the corresponding symbol name from the dictionary

    # Make an API request to get the data
    # Rest of the code...




