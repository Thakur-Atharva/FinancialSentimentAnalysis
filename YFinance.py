from bs4 import BeautifulSoup
import requests
import summary
import pandas as pd
from transformers import pipeline

# url = "https://finance.yahoo.com/m/352eafc8-c07c-376d-95ca-cc57a52af27f/the-brilliant-reason-apple%27s.html?.tsrc=rss"
# URL = "https://finance.yahoo.com/quote/AAPL/news"
# URL = "https://finance.yahoo.com/topic/stock-market-news"

df = pd.read_excel('S&P - first 10 (1).xlsx')
symbols = df['Symbol'].tolist()
company_data_list = []

for symbol in symbols:
    URL = "https://finance.yahoo.com/quote/" + symbol + "?p=" + symbol + "&.tsc=fin-srch"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = []
    #summaries = []
    articles = []
    for link in soup.find_all('a', href = True):
        news_url = link.get('href')
        if "/news/" in news_url and ".html" in news_url:
            urls.append("https://finance.yahoo.com" + news_url)
            print(news_url)

    print(urls)

    for URL in urls:
        page2 = requests.get(URL)
        soup = BeautifulSoup(page2.content, 'html.parser')
        print(URL)
        print(soup.text[soup.text.find('below' + symbol) + 5:soup.text.find('TRENDING 1')])
        articles.append(soup.text[soup.text.find('below' + symbol) + 5:soup.text.find('TRENDING 1')])
        #summaries.append(summary.summarize(soup.text[soup.text.find('below' + symbol) + 5:soup.text.find('TRENDING 1')]))
        print()

    companydata = {'symbol': symbol, 'articles' : articles}

    company_data_list.append(companydata)

df = pd.DataFrame(company_data_list)

# Write the dataframe to a CSV file
df.to_csv('company_data_yahoo2.csv', index=False)

    #print(summaries)

"""URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
urls = []
summaries = []
for link in soup.find_all('a', href = True):
    news_url = link.get('href')
    if "/news/" in news_url and ".html" in news_url:
        urls.append("https://finance.yahoo.com" + news_url)
        print(news_url)

print(urls)

for URL in urls:
    page2 = requests.get(URL)
    soup = BeautifulSoup(page2.content, 'html.parser')
    print(URL)
    print(soup.text[soup.text.find('belowAAPL') + 5:soup.text.find('TRENDING 1')])
    summaries.append(summary.summarize(soup.text[soup.text.find('belowAAPL') + 5:soup.text.find('TRENDING 1')]))
    print()

print(summaries)"""

# # URL = "https://finance.yahoo.com/news/fed-meeting-apple-earnings-what-to-know-this-week-140035960.html"
# URL = "https://finance.yahoo.com/m/13f36da8-1059-40c1-a5ad-f6d57bc1a60b/new-report-reveals-details-on.html?.tsrc=fin-srch"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.text.replace(". ", ".\n"))


#from github

# from bs4 import BeautifulSoup
# import requests
# URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# for link in soup.find_all('a', href = True):
#     print (link.get('href'))
# URL = "https://finance.yahoo.com/news/true-value-always-prevails-against-technological-advancement-141902215.html"
# page2 =requests.get(URL)
# soup = BeautifulSoup(page2.content, 'html.parser')
# print(soup.text)
