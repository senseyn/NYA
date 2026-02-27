from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sys

print("Python версия:", sys.version)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nya_v2.db'
db = SQLAlchemy(app)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	text =db.Column(db.Text, nullable=False)


app.route("/index")
@app.route("/")
def index():
	if request.method == 'POST':
		print(request.form['title'])
		print(request.form['text'])
		return redirect('/')
	else:
		return render_template('login.html')


@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/create", methods=['POST', 'GET'])
def create():
	if request.method == 'POST':
		print(request.form['title'])
		print(request.form['text'])
		return redirect('/')
	else:
		return render_template('create.html')


if __name__ == "__main__":
	print("ЗАПУСК СЕРВЕРА")
	app.run(host='0.0.0.0', port=5000, debug=True)