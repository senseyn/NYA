from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sys

print("Python версия:", sys.version)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nya_v2.db'
db = SQLAlchemy(app)


app.route("/index")
@app.route("/")
def index():
	return render_template('/user/index.html')


@app.route("/login")
def login():
	return render_template('/user/login.html')


@app.route("/player")
def player():
	return render_template('/user/player.html')


#---ЭКСПЕРЕМЕНТАЛЬНЫЙ ФАЙЛ----#

#------------------------------

if __name__ == "__main__":
	print("ЗАПУСК СЕРВЕРА")
	app.run(host='0.0.0.0', port=5000, debug=True)