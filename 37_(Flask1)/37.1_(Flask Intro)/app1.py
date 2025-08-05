from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def home():                    #view functions
    return render_template('index.html')

@app.route('/data/<name>/<int:age>')
def data(name, age): 
    return render_template('index.html', n=name, a=age)

@app.route('/details/<name>/<int:age>/<address>')
def user_data(name, age, address): 
    d={
        'Name':name,
        'Age':age,
        'Address':address
    }
    return render_template('index.html', data=d)

app.run(host='localhost', port=5000, debug=True)