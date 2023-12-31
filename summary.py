import requests
from transformers import pipeline



def summarize(article):

    ARTICLE = """Apple today announced financial results for its fiscal 2023 second quarter ended April 1, 2023. The Company posted quarterly revenue of $94.8 billion, down 3 percent year over year, and quarterly earnings per diluted share of $1.52, unchanged year over year.
    “We are pleased to report an all-time record in Services and a March quarter record for iPhone despite the challenging macroeconomic environment, and to have our installed base of active devices reach an all-time high,” said Tim Cook, Apple’s CEO. “We continue to invest for the long term and lead with our values, including making major progress toward building carbon neutral products and supply chains by 2030.”
    “Our year-over-year business performance improved compared to the December quarter, and we generated strong operating cash flow of $28.6 billion while returning over $23 billion to shareholders during the quarter,” said Luca Maestri, Apple’s CFO. “Given our confidence in Apple’s future and the value we see in our stock, our Board has authorized an additional $90 billion for share repurchases. We are also raising our quarterly dividend for the eleventh year in a row.”
    Apple’s board of directors has declared a cash dividend of $0.24 per share of the Company’s common stock, an increase of 4 percent. The dividend is payable on May 18, 2023 to shareholders of record as of the close of business on May 15, 2023. The board of directors has also authorized an additional program to repurchase up to $90 billion of the Company’s common stock."""

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return ((summarizer(article, max_length=200, min_length=30, do_sample=False))[0]['summary_text'].split('. '))
    

# # turn the result into a list of sentences

# sentences = (summarizer(ARTICLE, max_length=200, min_length=30, do_sample=False))[0]['summary_text'].split('. ')

# print(sentences)

