# Internal libraries

# External libraries
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

# Define flask app
app = Flask(__name__,static_folder='static', static_url_path='')

'''
Routes:
    / : index
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_data():
    result = requests.get( request.args.get('url'))
    soup = BeautifulSoup(result.content, "lxml")
    results = soup.find_all( request.args.get('tag'))
    return render_template('result.html', results=results)

# Run App
if __name__ == '__main__':
    app.run(host= '0.0.0.0',port='5000')
