"""Orders, Order_Details"""

from __future__ import annotations

from datetime import date

from sqlalchemy import Date, Float, ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class OrderDetails(Base):
    """Промежуточная модель Подробности заказа."""

    __tablename__ = 'order_details'

    order_id: Mapped[int] = mapped_column(
        ForeignKey('orders.order_id', ondelete='CASCADE'),
        nullable=False,
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.product_id', ondelete='CASCADE'),
        nullable=False,
    )
    unit_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
    )
    discount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )


class Orders(Base):
    """Модель Заказов."""

    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey('customers.customer_id', ondelete='CASCADE'),
        nullable=True,
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey('employees.employee_id', ondelete='CASCADE'),
        nullable=True,
    )
    order_date: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )
    required_date: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )
    shipped_date: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )
    ship_via: Mapped[int] = mapped_column(
        ForeignKey('shippers.shipper_id', ondelete='CASCADE'),
        nullable=True,
    )
    freight: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )
    ship_name: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    ship_address: Mapped[str] = mapped_column(
        String(60),
        nullable=True,
    )
    ship_city: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
    ship_region: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
    ship_postal_code: Mapped[str] = mapped_column(
        String(10),
        nullable=True,
    )
    ship_country: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
