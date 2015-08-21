"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText, DateTime

from discariche.model.meta import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(45), nullable=False)
    password = Column(Unicode(128), nullable=False)
    created = Column(DateTime, nullable=False)
    
    __table_args__ = (saschema.UniqueConstraint("username"), 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } )

    def __init__(self, username='', long=0, lat=0, created=None):
        self.username = username
        self.password = password
        self.created = created

    def __repr__(self):
        return "<User('%s')" % self.username

