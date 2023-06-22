# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def math_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = add(a,b)
    return str(results)

@app.route('/sub')
def math_subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = sub(a,b)
    return str(results)

@app.route('/mult')
def math_multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = mult(a,b)
    return str(results)

@app.route('/div')
def math_divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = div(a,b)
    return str(results)

@app.route('/math/<func>')
def math_func(func):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    if func == 'add':
        results = add(a,b)

    if func == 'sub':
        results = sub(a,b)

    if func == 'mult':
        results = mult(a,b)

    if func == 'div':
        results = div(a,b)

    return str(results)

    