import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.secure import https
import discariche.lib.helpers as h
import discariche.lib.funcs as funcs
from datetime import datetime
from time import mktime, strptime

from discariche.model.meta import Session
# importa oggetti
from discariche.model import User, Status, Agent, DumpType, Dump, StatusDump, Reallocation, AgentDump, Quantity, Comune, CerCode, CerDump, BibMedia

from discariche.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AdminController(BaseController):
    
    requires_auth = ['index','changepass', 'adddump', 'adddt',\
                     'addstatus', 'addagent', 'moddump', 'modsubmit',\
                     'adddump', 'delstatusdump', 'delagentdump',\
                     'delquantity', 'delreallocation', 'viewdump', 'destroydump']
    
    @https()
    def index(self):
        # Return a rendered template
        #return render('/admin.mako')
        # or, return a string
        return render('/admin/adminindex.mako')

    @https()
    def changepass(self):
        if request.method == 'GET':
            return render('/admin/changepass.mako')
        if request.method == 'POST':
            user = request.POST.get('username')
            cp = request.POST.get('curpass')
            npa = request.POST.get('newpassa')
            npb = request.POST.get('newpassb')
        
            s = Session()
            rset = s.query(User).filter(User.username == user).all()

            if len(rset) < 1:
                c.error = 'Address does not exist'
                return render('/admin/changepass.mako')

            usr = rset[0]
            cparts = usr.password.split('$')
            salt = cparts[2]

            #print cparts[2] +' '+ cparts[3]

            oldmd = funcs.md5crypt(cp, salt)
            
            if (oldmd == usr.password):
                if (npa == npb):
                    usr.password = funcs.md5crypt(npa, funcs.genpasswd())
                    s.commit()
                    return render('/admin/changepass.mako')
                else:
                    c.error = 'Passwords do not match!'
                    return render('/admin/changepass.mako')
            else: 
                c.error = 'The old password is not correct'
                return render('/admin/changepass.mako')

    @https()
    def addstatus(self):
        if request.method == 'GET':
            c.s = Session.query(Status).all()
            return render('/admin/addstatus.mako')
        elif request.method == 'POST':
            ustat = request.POST.get('status')
           
            newstatus = Status()
            newstatus.description = ustat

            Session.add(newstatus)
            Session.commit()
             
            return render('/admin/ok.mako')
    
    @https()
    def addagent(self):
        if request.method == 'GET':
            c.a = Session.query(Agent).all()
            return render('/admin/addagent.mako')
        elif request.method == 'POST':
            uagent = request.POST.get('agent')
           
            newagent = Agent()
            newagent.name = uagent

            Session.add(newagent)
            Session.commit()
             
            return render('/admin/ok.mako')
    
    @https()
    def adddt(self):
        if request.method == 'GET':
            c.dt = Session.query(DumpType).all()
            return render('/admin/adddt.mako')
        elif request.method == 'POST':
            udt = request.POST.get('type')
           
            newdt = DumpType()
            newdt.type = udt

            Session.add(newdt)
            Session.commit()
             
            return render('/admin/ok.mako')

    @https()
    def adddump(self):
        if request.method == 'GET':
            return render('/admin/adddump.mako')
        elif request.method == 'POST':
            name = request.POST.get('name')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            description = request.POST.get('ddesc')
            history = request.POST.get('history')
            comune = request.POST.get('comune-id')            

            new_dump = Dump()
            new_dump.name = name
            new_dump.latitude = latitude
            new_dump.longitude = longitude
            new_dump.description = description
            new_dump.history = history
            new_dump.comune = comune

            Session.add(new_dump)
            Session.commit()
            
            i = 0
            stid_str = 'st-auto-id-'
            stid_sd = 'st-start-date-'
            stid_ed = 'st-end-date-'
            stid_notes = 'st-notes-'
            cur = request.POST.get(stid_str+str(i))
            
            while cur:
                if int(cur) != -1:
                    new_st = StatusDump()
                    new_st.id_dump = new_dump.id
                    new_st.id_status = cur
                    new_st.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(stid_sd+str(i)), "%d/%m/%Y")))
                    st_edate = request.POST.get(stid_ed+str(i))
                    if st_edate:
                        new_st.end_date = datetime.fromtimestamp(mktime(strptime(st_edate, "%d/%m/%Y")))
                    else:
                        new_st.end_date = None
                    new_st.notes = request.POST.get(stid_notes+str(i))
                    new_st.modder = session['custid']
                    new_st.lastmod = datetime.now()
                    
                    Session.add(new_st)
                i = i+1
                cur = request.POST.get(stid_str+str(i))
            
            
            i = 0
            dtid_str = 'dumptype-auto-id-'
            dtid_sd = 'dt-start-date-'
            dtid_ed = 'dt-end-date-'
            dtid_notes = 'dt-notes-'
            cur = request.POST.get(dtid_str+str(i))            

            while cur:
                if int(cur) != -1:
                    new_dt = Reallocation()
                    new_dt.id_dump = new_dump.id
                    new_dt.id_dumptype = cur
                    new_dt.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(dtid_sd+str(i)), "%d/%m/%Y")))
                    dt_edate = request.POST.get(dtid_ed+str(i))
                    if dt_edate:
                        new_dt.end_date = datetime.fromtimestamp(mktime(strptime(dt_edate, "%d/%m/%Y")))
                    else:
                        new_dt.end_date = None
                    new_dt.notes = request.POST.get(dtid_notes+str(i))
                    new_dt.modder = session['custid']
                    new_dt.lastmod = datetime.now()
                    
                    Session.add(new_dt)
                i = i+1
                cur =request.POST.get(dtid_str+str(i))
           

            i = 0
            agid_str = 'ag-auto-id-'
            agid_sd = 'ag-start-date-'
            agid_ed = 'ag-end-date-'
            cur = request.POST.get(agid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_ag = AgentDump()
                    new_ag.id_dump = new_dump.id
                    new_ag.id_agent = cur
                    new_ag.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(agid_sd+str(i)), "%d/%m/%Y")))
                    ag_edate = request.POST.get(agid_ed+str(i))
                    if ag_edate:
                        new_ag.end_date = datetime.fromtimestamp(mktime(strptime(ag_edate, "%d/%m/%Y")))
                    else:
                        new_ag.end_date = None
                    new_ag.modder = session['custid']
                    new_ag.lastmod = datetime.now()

                    Session.add(new_ag)
                i = i+1
                cur =request.POST.get(agid_str+str(i))

            i = 0
            qtyid_str = 'qty-'
            qtyid_sd = 'qty-start-date-'
            qtyid_ed = 'qty-end-date-'
            cur = request.POST.get(qtyid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_q = Quantity()
                    new_q.id_dump = new_dump.id
                    new_q.quantity = cur
                    new_q.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(qtyid_sd+str(i)), "%d/%m/%Y")))
                    q_edate = request.POST.get(qtyid_ed+str(i))
                    if q_edate:
                        new_q.end_date = datetime.fromtimestamp(mktime(strptime(q_edate, "%d/%m/%Y")))
                    else:
                        new_q.end_date = None
                    new_q.modder = session['custid']
                    new_q.lastmod = datetime.now()

                    Session.add(new_q)
                i = i+1
                cur =request.POST.get(qtyid_str+str(i))
            
            i = 0
            cerid_str = 'cer-auto-id-'
            cur = request.POST.get(cerid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_cd = CerDump()
                    new_cd.id_dump = new_dump.id
                    new_cd.id_cer = cur
                    new_cd.modder = session['custid']
                    new_cd.lastmod = datetime.now()

                    Session.add(new_cd)
                i = i+1
                cur =request.POST.get(cerid_str+str(i))

            i = 0
            bibtitle_str = 'bib-title-'
            biburl_str = 'bib-url-'
            bibtype_str = 'bib-type-'
            bibdate_str = 'bib-refdate-'

            cur_title = request.POST.get(bibtitle_str+str(i))
            cur_url = request.POST.get(biburl_str+str(i))
            if request.POST.get(bibdate_str+str(i)):
                cur_refdate = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
            else:
                cur_refdate = ''
            while cur_title:
                if (cur_title != '') and (cur_url != '') and (cur_refdate != ''):
                    new_bib = BibMedia()
                    new_bib.id_dump = new_dump.id
                    new_bib.description = cur_title
                    new_bib.url = request.POST.get(biburl_str+str(i))
                    new_bib.type = request.POST.get(bibtype_str+str(i))
                    new_bib.date_ref = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
                    new_bib.modder = session['custid']
                    new_bib.lastmod = datetime.now()

                    Session.add(new_bib)
                i = i+1
                cur_title = request.POST.get(bibtitle_str+str(i))
                cur_url = request.POST.get(biburl_str+str(i))
                if request.POST.get(bibdate_str+str(i)):
                    cur_refdate = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
                else:
                    cur_refdate = ''
     
            Session.commit()

            return render('/admin/adddump.mako')

    def moddump(self, id):
        if request.method == 'GET':
            
            c.dump = Session.query(Dump).filter(Dump.id == id).one()
            c.statusdump = Session.query(\
                            StatusDump.id.label('sd_id'),\
                            StatusDump.start_date.label('st_sdate'),\
                            StatusDump.end_date.label('st_edate'),\
                            StatusDump.notes.label('st_notes'),\
                            Status.id.label('st_id'),\
                            Status.description.label('st_desc')\
                        ).join(Status).\
                        filter(StatusDump.id_dump == id).all()
            if c.dump.comune:
                c.comune = Session.query(Comune).filter(Comune.id == c.dump.comune).one()
            else:
                c.comune = None
            
            c.agentdump = Session.query(\
                            AgentDump.id.label('ad_id'),\
                            AgentDump.start_date.label('ag_sdate'),\
                            AgentDump.end_date.label('ag_edate'),\
                            AgentDump.notes.label('ag_notes'),\
                            Agent.id.label('ag_id'),\
                            Agent.name.label('ag_name')
                        ).join(Agent).\
                        filter(AgentDump.id_dump == id).all()
            
            c.dumptype = Session.query(\
                            Reallocation.id.label('re_id'),\
                            Reallocation.start_date.label('dt_sdate'),\
                            Reallocation.end_date.label('dt_edate'),\
                            Reallocation.notes.label('dt_notes'),\
                            DumpType.id.label('dt_id'),\
                            DumpType.type.label('dt_type')
                        ).join(DumpType).\
                        filter(Reallocation.id_dump == id).all()

            c.qtydump = Session.query(\
                            Quantity.id.label('qty_id'),\
                            Quantity.start_date.label('qty_sdate'),\
                            Quantity.end_date.label('qty_edate'),\
                            Quantity.notes.label('qty_notes'),\
                            Quantity.quantity.label('qty_quantity')\
                        ).filter(Quantity.id_dump == id).all()
            
            c.cerdump = Session.query(\
                            CerDump.id.label('cd_id'),\
                            CerDump.id_cer.label('cd_cerid'),\
                            CerCode.id.label('cer_id'),\
                            CerCode.code.label('cer_code'),\
                            CerCode.description.label('cer_desc')\
                        ).join(CerCode).filter(CerDump.id_dump == id).all()
            
            c.bibdump = Session.query(\
                            BibMedia.id.label('bd_id'),\
                            BibMedia.description.label('bd_desc'),\
                            BibMedia.url.label('bd_url')\
                        ).filter(BibMedia.id_dump == id).all()
            #d = Session.query(\
            #        Dump,\
            #        StatusDump.start_date.label('st_sdate'),\
            #        StatusDump.end_date.label('st_edate'),\
            #        StatusDump.notes.label('st_notes'),\
            #        Status.description.label('st_desc'),\
            #        Status.id.label('st_id'),\
            #        AgentDump.start_date.label('ag_sdate'),\
            #        AgentDump.end_date.label('ag_edate'),\
            #        AgentDump.notes.label('ag_notes'),\
            #        Agent.name.label('ag_name'),\
            #        Agent.id.label('ag_id'),\
            #        Reallocation.start_date.label('dt_sdate'),\
            #        Reallocation.end_date.label('dt_edate'),\
            #        Reallocation.notes.label('dt_notes'),\
            #        DumpType.type.label('dt_type'),\
            #        DumpType.id.label('dt_id'),\
            #        Quantity.start_date.label('qty_sdate'),\
            #        Quantity.end_date.label('qty_edate'),\
            #        Quantity.quantity.label('qty_quantity'),\
            #        Quantity.notes.label('qty_notes')\
            #    ).join(StatusDump).join(Status).\
            #    join(AgentDump).join(Agent).\
            #    join(Reallocation).join(DumpType).\
            #    join(Quantity).all()
            
                    
            return render('/admin/moddump.mako')
        
    def modsubmit(self):    
        if request.method == 'POST':
            
            name = request.POST.get('name')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            description = request.POST.get('ddesc')
            history = request.POST.get('history')
            mainid = int(request.POST.get('mainid'))
            comune = request.POST.get('comune-id')
        
            new_dump = Session.query(Dump).filter(Dump.id == mainid).one()
            new_dump.name = name
            new_dump.latitude = latitude
            new_dump.longitude = longitude
            new_dump.description = description
            new_dump.history = history
            new_dump.comune = comune

            Session.commit()
            
            i = 0
            stid_str = 'st-auto-id-'
            stid_sd = 'st-start-date-'
            stid_ed = 'st-end-date-'
            stid_notes = 'st-notes-'
            cur = request.POST.get(stid_str+str(i))
            
            while cur:
                if int(cur) != -1:
                    new_st = StatusDump()
                    new_st.id_dump = new_dump.id
                    new_st.id_status = cur
                    new_st.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(stid_sd+str(i)), "%d/%m/%Y")))
                    st_edate = request.POST.get(stid_ed+str(i))
                    if st_edate:   
                        new_st.end_date = datetime.fromtimestamp(mktime(strptime(st_edate, "%d/%m/%Y")))
                    else:
                        new_st.end_date = None
                    new_st.notes = request.POST.get(stid_notes+str(i))
                    new_st.modder = session['custid']
                    new_st.lastmod = datetime.now()
                    
                    Session.add(new_st)
                i = i+1
                cur = request.POST.get(stid_str+str(i))
            
            
            i = 0
            dtid_str = 'dumptype-auto-id-'
            dtid_sd = 'dt-start-date-'
            dtid_ed = 'dt-end-date-'
            dtid_notes = 'dt-notes-'
            cur = request.POST.get(dtid_str+str(i))            

            while cur:
                if int(cur) != -1:
                    new_dt = Reallocation()
                    new_dt.id_dump = new_dump.id
                    new_dt.id_dumptype = cur
                    new_dt.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(dtid_sd+str(i)), "%d/%m/%Y")))
                    dt_edate = request.POST.get(dtid_ed+str(i))
                    if dt_edate:   
                        new_dt.end_date = datetime.fromtimestamp(mktime(strptime(dt_edate, "%d/%m/%Y")))
                    else:
                        new_dt.end_date = None
                    new_dt.notes = request.POST.get(dtid_notes+str(i))
                    new_dt.modder = session['custid']
                    new_dt.lastmod = datetime.now()
                    
                    Session.add(new_dt)
                i = i+1
                cur =request.POST.get(dtid_str+str(i))
           

            i = 0
            agid_str = 'ag-auto-id-'
            agid_sd = 'ag-start-date-'
            agid_ed = 'ag-end-date-'
            cur = request.POST.get(agid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_ag = AgentDump()
                    new_ag.id_dump = new_dump.id
                    new_ag.id_agent = cur
                    new_ag.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(agid_sd+str(i)), "%d/%m/%Y")))
                    ag_edate = request.POST.get(agid_ed+str(i))
                    if ag_edate:   
                        new_ag.end_date = datetime.fromtimestamp(mktime(strptime(ag_edate, "%d/%m/%Y")))
                    else:
                        new_ag.end_date = None
                    new_ag.modder = session['custid']
                    new_ag.lastmod = datetime.now()

                    Session.add(new_ag)
                i = i+1
                cur =request.POST.get(agid_str+str(i))

            i = 0
            qtyid_str = 'qty-'
            qtyid_sd = 'qty-start-date-'
            qtyid_ed = 'qty-end-date-'
            cur = request.POST.get(qtyid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_q = Quantity()
                    new_q.id_dump = new_dump.id
                    new_q.quantity = cur
                    new_q.start_date = datetime.fromtimestamp(mktime(strptime(request.POST.get(qtyid_sd+str(i)), "%d/%m/%Y")))
                    q_edate = request.POST.get(qtyid_ed+str(i))
                    if q_edate:   
                        new_q.end_date = datetime.fromtimestamp(mktime(strptime(q_edate, "%d/%m/%Y")))
                    else:
                        new_q.end_date = None
                    new_q.modder = session['custid']
                    new_q.lastmod = datetime.now()

                    Session.add(new_q)
                i = i+1
                cur =request.POST.get(qtyid_str+str(i))
            
            i = 0
            cerid_str = 'cer-auto-id-'
            cur = request.POST.get(cerid_str+str(i))

            while cur:
                if int(cur) != -1:
                    new_cd = CerDump()
                    new_cd.id_dump = new_dump.id
                    new_cd.id_cer = cur
                    new_cd.modder = session['custid']
                    new_cd.lastmod = datetime.now()

                    Session.add(new_cd)
                i = i+1
                cur = request.POST.get(cerid_str+str(i))
 
            i = 0
            bibtitle_str = 'bib-title-'
            biburl_str = 'bib-url-'
            bibtype_str = 'bib-type-'
            bibdate_str = 'bib-refdate-'

            cur_title = request.POST.get(bibtitle_str+str(i))
            cur_url = request.POST.get(biburl_str+str(i))
            if request.POST.get(bibdate_str+str(i)):
                cur_refdate = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
            else:
                cur_refdate = ''
            while cur_title:
                if (cur_title != '') and (cur_url != '') and (cur_refdate != ''):
                    new_bib = BibMedia()
                    new_bib.id_dump = new_dump.id
                    new_bib.description = cur_title
                    new_bib.url = request.POST.get(biburl_str+str(i))
                    new_bib.type = request.POST.get(bibtype_str+str(i))
                    new_bib.date_ref = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
                    new_bib.modder = session['custid']
                    new_bib.lastmod = datetime.now()

                    Session.add(new_bib)
                i = i+1
                cur_title = request.POST.get(bibtitle_str+str(i))
                cur_url = request.POST.get(biburl_str+str(i))
                if request.POST.get(bibdate_str+str(i)):
                    cur_refdate = datetime.fromtimestamp(mktime(strptime(request.POST.get(bibdate_str+str(i)), "%d/%m/%Y")))
                else:
                    cur_refdate = ''
            
            Session.commit()

            return render('/admin/adddump.mako')


    def delstatusdump(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(StatusDump).filter(StatusDump.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delagentdump(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(AgentDump).filter(AgentDump.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delreallocation(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(Reallocation).filter(Reallocation.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delquantity(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(Quantity).filter(Quantity.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delcerdump(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(CerDump).filter(CerDump.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delbibdump(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(BibMedia).filter(BibMedia.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def destroydump(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(Dump).filter(Dump.id == todel).one()
            Session.delete(obj)
            Session.commit() 
     
    def viewdump(self):
        if request.method == 'GET':
            c.dumps = Session.query(Dump).all()
            return render('/admin/viewdump.mako')
    
    def delexdt(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(DumpType).filter(DumpType.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delexstatus(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(Status).filter(Status.id == todel).one()
            Session.delete(obj)
            Session.commit() 
    
    def delexagent(self):
        if request.method == 'POST':
            todel = request.POST.get('id')
            obj = Session.query(Agent).filter(Agent.id == todel).one()
            Session.delete(obj)
            Session.commit() 
