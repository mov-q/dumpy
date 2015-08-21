import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from sqlalchemy.sql import or_, and_
from discariche.model import CerCode
from discariche.model.meta import Session

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CercodeController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/cercode.mako')
        # or, return a string
        return 'Hello World'
    
    @jsonify
    def cer_jac(self):
        out = {"res":[]}
        if request.method == 'GET':
            udesc = request.GET.get('input')
            ac_q = Session.query(CerCode)
            try:
                res = ac_q.filter(or_(CerCode.description.like('%'+udesc+'%'),CerCode.code.like("%"+udesc+"%"))).\
                        limit(20)
                #res = ac_q.filter(Cer.description.like("%"+udesc+"%")).\
                #        all().limit(30)
            except:
                return out
            else:
                out = {"res":[{"id":str(r.id), "desc":r.code+' '+r.description, "code":r.code} for r in res]}
                return out
        else:
            return out

