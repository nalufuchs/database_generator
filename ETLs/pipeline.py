from database import db_connection as db
from sqlalchemy import text


def read_queries(query):
    with open(query, 'r') as file:
        query = file.read()
    return query


def process_tables():
    with db.session as connection:
        profitable_query = read_queries('profitable_products_query.sql')
        connection.execute(text(profitable_query))

        top100_query = read_queries('top_100_products_query.sql')
        connection.execute(text(top100_query))

        connection.commit()

        intersection_top100_and_profitable = read_queries('intersection_top100_and_profitable_products.sql')
        connection.execute(text(intersection_top100_and_profitable))

        connection.commit()

        print('Queries executadas com sucesso!')
