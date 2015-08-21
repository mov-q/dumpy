"""Person model"""
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import schema as saschema
from sqlalchemy.types import Integer, String, Unicode, Float, UnicodeText, Date, DateTime

from discariche.model.meta import Base

class BibMedia(Base):
    __tablename__ = "bib_media"

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(128), nullable=False)
    url = Column(Unicode(1024), nullable=False)
    type = Column(Unicode(64), nullable=False)
    id_dump = Column(Integer, saschema.ForeignKey('dump.id', onupdate="CASCADE", ondelete="CASCADE"))
    date_ref = Column(Date, nullable=False)
    modder = Column(Integer, saschema.ForeignKey('user.id', onupdate="CASCADE", ondelete="SET NULL"))
    lastmod = Column(DateTime, nullable=False)
    
    __table_args__ = ( 
                        {
                         "mysql_engine":"InnoDB",
                         "mysql_charset":"utf8"
                         } 
                    )

    def __init__(self, description=''):
        self.description = description

    def __repr__(self):
        return "<BibMedia('%s')" % self.descrition

