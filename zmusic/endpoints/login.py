from flask import request, redirect, url_for
from flask.ext import admin, wtf, login
from zmusic.database import db, User

# Define login and registration forms (for flask-login)
class LoginForm(wtf.Form):
	username = wtf.TextField(validators=[wtf.required()])
	password = wtf.PasswordField(validators=[wtf.required()])

	def validate_login(self, field):
		user = self.get_user()

		if user is None:
			raise wtf.ValidationError('Invalid user')

		if user.password != self.password.data:
			raise wtf.ValidationError('Invalid password')

	def get_user(self):
		return db.session.query(User).filter_by(username=self.username.data).first()

class Login(admin.BaseView):
	def is_accessible(self):
		return not login.current_user.is_authenticated()
	@admin.expose(methods=('GET', 'POST'))
	def index(self):
		form = LoginForm(request.form)
		if form.validate_on_submit():
			user = form.get_user()
			login.login_user(user)
			return redirect(url_for('home.index'))
		return self.render('login.html', form=form)

class Logout(admin.BaseView):
	def is_accessible(self):
		return login.current_user.is_authenticated()
	@admin.expose()
	def index(self):
		login.logout_user()
		return redirect(url_for('home.index'))