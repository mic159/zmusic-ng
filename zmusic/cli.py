from zmusic.database import db, User
from getpass import getpass
import zmusic.app
import argparse

def create_db():
	app = zmusic.app.create_app()
	print 'Creating new database at: ', app.config['SQLALCHEMY_DATABASE_URI']
	db.drop_all()
	db.create_all()
	admin = User()
	admin.username = 'admin'
	admin.is_admin = True
	admin.password = getpass('New admin password: ')
	session = db.session()
	session.add(admin)
	session.commit()