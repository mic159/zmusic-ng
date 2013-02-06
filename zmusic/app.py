from pkg_resources import resource_filename
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from zmusic.database import db
from zmusic.endpoints import load_endpoints
from zmusic.login import login_manager

def main():
	app = Flask(__name__)
	app.config.from_pyfile(resource_filename('zmusic', 'app.cfg'))
	db.init_app(app)
	db.app = app
	login_manager.setup_app(app)
	
	load_endpoints(app)
	app.run()