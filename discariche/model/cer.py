"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText

from discariche.model.meta import Base

class CerCode(Base):
    __tablename__ = "cer_code"

    id = Column(Integer, primary_key=True)
    code = Column(Unicode(56), nullable=False)
    description = Column(Unicode(512), nullable=False)
    
    __table_args__ = ( 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                    )

    def __init__(self, description=''):
        self.description = description

    def __repr__(self):
        return "<Cer('%s')" % self.description

