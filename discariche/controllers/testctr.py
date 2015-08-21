import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from discariche.model.meta import Session
# importa oggetti
from discariche.model import Dump

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TestctrController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/testctr.mako')
        # or, return a string
        return render('/testctr/testctrindex.mako')
    
    @jsonify
    def getCoords(self):
        out = {"res":[]}
        if request.method == 'GET':
            q = request.GET.get('input')
            d = Session.query(Dump)
            res = d.all()
            out = {"res":[\
                    {"id":str(r.id),\
                     "title":r.name,\
                     "longitude":str(r.longitude),\
                     "latitude":str(r.latitude)\
                    } for r in res ]}
            return out
