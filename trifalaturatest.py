import trafilatura
import pandas as pd
import requests

from bs4 import BeautifulSoup

df = pd.read_excel('S&P - demo.xlsx')

symbols = df['Symbol'].tolist()

articles = {}

for symbol in symbols:
    URL = "https://www.google.com/finance/quote/" + symbol + ":NASDAQ?hl=en"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    urls = []

    links = soup.find_all('a', class_='TxRU9d')
    for link in links:
        href = link.get('href')
        urls.append(href)
    
    articles.update({symbol: urls})

df2 = pd.DataFrame()

text_content = {}

for symbol in symbols:
    url = articles[symbol]
    company_text = []
    for link in url:
        try:
            downloaded = trafilatura.fetch_url(link)
            result = trafilatura.extract(downloaded)
        except:
            print('Error')
            continue
        company_text.append(result)
    text_content.update({symbol: company_text})   
    
pd.DataFrame.from_dict(text_content, orient='index').to_csv('scraped_articles.csv', header=False)

(pd.read_csv('scraped_articles.csv', header=None)).to_excel('scraped_articles.xlsx', index=False, header=False)


# for symbol in articles.items():
#     print(symbol)
#     downloaded = trafilatura.fetch_url(url)
#     result = trafilatura.extract(downloaded)
#     print(result)

    # for url in urls:
    #     try:
    #         downloaded = trafilatura.fetch_url(url)
    #         result = trafilatura.extract(downloaded)
    #         print(result)
    #         df2 = df2.append({'symbol': symbol, 'articles': [result]}, ignore_index=True)
    #     except:
    #         print('Error')
    #         continue

# print(df2)


#     for URL in urls:
#         try:
#             downloaded = trafilatura.fetch_url(URL)
#             result = trafilatura.extract(downloaded)
#             df2 = df2.append({'symbol': symbol, 'article': result}, ignore_index=True)
#         except:
#             print('Error')
#             continue
# print(df2)
# df2.to_csv('company_articles2.csv', index=False)


