from flask import Response, send_from_directory, current_app as app
from pkg_resources import resource_filename
from mimetypes import guess_type
import os

def serve_static(filename):
	static_dir = resource_filename('zmusic', 'frontend')
	if app.config["ACCEL_STATIC_PREFIX"]:
		mimetype = None
		types = guess_type(os.path.join(static_dir, filename))
		if len(types) != 0:
			mimetype = types[0]
		response = Response(mimetype=mimetype)
		response.headers.add("X-Accel-Redirect", os.path.join(app.config["ACCEL_STATIC_PREFIX"], filename))
		return response
	else:
		return send_from_directory(static_dir, filename)
