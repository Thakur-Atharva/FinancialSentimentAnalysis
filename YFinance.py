from bs4 import BeautifulSoup
import requests

# url = "https://finance.yahoo.com/m/352eafc8-c07c-376d-95ca-cc57a52af27f/the-brilliant-reason-apple%27s.html?.tsrc=rss"
URL = "https://finance.yahoo.com/quote/AAPL/news"
# url = "https://finance.yahoo.com/topic/stock-market-news"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# for link in soup.find_all('a', href = True):
    # print(link.get('href'))

# URL = "https://finance.yahoo.com/news/fed-meeting-apple-earnings-what-to-know-this-week-140035960.html"
URL = "https://finance.yahoo.com/m/13f36da8-1059-40c1-a5ad-f6d57bc1a60b/new-report-reveals-details-on.html?.tsrc=fin-srch"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.text.replace(". ", ".\n"))


#from github

from bs4 import BeautifulSoup
import requests
URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.find_all('a', href = True):
    print (link.get('href'))
URL = "https://finance.yahoo.com/news/true-value-always-prevails-against-technological-advancement-141902215.html"
page2 =requests.get(URL)
soup = BeautifulSoup(page2.content, 'html.parser')
print(soup.text)
