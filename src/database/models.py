from sqlalchemy import Integer, Text, DateTime, Column, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Spark(Base):
    __tablename__ = 'sparks'

    id = Column(Integer(), primary_key=True)
    content = Column(Text(), nullable=False)
    context = Column(Text(), nullable=False)
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())