import populate_database as ppd
import SQLquery as sq


if __name__ == '__main__':
    customers = ppd.create_customers(1000)
    products = ppd.create_products(500)
    orders = ppd.create_orders(customers, 5)
    ppd.create_order_products(orders, products, 5)
    print('Clientes inseridos com sucesso!')
    queries = sq.process_tables()

