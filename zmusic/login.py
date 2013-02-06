from flask_login import LoginManager
from flask_login import current_user, UserMixin
from flask import request, abort, current_app as app
from functools import wraps


login_manager = LoginManager()

class User(UserMixin):
	def __init__(self, id, admin=False):
		self.admin = admin
		self.id = id

music_user = User("user")
admin_user = User("admin", True)

@login_manager.user_loader
def load_user(id):
	if id == "user":
		return music_user
	elif id == "admin":
		return admin_user
	return None

@login_manager.unauthorized_handler
def unauthorized():
	return abort(403)

def login_required(fn):
	@wraps(fn)
	def decorated_view(*args, **kwargs):
		if query_is_admin_user(request.args) or query_is_music_user(request.args) or current_user.is_authenticated():
			return fn(*args, **kwargs)
		return app.login_manager.unauthorized()
	return decorated_view

def admin_required(fn):
	@wraps(fn)
	def decorated_view(*args, **kwargs):
		if query_is_admin_user(request.args) or (current_user.is_authenticated() and current_user.admin):
			return fn(*args, **kwargs)
		return app.login_manager.unauthorized()
	return decorated_view

def query_is_music_user(query):
	username = query.get("username", None)
	password = query.get("password", None)
	return username == app.config["MUSIC_USER"] and password == app.config["MUSIC_PASSWORD"]

def query_is_admin_user(query):
	username = query.get("username", None)
	password = query.get("password", None)
	return username == app.config["ADMIN_USER"] and password == app.config["ADMIN_PASSWORD"]
