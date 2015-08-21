#!/var/www/marco@shift-left.net/chroot/disc.sleft.net/virtpy/bin/python
# setup the virtualenv
import os
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = '/var/www/marco@shift-left.net/chroot/disc.sleft.net/virtpy/bin:' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = '/var/www/marco@shift-left.net/chroot/disc.sleft.net/virtpy'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/marco@shift-left.net/chroot/disc.sleft.net/virtpy/egg_cache'

os.chdir('/var/www/marco@shift-left.net/chroot/disc.sleft.net/disc.sleft.net-html/')
import sys

# Add a custom Python path.
#sys.path.insert(0, "/var/admin/graphite/webapp/web")
#sys.path.insert(0, "/var/admin/graphite/webapp")

# Load the WSGI application from the config file
from paste.deploy import loadapp
wsgi_app = loadapp('config:/var/www/marco@shift-left.net/chroot/disc.sleft.net/disc.sleft.net-html/development.ini')

# Deploy it using FastCGI
if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(wsgi_app).run()
