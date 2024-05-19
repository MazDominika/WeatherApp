from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'HasloPracaInzynierska'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://mazdomin:3B2GccHfjm3KuA8K@mysql.agh.edu.pl/mazdomin'
db = SQLAlchemy(app)

login = LoginManager(app)

from app import routes