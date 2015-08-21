"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText

from discariche.model.meta import Base

class Agent(Base):
    __tablename__ = "agent"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    
    __table_args__ = ( 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                    )

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return "<Agent'%s')" % self.name

