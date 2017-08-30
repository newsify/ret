# Internal libraries
import re

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

@app.route('/get/bytag')
def getbytag():
    result = requests.get( request.args.get('url'))
    soup = BeautifulSoup(result.content, "lxml")
    results = soup.find_all( request.args.get('tag'))
    return render_template('result.html', results=results)

@app.route('/get/intext')
def findintext():
    result = requests.get( request.args.get('url'))
    soup = BeautifulSoup(result.content, "lxml")
    results = soup.body.findAll(text=re.compile( request.args.get('text') ))
    return render_template('result.html', results=results)

@app.route('/get/inattr')
def findinattr():
    result = requests.get( request.args.get('url'))
    soup = BeautifulSoup(result.content, "lxml")
    attribute = request.args.get('attr')
    results = soup.findAll(attrs={request.args.get('attr') : re.compile( request.args.get('text') )})
    return render_template('result.html', results=results)

# Run App
if __name__ == '__main__':
    app.run(host= '0.0.0.0',port='5000')
