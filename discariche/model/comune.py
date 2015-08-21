"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText, Date, SmallInteger

from discariche.model.meta import Base

class Comune(Base):
    __tablename__ = "comune"

    id = Column(Integer, primary_key=True)
    codice_istat = Column(Unicode(6), nullable=False)
    denominazione = Column(Unicode(255), nullable=False)
    codice_regione_campania = Column(Unicode(3), nullable=False)
    descrizione_regione = Column(Unicode(255), nullable=False)
    codice_provincia = Column(Unicode(3), nullable=False)
    descrizione_provincia = Column(Unicode(3), nullable=False)
    codice_catastale = Column(Unicode(4), nullable=False)
    flag_statoestero = Column(SmallInteger, default=0)
    date_insert = Column(Date, nullable=False)
    date_delete = Column(Date)
    
    __table_args__ = ( 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                    )

    def __init__(self, description=''):
        self.description = description

    def __repr__(self):
        return "<Comune('%s')" % self.denominazione

