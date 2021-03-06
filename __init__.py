from flask import Flask

from config import config

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from Avenger_Phone_App import routes,models