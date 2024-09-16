from database import db_connection as db
from database.create_database import Base
from sqlalchemy import text


if __name__ == '__main__':

    if_table_exists = """
    SELECT COUNT(*) AS total_tables
    FROM information_schema.tables
    WHERE table_name IN ('customers', 'orders', 'products', 'order_products')"""

    with db.engine.connect() as connection:
        count = connection.execute(text(if_table_exists)).scalar()
        if count != 0:
            print('ERROR! Tables already exists.')
            exit()

    Base.metadata.create_all(db.engine)
    print('Tabelas criadas com sucesso!')