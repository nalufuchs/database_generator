from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(150), nullable=False)
    customer_email = Column(String(100), nullable=False)
    customer_cpf = Column(String(50), unique=True, nullable=False)

    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(150), nullable=False)
    sale_value = Column(Integer(), nullable=False)
    final_cost = Column(Integer(), nullable=False)

    order_products = relationship("OrderProduct", back_populates="product")


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    sale_time = Column(DateTime, default=datetime.datetime.utcnow)

    customer = relationship("Customer", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")


class OrderProduct(Base):
    __tablename__ = 'order_product'

    order_product_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.order_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    products_count = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_products")
    product = relationship("Product", back_populates="order_products")


