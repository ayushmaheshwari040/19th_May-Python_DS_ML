from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():                    #view functions
    return 'hello world'

@app.route('/index/')
def index(): 
    return "This is index page"

@app.route('/data/')
def data(): 
    return "<h1>This is first level heading of data page<h1>"

@app.route('/<name>/<int:age>')        # defining variable, by default string type
def details(name, age):
    return f"{name}\n{age}" 
    
@app.route('/details/<name>/<int:age>/<address>')
def user_data(name, age, address): 
    d={
        'name':name,
        'age':age,
        'address':address
    }
    return d

app.run(host='localhost', port=5000, debug=True)
