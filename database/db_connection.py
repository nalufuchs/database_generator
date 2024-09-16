from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database_url = 'postgresql://postgres:postgres@localhost/database_tester'
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
session = Session()



