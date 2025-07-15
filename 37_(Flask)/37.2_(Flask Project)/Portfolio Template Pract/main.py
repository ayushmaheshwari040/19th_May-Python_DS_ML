from flask import Flask, render_template, request
import pymysql as sql

app = Flask(__name__)

def db_connect():
    conn = sql.connect(host='localhost', port=3306, user='root', password='', database='dsml12pm')
    cur = conn.cursor()
    return conn, cur

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('services.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/aftersubmit/', methods=['GET', 'POST'])
def aftersubmit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        conn, cur = db_connect()
        cmd = f"insert into flask_data values('{name}', '{email}', '{phone}', '{message}')"
        cur.execute(cmd)
        conn.commit()
        conn.close()
        msg = "Details are sent successfully..."
        return render_template('contact.html', m=msg)
    else:
        return render_template('contact.html')
    

app.run(debug=True)

