import requests
import pandas as pd

API_URL = "https://api-inference.huggingface.co/models/ahmedrachid/FinancialBERT-Sentiment-Analysis"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Choose which test case to run below:

# Read the CSV file
df = pd.read_csv('company_data5.csv')

# Filter the rows with symbol "MSFT"
msft_row = df[df['symbol'] == 'MSFT']

# Get the text from the 'highlights' column
highlights_text = msft_row['highlights'].values[0]

print(highlights_text)



testA = highlights_text.replace('[', '').replace(']', '').replace('<', '').replace('>', '')

#testA = "Autodesk shares fell even as the software company reported third-quarter earnings that beat analyst expectations on both the top and bottom lines and lifted its full-year guidance. However, total billings dropped 11 due to Autodesk shifting its customer billing from a 3-year contract that's paid upfront to an annual payment. Additionally, Piper Sandler downgraded the stock from Overweight to a Neutral citing margin concerns. Yahoo Finance's Jared Blikre and Seana Smith break down the details of this trending ticker. For more expert insight and the latest market action, click here to watch this full episode of Yahoo Finance Live."

def sort_sentiment(list_dict):  #
    new_list = [{}, {}, {}]  
    max_val = 0
    max = ''
    for dict in list_dict:
        if dict['label'] == 'positive':         #
            if dict['score'] > max_val:
                max = 'positive'
                max_val = dict['score']
            new_list[0] = dict
        elif dict['label'] == 'neutral':
            if dict['score'] > max_val:
                max = 'neutral'
                max_val = dict['score'] 
            new_list[1] = dict
        else:
            if dict['score'] > max_val:
                max = 'negative'
                max_val = dict['score']
            new_list[2] = dict

    return new_list, max, max_val


# the double for loop separates sentences and their main clauses.
running = 0
count = 0

for i in testA.split('. '):
    for j in i.split('and '):
        count = count + 1
        print(j + '\n')
        output = query({
            "inputs": f"{j}",
        })
        result, max, max_val = sort_sentiment(output[0])
        print(max, f"{round(max_val, 3) * 100}%")
        running = running + max_val
        #print(result[0])
        #print(result[1])
        #print(result[2])
        #print('')


# for i in testA.split('.'):
#     count = count + 1
#     print(i + '\n')
#     output = query({
#         "inputs": f"{i}",
#     })
#     result, max, max_val = sort_sentiment(output[0])
#     print(max, f"{round(max_val, 3) * 100}%")
#     running = running + max_val
#         # print(result[0])
#         # print(result[1])
#         # print(result[2])
#     print('')

# print(f"Average sentiment: {round(running/count, 3) * 100}%")


# count = count + 1
# output = query({
#     "inputs": f"{testA}",
# })


# #result, max, max_val = sort_sentiment(output)
# #print(max, f"{round(max_val, 3) * 100}%")
# #running = running + max_val
#         # print(result[0])
#         # print(result[1])
#         # print(result[2])
# print('')

print(f"Average sentiment: {round(running/count, 3) * 100}%")


