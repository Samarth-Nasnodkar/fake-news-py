from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  # render page stored in ./frontend/index.html
  return render_template('index.html')

@app.route('/details', methods=['GET'])
def details():
  url = request.args.get('url')
  return '<h1>' + url + '</h1>'

if __name__ == '__main__':
  app.run('0.0.0.0', port=8000, debug=True)