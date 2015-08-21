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

class DumptypeController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/dumptype.mako')
        # or, return a string
        return 'Hello World'

    @jsonify
    def dumptype_jac(self):
        out = {"res":[]}
        if request.method == 'GET':
            name = request.GET.get('input')
            ac_q = Session.query(DumpType)
            try:
                res = ac_q.filter(DumpType.type.like("%"+name+"%")).limit(15)
            except:
                return out
            else:
                out = {"res":[{"id":str(r.id), "type":r.type} for r in res]}
                return out
        else:
            return out

