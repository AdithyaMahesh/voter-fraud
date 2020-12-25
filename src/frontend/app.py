from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session 
import datetime
import json
from hashlib import sha256
import requests
from sql_con import verify
from flask_mysqldb import MySQL
import MySQLdb.cursors 
import re 


app = Flask(__name__)

app.secret_key = 'secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql123rootpswd'
app.config['MYSQL_DB'] = 'sampledb'


mysql = MySQL(app)

@app.route('/') 
@app.route('/login', methods =['GET', 'POST'])
def login(): 
	msg = '' 
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
		username = request.form['username'] 
		password = request.form['password'] 
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, )) 
		account = cursor.fetchone() 
		if account: 
			session['loggedin'] = True
			session['id'] = account['id'] 
			session['username'] = account['username'] 
			msg = 'Logged in successfully !'
			return render_template('home.html', msg = msg) 
		else: 
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)


@app.route('/logout') 
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect(url_for('login'))

    

CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"



posts = []


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/', methods=['GET'])
def index():
    fetch_posts()
    return render_template('index.html',
                           title='Voter Dashboard',
                           votes=[],
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/error', methods=['GET'])
def index3():
    return render_template('error.html',
                           title='Voter Dashboard',
                           votes=[],
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/votes', methods=['GET'])
def index2():
    fetch_posts()
    return render_template('index2.html',
                           title='Blockchain Votes',
                           votes=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/changeNode', methods=['GET'])
def changeNode():
    CONNECTED_NODE_ADDRESS = "http://127.0.0.1:9000"
    return f'changed node to pper node {CONNECTED_NODE_ADDRESS}'


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    author = request.form["author"]
    password = request.form["password"]
    dob = request.form["dob"]
    response = verify(author, password, dob)
    print("Got: ", post_content, author, password, dob, response)

    if response:
        post_object = {
            'author': author,
            'content': sha256(post_content.encode()).hexdigest(),
        }

        # Submit a transaction
        new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

        requests.post(new_tx_address, json=post_object, headers={'Content-type': 'application/json'})

        return redirect('/')   
    else:
        return redirect('/error')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
