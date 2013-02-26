from flask_login import LoginManager
from flask_login import current_user, UserMixin
from flask import request, redirect, current_app as app, url_for
from functools import wraps
from zmusic.database import User, db


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
	return db.session.query(User).get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
	return redirect(url_for('login.index'))