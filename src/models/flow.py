from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base  = declarative_base()

class Flow(Base):
    __tablename__ = 'flow'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String)