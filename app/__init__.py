#init.py by Usu Edeaghe

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'
app.config['SECRET_KEY'] = 'my-first-flask-application'

# Database Instance
db = SQLAlchemy(app)


from app import routes