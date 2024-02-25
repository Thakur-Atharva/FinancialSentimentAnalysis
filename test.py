# import requests
# from bs4 import BeautifulSoup

# # Replace 'your_url' with the actual URL you want to scrape
# url = 'https://finance.yahoo.com/news/increases-ceo-compensation-might-put-101645673.html'

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all text in the page
#     all_text = soup.get_text()

#     # Print all the text
#     print(all_text)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")


import trafilatura

# Replace 'your_url' with the actual URL you want to scrape
url = 'https://finance.yahoo.com/news/increases-ceo-compensation-might-put-101645673.html'

# Download the web page content using Trafilatura
downloaded_content = trafilatura.fetch_url(url)

text_content = trafilatura.extract(downloaded_content)
print(text_content)
