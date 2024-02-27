import requests
from transformers import pipeline

ARTICLE = """Better Tech Stock: Microsoft vs. Apple
Wall Street is particularly bullish about tech stocks now. Excitement about budding markets like artificial intelligence (AI) and easing inflation sent the Nasdaq-100 Technology Sector index up 47% since last February.
As the world's two most valuable companies and leaders in tech, Microsoft (NASDAQ: MSFT) and Apple (NASDAQ: AAPL) have seen their shares rise 54% and 18% during the period. These companies are some of the most attractive ways to invest in the industry, with one a king in productivity software and the other leading the consumer tech market.
Microsoft and Apple have long histories of delivering consistent stock growth, and that looks unlikely to change. Over the last year, Microsoft emerged as one of the biggest names in AI. Meanwhile, Apple is home to a highly profitable services business and is gaining market share in the virtual reality/augmented reality (VR/AR) industry.
So, let's examine these businesses and determine whether Microsoft or Apple is the better tech stock this February.
Microsoft
In January, Microsoft overtook Apple as the world's most valuable company, with its market cap at just over $3 trillion.
The company is a tech behemoth with positions in multiple areas of the industry, leading in productivity software, game consoles, cloud computing, and operating systems. Its diverse business model allows it to profit from tailwinds across tech, making its stock an exceptionally reliable option.
Since 2019, Microsoft's annual revenue climbed 68%, with operating income up 106%. Additionally, its free cash flow jumped 76% to $67 billion.
The company has significant cash reserves, allowing it to keep investing in its business and retain its prominent role in tech. Microsoft became a leader in AI after sinking billions into ChatGPT developer OpenAI. The partnership granted Microsoft access to some of the sector's most advanced AI models, which it used to carve out a lucrative position in the budding industry.
The AI market is projected to expand at a compound annual growth rate (CAGR) of 37% through 2030, which would see it hit nearly $2 trillion before the end of the decade.
Meanwhile, Microsoft used OpenAI's technology to introduce AI features across its product lineup. In 2023, Microsoft added new AI tools to its Azure cloud platform, integrated aspects of ChatGPT into its Bing search engine, and boosted productivity in its Office software suite with the help of AI.
Apple
Apple hasn't had it as easy as Microsoft in the last year. In 2023, macroeconomic headwinds caught up with the company, leading to four consecutive quarters of revenue declines.
The streak was finally broken in Apple's latest quarter, with revenue rising 2% year over year to $120 billion in the first quarter of 2024. The company beat Wall Street forecasts by more than $1 billion.
However, outperforming estimates wasn't enough to quell investor concern over its iPhone business, with its stock down nearly 6% year to date. Smartphone sales rose 6% in Q1 2024, yet fell 13% in China. The country has increased restrictions on the iPhone, threatening business from Apple's third-largest market.
As a result, it's promising that the company is expanding its product lineup and prioritizing digital markets like services to lean less on iPhone sales over the long term.
The company released the Vision Pro, its first VR/AR headset, earlier this year. Launching at $3,499, the new device created significant hype for the technology. If the company employs a similar pricing strategy to that used with past products and brings down the cost with subsequent generations, an investment in Apple could be an investment in the future leader of the VR/AR market.
The VR market alone is expected to grow at a CAGR of 31% until at least 2030. It could be smart to invest in the tech giant at the very start of its journey into the industry.
Alongside free cash flow that hit $107 billion last year, Apple has the funds to overcome current headwinds and keep investing in high-growth areas of tech.
Is Microsoft or Apple the better tech stock?
Microsoft and Apple have exciting long-term outlooks, with opportunities to profit from multiple subsectors of tech.
However, Microsoft's more significant priority on digital markets like cloud computing and AI makes it less vulnerable to macroeconomic headwinds and potentially the more reliable buy.
Meanwhile, earnings-per-share estimates indicate Microsoft has more growth potential than Apple in the near term.
Microsoft's earnings could hit just under $16 per share, while Apple's may reach nearly $8 per share in the next two fiscal years. Multiplying those figures by the companies' forward price-to-earnings ratios (Microsoft's 35 and Apple's 28) yields a stock price of $546 for Microsoft and $218 for Apple.
Looking at their current positions, these projections would see Microsoft's stock rise by 35% and Apple's increase by 20% by fiscal 2026. If these projections are correct, Microsoft has significantly more room to run and is the better tech stock to buy this month.
Where to invest $1,000 right now
When our analyst team has a stock tip, it can pay to listen. After all, the newsletter they have run for two decades, Motley Fool Stock Advisor, has more than tripled the market.*
They just revealed what they believe are the 10 best stocks for investors to buy right now… and Microsoft made the list -- but there are 9 other stocks you may be overlooking.
*Stock Advisor returns as of February 20, 2024
Dani Cook has no position in any of the stocks mentioned. The Motley Fool has positions in and recommends Apple and Microsoft. The Motley Fool recommends the following options: long January 2026 $395 calls on Microsoft and short January 2026 $405 calls on Microsoft. The Motley Fool has a disclosure policy.
Better Tech Stock: Microsoft vs. Apple was originally published by The Motley Fool"""
def summarize(article):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print ((summarizer(article, max_length=1000, min_length=30, do_sample=False))[0]['summary_text'].split('. '))

summarize(ARTICLE)

# # # turn the result into a list of sentences

# sentences = (summarizer(ARTICLE, max_length=200, min_length=30, do_sample=False))[0]['summary_text'].split('. ')

# print(sentences)

