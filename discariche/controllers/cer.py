import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from sqlalchemy.decorators import jsonify

from sqlalchemy import or_, and_
from pylons.model import Cer

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CerController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/cer.mako')
        # or, return a string
        return 'Hello World'

    @jsonify
    def cer_jac(self):
        out = {"res":[]}
        if request.method == 'GET':
            udesc = request.GET.get('input')
            ac_q = Session.query(Cer)
            try:
                res = ac_q.filter(or_(Cer.description.like("%"+udesc+"%")),(Cer.code.like("%"+udesc+"%"))).\
                    limit(30)
            except:
                return out
            else:
                out = {"res":[{"id":str(r.id), "desc":r.code+' '+r.description +, "code":r.code} for r in res]}
                return out
        else:
            return out

