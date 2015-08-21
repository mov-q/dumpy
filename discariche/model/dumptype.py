"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText

from discariche.model.meta import Base

class DumpType(Base):
    __tablename__ = "dumptype"

    id = Column(Integer, primary_key=True)
    type = Column(Unicode(128), nullable=False)
    
    __table_args__ = ( 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                    )

    def __init__(self, type=''):
        self.type = type

    def __repr__(self):
        return "<DumpType('%s')" % self.type

