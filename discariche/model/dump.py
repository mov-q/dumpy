"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText, DateTime, Numeric, Float

from discariche.model.meta import Base

class Dump(Base):
    __tablename__ = "dump"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    description = Column(Unicode(128))
    longitude = Column(Numeric(precision=20, scale=16), nullable=False)
    latitude = Column(Numeric(precision=20, scale=16), nullable=False)
    capacity = Column(Float, nullable=True)
    history = Column(UnicodeText(4294967295), nullable=True)
    user = Column(Integer, saschema.ForeignKey('user.id', onupdate="CASCADE", ondelete="SET NULL"))
    comune = Column(Integer, saschema.ForeignKey('comune.id', onupdate="CASCADE", ondelete="SET NULL"))
    
    __table_args__ = (saschema.UniqueConstraint("longitude","latitude"), 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } )

    def __init__(self, name='', long=0, lat=0):
        self.name = name
        self.long = long
        self.lat = lat

    def __repr__(self):
        return "<Dump('%s')" % self.name

