from zmusic.endpoints.error import setup_errors
from zmusic.endpoints.login import Login, Logout
from zmusic.endpoints.query import query
from zmusic.endpoints.scan import scan_music
from zmusic.endpoints.song import song
from zmusic.endpoints.static import serve_static, AdminStatic
from zmusic.endpoints.stats import stats_all_ips, stats_for_ip
from zmusic.endpoints.zip import zipfile
from zmusic.endpoints.admin import ScanFolders, Home, UserManager
from flask.ext import admin

def load_endpoints(app):
	setup_errors(app)
	app.add_url_rule('/query', 'query', query, defaults={ "query": "" })
	app.add_url_rule('/query/', 'query2', query, defaults={ "query": "" })
	app.add_url_rule('/query/<path:query>', 'query3', query)
	app.add_url_rule('/scan', 'scan', scan_music)
	app.add_url_rule('/song/<id>.<ext>', 'song', song)
	app.add_url_rule('/stats', 'stats_all', stats_all_ips)
	app.add_url_rule('/stats/<ip>', 'stats_for_ip', stats_for_ip)
	app.add_url_rule('/zip', 'zip', zipfile, methods=['POST'])
	app.add_url_rule('/static/<path:filename>', 'static', serve_static)
	app_admin = admin.Admin(app, name='zmusic-ng', index_view=Home(name='Music', url='/'))
	app_admin.add_view(ScanFolders(name='Scan music directory', endpoint='scan', category='Admin', url='/scan'))
	app_admin.add_view(UserManager(name='Manage Users', endpoint='users', category='Admin', url='/users'))
	app_admin.add_view(AdminStatic())
	app_admin.add_view(Login(name='Login', endpoint='login', url='/login'))
	app_admin.add_view(Logout(name='Logout', endpoint='logout', url='/logout'))