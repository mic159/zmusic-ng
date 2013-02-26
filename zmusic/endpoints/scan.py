from zmusic.database import db, Song
from zmusic.picard.formats import open as readtags
from zmusic.picard.util import encode_filename
from flask import Response, current_app as app
from flask.ext import login
import time
import os

@login.login_required
def scan_music():
	db.create_all();
	def do_scan(root_path):
		yield "%i | Begin.\n" % int(time.time())
		all_files = {}
		for root, dirs, files in os.walk(unicode(root_path)):
			if len(files) != 0:
				yield "%i | Scanning [%s].\n" % (int(time.time()), encode_filename(root))
			for name in files:
				name = encode_filename(os.path.join(root, name))
				all_files[name] = True
				song = Song.query.get(name)
				if song != None:
					stat = os.stat(name)
					if song.lastmodified == stat.st_mtime and song.filesize == stat.st_size:
						continue
				else:
					song = Song()
				try:
					tags = readtags(name)
				except:
					tags = None
				if tags == None:
					yield "%i | Skipping [%s].\n" % (int(time.time()), name)
					continue
				song.sync_picard(tags)
				db.session.add(song)
				yield "%i | Adding [%s].\n" % (int(time.time()), encode_filename(song.filename))
		for song in db.session.query(Song.filename):
			if song.filename not in all_files:
				Song.query.filter(Song.filename == song.filename).delete(False)
				yield "%i | Removing [%s].\n" % (int(time.time()), encode_filename(song.filename))
		db.session.commit()
		yield "%i | Done.\n" % int(time.time())
	response = Response(do_scan(app.config["MUSIC_PATH"]), mimetype="text/plain", direct_passthrough=True)
	response.headers.add("X-Accel-Buffering", "no")
	response.cache_control.no_cache = True
	return response
