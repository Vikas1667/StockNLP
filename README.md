
### Usecases 

1. Bank Statement Analysis

    1.  Data parsing 
        1. Parsing Pdf and CSV data using Open source python packages and AWS textract 

    2. Extracting PDF statement
        1) Open source: Tabula
        2) Cloud Solution: AWS --> Textract
     
    3. Parsing CSV data 
        1) Paring CSV data 
 
    4. Spend analysis using Bank statement
        1. https://towardsdatascience.com/manage-your-money-with-python-707579202203

2. Financial Data Extraction 
    1. Income Statement, Balance Sheet Extraction, Cashflow data extraction
    2. Web Scraping Stock Tickers and NSE nifty list Using Python 
    3. Transcript data extraction using Seeking Alpha 


3. Portfolio Analysis API 
   1) Build with open source and test with streamlit   
   2) Build using Kite API
  
   * Design 
      1. Getting stocks data from user 
      2. Prediction model for stocks
   
   * Task
      1. Build Skeleton and test using Streamlit. 
      2. Development account for kite. 
   
    

### Data Extraction Methods

API with alot information for accessing various segment of business
1. [Financial Modeling Prep](https://site.financialmodelingprep.com/)


### NLP Funnel 
### Financial Terms and NLP bond

1. Financial Compliance

Financial compliance is the regulation and enforcement of the laws and rules in finance and the capital markets. It ranges through the entire financial spectrum, from investment banking practices to retail banking practices


## Text Summarization

### Various Methods 

   1. Extraction-based Summarization
        1. Unsupervised Extractive Summarization 

   2. Abstraction-based Summarization

### Task in Progress
   1. Dataset 
   2. Techniques:
   3. Eval Metrics:ROUGE scores,
   4. Issue
   5. overcome 
 
### Implementation
TFIDF and centroid embedding
https://towardsdatascience.com/a-better-approach-to-text-summarization-d7139b571439


### Skipthought and Clustering
https://medium.com/jatana/unsupervised-text-summarization-using-sentence-embeddings-adb15ce83db1

## Stock Component Analysis
1. Option Chain Data Extraction
2. Support Resistance Indicators
3. Scrapping strike price & expiry date
4. Real Time stock data prediction

References
1. https://www.youtube.com/watch?v=q_MWWVgghsQ
2. yahoo graph : https://gist.github.com/SajidLhessani

#### References
1. https://tradewithpython.com/portfolio-analysis-using-python
2. https://towardsdatascience.com/understanding-automatic-text-summarization-1-extractive-methods-8eb512b21ecc
3. https://towardsdatascience.com/creating-an-interactive-data-app-using-plotlys-dash-356428b4699c
4. https://stackoverflow.com/questions/66708474/is-there-a-way-to-render-spacys-ner-output-on-a-dash-dashboard
5. https://stackoverflow.com/questions/52638897/how-do-i-give-a-delay-in-user-input-to-a-textbox-in-a-dash-app




Skeleton
(Financial)Keyword(tw)--> Data extraction(Mongo)--> Model(CNN or LSTM)-->FastAPI

Beautifulsoup
Requests
Selenium
```
!pip install bs4
!pip install --upgrade kiteconnect
!pip install moneycontrolPy
!pip install dateparser
!pip install moneycontrolPy
!pip install dateparser
!pip install selenium
from selenium import webdriver
```

https://www.kaggle.com/kritanjalijain/twitter-sentiment-analysis-lstm/notebook


Task 2.1: Decide by sneha(Financial Domain, Healthcare),(Text Classification) 

https://towardsdatascience.com/multi-label-emotion-classification-with-pytorch-huggingfaces-transformers-and-w-b-for-tracking-a060d817923

Task 3 : Scrap the stock data--> store in mongodb



NLP topics
 
	1. Financial Documents(NSE, Transcripts, statements), Table and Image(table) extraction then NLP Dash Application(Trending keywords, Topic Modeling,) DASK.--> Package
          
	Skeleton -- Design, function, doc variation 

	1. Brazilian E-commerce 
	
	
	2. Utility building and Build word2vec with Fast text 
	Word2vec 
	 1) CBOW and Skipgram
	 2) TFIDF, glove, sentence embedding, Blazzing Text
	https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext.html
	 
	
	
	3.  Food NLP prototype 
	
	https://www.ifpri.org/topics
	https://fas.org.in/
	https://www.ifpri.org/topic/food-security
	

India Food Security
https://nfsa.gov.in/



NSE pdf--> Raw text--> Topic modeling, spacy NER --> tp(finance, Food  )-->Keywords --> News scraper--> News collect--> Topic modeling --->sentiment, intent , Emotion--> Chatbot


Keywords based News Extractor:

https://medium.com/daily-python/python-script-to-search-for-news-based-on-keywords-daily-python-5-509348bd190e


	1. Neo4j__ graph 
    2.    MongoDB

Frontend: Various  statistics and No of Topics, Topic modeling,

Financial NLP 
Tab: Financial PDF Extractor  
Task1:2 week: 11/6 --> 1/7
	1. PYTesseract--> text--> topic modeling , Keyphrase--> API
	

NSE extractor
 tabs : Annual report Analysis


1) Preprocessing Steps

