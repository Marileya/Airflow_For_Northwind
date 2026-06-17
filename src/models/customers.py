"""Customers"""

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Customer(Base):
    """Модель покупатели."""

    __tablename__ = 'customers'

    customer_id: Mapped[str] = mapped_column(
        String(5),
        primary_key=True, index=True
    )
    company_name: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    contact_name: Mapped[str] = mapped_column(
        String(30),
        nullable=True,
    )
    contact_title: Mapped[str] = mapped_column(
        String(30),
        nullable=True,
    )
    address: Mapped[str] = mapped_column(
        String(60),
        nullable=True,
    )
    city: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
    region: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
    postal_code: Mapped[str] = mapped_column(
        String(10),
        nullable=True,
    )
    country: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
    )
    phone: Mapped[str] = mapped_column(
        String(24),
        nullable=True,
    )
    fax: Mapped[str] = mapped_column(
        String(24),
        nullable=True,
    )
