from database import populate_database as ppd
from database import db_connection as db
from sqlalchemy import text


if __name__ == '__main__':

    is_table_populates = """
    SELECT COUNT(*) as total FROM customers 
    UNION
    SELECT COUNT(*) FROM products
    UNION 
    SELECT COUNT(*) FROM order_products
    UNION
    SELECT COUNT(*) FROM orders"""

    with db.engine.connect() as connection:
        count = connection.execute(text(is_table_populates)).scalar()
        if count != 0:
            print('ERROR! Tables is already populated.')
            exit()

    customers = ppd.create_customers(5000)
    products = ppd.create_products(1000)
    orders = ppd.create_orders(customers, 5)
    ppd.create_order_products(orders, products, 5)
    print('Customers, their orders and products successfully inserted!')