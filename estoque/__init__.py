from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria o engine
engine = create_engine('sqlite:///estoque.db')

# Cria a classe base
Base = declarative_base()

from estoque.models import *

Session = sessionmaker(bind=engine)
session = Session()

