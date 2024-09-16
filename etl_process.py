from ETLs import pipeline as pl
from database import db_connection as db
from sqlalchemy import text


if __name__ == '__main__':

    if_table_exists = """
    SELECT COUNT(*) AS total_tables
    FROM information_schema.tables
    WHERE table_name IN ('top_100_products_sold', 'profitable_products')"""

    with db.engine.connect() as connection:
        count = connection.execute(text(if_table_exists)).scalar()
        if count != 0:
            print('ERROR! Those tables were already created.')
            exit()

    queries = pl.process_tables()

