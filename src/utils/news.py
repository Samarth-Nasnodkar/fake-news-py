import newspaper
import pickle
import numpy as np
import pandas as pd
import re
import string

def processText(text: str) -> str:
  text = text.lower()
  text = re.sub('\[.*?\]', '', text)
  text = re.sub("\\W"," ",text) 
  text = re.sub('https?://\S+|www\.\S+', '', text)
  text = re.sub('<.*?>+', '', text)
  text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text = re.sub('\n', '', text)
  text = re.sub('\w*\d\w*', '', text)    
  return text

class News:
  def __init__(self) -> None:
    self.lRModel = pickle.load(open('../ml/models/lr.pkl', 'rb'))
    self.DTModel = pickle.load(open('../ml/models/dt.pkl', 'rb'))
    self.RFCModel = pickle.load(open('../ml/models/rfc.pkl', 'rb'))
    self.GBCModel = pickle.load(open('../ml/models/gbc.pkl', 'rb'))
    self.vectorization = pickle.load(open('../ml/models/vectorizer.pkl', 'rb'))

  def fetchNewsContent(self, url: str) -> str:
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text
  
  def predict(self, articleText: str) -> str:
    testing_news = {"text": [articleText]}
    df_test = pd.DataFrame(testing_news)
    df_test['text'] = df_test['text'].apply(processText)
    x_test = df_test['text']
    xv_test = self.vectorization.transform(x_test)
    preds = [
      self.lRModel.predict(xv_test)[0], 
      self.DTModel.predict(xv_test)[0], 
      self.RFCModel.predict(xv_test)[0], 
      self.GBCModel.predict(xv_test)[0]
      ]
    print(f'{preds =}')
    return preds[2]
    # return np.bincount(preds).argmax()