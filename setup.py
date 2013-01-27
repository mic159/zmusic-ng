from setuptools import setup, find_packages

setup( name = 'zmusic-ng'
	 , version = '1.0'

	 , author = 'Jason A. Donenfeld'
	 , author_email = 'Jason@zx2c4.com'
	 , description = 'ZX2C4 Music provides a web interface for playing and downloading music files using metadata.'
	 , license = 'GPLv2'

	 , packages = find_packages()
	 , package_data = {
		'zmusic': [ 'frontend/js/scripts.min.js'
				  , 'frontend/css/styles.min.css'
	 			  , 'frontend/index.html'
	 			  , 'frontend/stats.html'
	 			  , 'frontend/robots.txt'
	 			  , 'frontend/favicon.ico'
	 			  , 'frontend/font/*'
				  , 'app.cfg'
	 			  ]
	 }
	 , entry_points = {
	 	'console_scripts': [
	 		'zmusic-ng = zmusic:main',
	 	]
	 }
	 , install_requires = 
	 	[ 'flask'
	 	, 'flask-login'
	 	, 'flask-sqlalchemy'
	 	, 'mutagen'
	 	]
)
