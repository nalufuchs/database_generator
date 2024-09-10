from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base


database_url = 'postgresql://postgres:postgres@localhost/database_tester'
engine = create_engine(database_url)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

