"""The application's model objects"""
from discariche.model.meta import Session, Base
import discariche.lib.helpers as h

from discariche.model.comune import Comune
from discariche.model.cer import CerCode
from discariche.model.agent import Agent
from discariche.model.status import Status
from discariche.model.dumptype import DumpType
from discariche.model.user import User
from discariche.model.dump import Dump
from discariche.model.agentdump import AgentDump
from discariche.model.statusdump import StatusDump
from discariche.model.reallocation import Reallocation
from discariche.model.cerdump import CerDump
from discariche.model.quantity import Quantity
from discariche.model.bibmedia import BibMedia



def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

