from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cpf_cnpj = Column(String(14), unique=True, nullable=False, comment='Aceita inserção de CPF ou CNPJ')
    #AJEITAR O LANCE DO CPF DPS

    order = relationship("Orders", back_populates="customer", cascade='all, delete-orphan')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    sale_value = Column(DECIMAL(), nullable=False)
    final_cost = Column(DECIMAL(), nullable=False)

    order_product = relationship("OrderProducts", back_populates="product")


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    sale_time = Column(DateTime, default=datetime.datetime.utcnow)

    customer = relationship("Customers", back_populates="order")
    order_product = relationship("OrderProducts", back_populates="order")


class OrderProducts(Base):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    products_count = Column(Integer, nullable=False)

    order = relationship("Orders", back_populates="order_product")
    product = relationship("Products", back_populates="order_product")
