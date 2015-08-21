import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import discariche.lib.helpers as h
from pylons.decorators import jsonify

from discariche.model.meta import Session
# importa oggetti
from discariche.model import User, Status, Agent, DumpType

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class StatusController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/status.mako')
        # or, return a string
        return 'Hello World'
    
    @jsonify
    def status_jac(self):
        out = {"res":[]}
        if request.method == 'GET':
            udesc = request.GET.get('input')
            ac_q = Session.query(Status)
            try:
                res = ac_q.filter(Status.description.like("%"+udesc+"%")).limit(15)
            except:
                return out
            else:
                out = {"res":[{"id":str(r.id), "desc":r.description} for r in res]}
                return out
        else:
            return out

