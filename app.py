#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

@app.route('/<endpoint>') # dynamic endpoint
def check_endpoint(endpoint):
    return 'Check endpoint - %s!\n' % endpoint

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone
   
