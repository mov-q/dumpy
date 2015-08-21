import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from discariche.model.meta import Session
# importa oggetti
from discariche.model import Dump, Reallocation, DumpType, AgentDump, Agent, Status, StatusDump, Quantity, Comune, CerCode, CerDump, BibMedia

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ShowController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/show.mako')
        # or, return a string
        return render('/show/index.mako')
    
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
    
    @jsonify
    def getNodeInfo(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(
                        Dump.id.label('id'),\
                        Dump.name.label('name'),\
                        Dump.description.label('description'),\
                        Dump.history.label('history'),\
                        Dump.longitude.label('longitude'),\
                        Dump.latitude.label('latitude'),\
                        Comune.denominazione.label('com'),\
                        Comune.descrizione_provincia.label('prov')\
                        ).join(Comune).filter(Dump.id == q)
            r = d.one()
            out =   {"id":str(r.id),\
                     "title":r.name,\
                     "desc":r.description,\
                     "history":r.history,\
                     "longitude":str(r.longitude),\
                     "latitude":str(r.latitude),\
                     "com":r.com,\
                     "prov":r.prov\
                    }
            return out
    
    @jsonify
    def getNodeDest(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    Reallocation.start_date.label('start_date'),\
                    Reallocation.end_date.label('end_date'),
                    Reallocation.notes.label('notes'),
                    DumpType.type.label('type')\
                ).\
                join(DumpType).\
                filter(Reallocation.id_dump == q).order_by(Reallocation.start_date.desc())
            res = d.all()
            out = {"res":[\
                    {"sd":str(r.start_date.month)+'/'+str(r.start_date.year),\
                     "ed":(str(r.end_date.month)+'/'+str(r.end_date.year)) if r.end_date else None,\
                     "type":r.type,\
                     "notes":r.notes\
                    } for r in res ]}
            return out
    
    @jsonify
    def getNodeAgent(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    AgentDump.start_date.label('start_date'),\
                    AgentDump.end_date.label('end_date'),
                    AgentDump.notes.label('notes'),
                    Agent.name.label('name')\
                ).\
                join(Agent).\
                filter(AgentDump.id_dump == q).order_by(AgentDump.start_date.desc())
            res = d.all()
            out = {"res":[\
                    {"sd":str(r.start_date.month)+'/'+str(r.start_date.year),\
                     "ed":(str(r.end_date.month)+'/'+str(r.end_date.year)) if r.end_date else None,\
                     "name":r.name,\
                     "notes":r.notes\
                    } for r in res ]}
            return out
    
    @jsonify
    def getNodeStatus(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    StatusDump.start_date.label('start_date'),\
                    StatusDump.end_date.label('end_date'),
                    StatusDump.notes.label('notes'),
                    Status.description.label('desc')\
                ).\
                join(Status).\
                filter(StatusDump.id_dump == q).order_by(StatusDump.start_date.desc())
            res = d.all()
            out = {"res":[\
                    {"sd":str(r.start_date.month)+'/'+str(r.start_date.year),\
                     "ed":(str(r.end_date.month)+'/'+str(r.end_date.year)) if r.end_date else None,\
                     "desc":r.desc,\
                     "notes":r.notes\
                    } for r in res ]}
            return out
    
    @jsonify
    def getNodeQuantity(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    Quantity.start_date.label('start_date'),\
                    Quantity.end_date.label('end_date'),
                    Quantity.notes.label('notes'),
                    Quantity.quantity.label('qty')\
                ).\
                filter(Quantity.id_dump == q).order_by(Quantity.start_date.desc())
            res = d.all()
            out = {"res":[\
                    {"sd":str(r.start_date.month)+'/'+str(r.start_date.year),\
                     "ed":(str(r.end_date.month)+'/'+str(r.end_date.year)) if r.end_date else None,\
                     "qty":r.qty,\
                     "notes":r.notes\
                    } for r in res ]}
            return out
    
    @jsonify
    def getNodeCer(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    CerCode.code.label('cer_code'),\
                    CerCode.description.label('cer_desc'),
                ).\
                join(CerDump).\
                filter(CerDump.id_dump == q).order_by(CerCode.code.asc())
            res = d.all()
            out = {"res":[\
                    {"code":r.cer_code,\
                     "desc":r.cer_desc\
                    } for r in res ]}
            return out
    
    @jsonify
    def getNodeBiblio(self):
        out = {"res":[]}
        if request.method == 'POST':
            q = request.POST.get('node')
            d = Session.query(\
                    BibMedia.description.label('bm_desc'),\
                    BibMedia.url.label('bm_url'),\
                    BibMedia.type.label('bm_type'),\
                    BibMedia.date_ref.label('bm_dref')\
                ).\
                filter(BibMedia.id_dump == q).order_by(BibMedia.date_ref.desc())
            res = d.all()
            out = {"res":[\
                    {"desc":r.bm_desc,\
                     "url":r.bm_url,\
                     "type":r.bm_type,\
                     "date":str(r.bm_dref.day)+"/"+str(r.bm_dref.month)+"/"+str(r.bm_dref.year)\
                    } for r in res ]}
            return out
