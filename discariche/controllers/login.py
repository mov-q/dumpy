import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import discariche.lib.helpers as h
import discariche.lib.funcs as funcs
from pylons.decorators.secure import https

from discariche.model.meta import Session
# importa oggetti
from discariche.model import User

from discariche.lib.base import BaseController, render


log = logging.getLogger(__name__)

class LoginController(BaseController):

    @https()
    def index(self):
        """
        Show login form. Submits to /login/submit
        """
        return render('/login/loginindex.mako')

    @https()
    def submit(self):
        """
        Verify username and password
        """
        # Both fields filled?
        form_username = str(request.params.get('username'))
        form_password = str(request.params.get('password'))

        # Get user data from database
        s = Session()
        rset = s.query(User).filter(User.username == form_username).all()
        if len(rset) < 1: # User does not exist
            return render('/login/loginindex.mako')

        usr = rset[0]
        cparts = usr.password.split('$')
        salt = cparts[2]
        oldmd = funcs.md5crypt(form_password, salt)
        
        # Wrong password? (MD5 hashes used here)
        if oldmd  != usr.password:
            c.loginerror = True
            return render('/login/loginindex.mako')

        cookie_string = funcs.simplemd5(form_username + request.environ['REMOTE_ADDR'])
        # should set the cookie based here
        response.set_cookie('discsleftnet', cookie_string, expires='3600')
     
        # Mark user as logged in
        session['user'] = form_username
        session['custid'] = usr.id
        session['cur_cookie'] = cookie_string
        session.save()

        # Send user back to the page he originally wanted to get to
        if session.get('path_before_login'):
            redirect(session['path_before_login'])
        else: # if previous target is unknown just send the user to a welcome page
            return render('/login/loggedin.mako')

    def logout(self):
        """
        Logout the user and display a confirmation message
        """
        if 'user' in session:
            del session['user']
            session.save()
        return render('/login/loginindex.mako')

