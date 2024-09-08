from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from create_database_script import Base


database_url = 'postgresql://postgres:postgres@localhost/teste'
engine = create_engine(database_url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
