import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.secure import https
from pylons.decorators import jsonify
import discariche.lib.helpers as h
import discariche.lib.funcs as funcs
from datetime import datetime
from time import mktime, strptime

from discariche.model.meta import Session
# importa oggetti
from discariche.model import Comune

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ComuniController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/comuni.mako')
        # or, return a string
        return 'Hello World'

    @jsonify
    def comuni_jac(self):
        out = {"res":[]}
        if request.method == 'GET':
            name = request.GET.get('input')
            ac_q = Session.query(Comune)
            try:
                res = ac_q.filter(Comune.denominazione.like("%"+name+"%")).limit(15)
            except:
                return out
            else:
                out = {"res":[{"id":str(r.id), "name":r.denominazione} for r in res]}
                return out
        else:
            return out
