from faker import Faker
import random
import db_connection as db
import create_database as cds


fake = Faker()

def create_customers(n):
    customers = []
    for _ in range(n):
        customer = cds.Customer(
            customer_name=fake.name(),
            customer_email=fake.email(),
            customer_cpf=fake.unique.ssn()
        )
        db.session.add(customer)
        customers.append(customer)
    db.session.commit()
    return customers

def create_products(n):
    products = []
    for _ in range(n):
        product = cds.Product(
            product_name=fake.word(),
            sale_value=random.randint(1000, 10000),
            final_cost=random.randint(500, 9000)
        )
        db.session.add(product)
        products.append(product)
    db.session.commit()
    return products

def create_orders(customers, num_orders_per_customer):
    orders = []
    for customer in customers:
        for _ in range(num_orders_per_customer):
            sale_time = fake.date_time_between(start_date='-3y', end_date='now')
            order = cds.Order(
                customer_id=customer.customer_id,
                sale_time=sale_time
            )
            db.session.add(order)
            orders.append(order)
    db.session.commit()
    return orders

def create_order_products(orders, products, max_products_per_order):
    for order in orders:
        num_products = random.randint(1, max_products_per_order)
        selected_products = random.sample(products, num_products)
        for product in selected_products:
            order_product = cds.OrderProduct(
                order_id=order.order_id,
                product_id=product.product_id,
                products_count=random.randint(1, 10)
            )
            db.session.add(order_product)
    db.session.commit()