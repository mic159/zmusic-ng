from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext import admin, login
from zmusic.login import login_manager
from zmusic.database import db, User

class Home(admin.BaseView):
	@admin.expose()
	@login.login_required
	def index(self):
		return self.render('music.html')

class AdminView(admin.BaseView):
	def is_accessible(self):
		if not login.current_user.is_authenticated():
			return False
		return login.current_user.is_admin

class ScanFolders(AdminView):
	@admin.expose()
	def index(self):
		return self.render('admin/index.html')

class UserManager(ModelView, AdminView):
	def __init__(self, **options):
		super(UserManager, self).__init__(User, db.session, **options)