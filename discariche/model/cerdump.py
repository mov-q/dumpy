"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText, DateTime

from discariche.model.meta import Base

class CerDump(Base):
    __tablename__ = "cer_dump"

    id = Column(Integer, primary_key=True)
    id_dump = Column(Integer, saschema.ForeignKey('dump.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_cer = Column(Integer, saschema.ForeignKey('cer_code.id',onupdate="CASCADE", ondelete="SET NULL"))
    notes = Column(Unicode(512), nullable=True)
    modder = Column(Integer, saschema.ForeignKey('user.id', onupdate="CASCADE", ondelete="SET NULL"))
    lastmod = Column(DateTime, nullable=False)
    
    __table_args__ = (
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                     )

    def __init__(self):
        pass

    def __repr__(self):
        pass

