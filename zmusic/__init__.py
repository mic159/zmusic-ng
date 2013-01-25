from pkg_resources import resource_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile(resource_filename('zmusic', 'app.cfg'))

db = SQLAlchemy(app)

login_manager = LoginManager()
import zmusic.login
login_manager.setup_app(app)

import zmusic.endpoints

def main():
	app.run()
