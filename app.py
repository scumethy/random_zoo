import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object('config')
os.makedirs(config.PATH_TO_IMAGES, exist_ok=True)

db = SQLAlchemy(app)

from views.animal import animal
from views.history import history
app.register_blueprint(animal)
app.register_blueprint(history)

db.create_all()

if __name__ == '__main__':
    app.run()
