
from flask import Flask, jsonify, make_response, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    return 'Index Page'

@app.route('/hello')
def hello(): 
    return 'Hello, World'

if __name__ == '__main__':
    app.run()
