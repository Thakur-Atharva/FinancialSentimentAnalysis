import requests

API_URL = "https://api-inference.huggingface.co/models/ahmedrachid/FinancialBERT-Sentiment-Analysis"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "I like you. I love you",
})

print(output[0][0])
print(output[0][1])
print(output[0][2])