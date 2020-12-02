from flask import *
from flask import request, flash, redirect
import requests
import mysql.connector
import os
import hashlib


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
#app.run(debug=True)


@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
	try:
		conn = connect_to_db()
		cursor = conn.cursor()
		query = "SELECT * FROM users WHERE username = %s"
		username = (request.form['username'], )
		password = request.form['password']


		#check if this username exists
		cursor.execute(query, username)

		results = cursor.fetchall()

		if len(results) == 0:
			flash('username not found')
		else:
			stored_key = results[0][1]
			salt = results[0][2]
			key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
			
			print(salt)
			print(key)
			print(stored_key)

			if stored_key == key:
				flash('authenticated')
				return redirect('http://127.0.0.1:3030/')
			else:
				flash('Incorrect password')
				return redirect('http://127.0.0.1:3030/')
		

	except Exception as e:
		print('Stress in login')
		print(e)


@app.route('/signup', methods = ['POST'])
def signup():
	try:
		conn = connect_to_db()
		cursor = conn.cursor()
		sql_statement = 'INSERT INTO users (username, pwdHash, salt, email) VALUES (%s, %s, %s, %s)'

		salt = os.urandom(32)
		password = request.form['password']
		key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

		values = (request.form['username'], str(key), str(salt), request.form['email'])
		cursor.execute(sql_statement, values)
		conn.commit()


		return redirect('http://127.0.0.1:3030/')

	except Exception as e:
		print('error in signing up')
		print(e)

def connect_to_db():
	try:
		file = open('C:\\project clean latests\\creds\\dbCredentials.txt', 'r')
		creds = file.read().split(',')
		conn = mysql.connector.connect(
		  host=creds[0],
		  user=creds[1],
		  password=creds[2],
		  database=creds[3]
		)
		file.close()
		return conn
	except:
		print('error in opening creds file or connecting to db')


app.run(port=3000)