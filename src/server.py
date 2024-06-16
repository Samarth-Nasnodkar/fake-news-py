from flask import Flask, render_template, request
from utils.news import News

app = Flask(__name__)
news = News()

@app.route('/', methods=['GET'])
def home():
  # render page stored in ./frontend/index.html
  return render_template('index.html')

@app.route('/details', methods=['GET'])
def details():
  url = request.args.get('url')
  articleContent = news.fetchNewsContent(url)
  return render_template('details.html', content=articleContent)

@app.route('/result', methods=['GET', 'POST'])
def result():
  articleText = request.form['article-text']
  prediction = news.predict(articleText)
  result = ''
  bgColor = ''
  if prediction == 0:
    result = 'Fake'
    bgColor = 'darkred'
  else:
    result = 'Real'
    bgColor = 'green'
  
  return render_template('result.html', result=result, bgColor=bgColor)

if __name__ == '__main__':
  app.run('0.0.0.0', port=8000, debug=True)