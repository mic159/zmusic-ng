from zmusic.endpoints.error import setup_errors
from zmusic.endpoints.login import login, login_check, logout
from zmusic.endpoints.query import query
from zmusic.endpoints.scan import scan_music
from zmusic.endpoints.song import song
from zmusic.endpoints.static import serve_static
from zmusic.endpoints.stats import stats_all_ips, stats_for_ip
from zmusic.endpoints.zip import zipfile

def load_endpoints(app):
	setup_errors(app)
	app.add_url_rule('/query', 'query', query, defaults={ "query": "" })
	app.add_url_rule('/query/', 'query2', query, defaults={ "query": "" })
	app.add_url_rule('/query/<path:query>', 'query3', query)
	app.add_url_rule('/login', 'login', login, methods=['POST'])
	app.add_url_rule('/login', 'login_check', login_check, methods=['GET'])
	app.add_url_rule('/logout', 'logout', logout)
	app.add_url_rule('/scan', 'scan', scan_music)
	app.add_url_rule('/song/<id>.<ext>', 'song', song)
	app.add_url_rule('/stats', 'stats_all', stats_all_ips)
	app.add_url_rule('/stats/<ip>', 'stats_for_ip', stats_for_ip)
	app.add_url_rule('/zip', 'zip', zipfile, methods=['POST'])
	app.add_url_rule('/', 'index', serve_static, defaults={ "filename": "index.html" })
	app.add_url_rule('/<path:filename>', 'static', serve_static)