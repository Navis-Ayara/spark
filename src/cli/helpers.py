from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database.models import Spark

engine = create_engine("sqlite:///sparks_store.db")

Session = sessionmaker(bind=engine)

session = Session()