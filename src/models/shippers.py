"""Shippers, Suppliers"""

from __future__ import annotations

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class Shipper(Base):
    """Модель Доставщик."""

    __tablename__ = 'shippers'

    shipper_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    company_name: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    phone: Mapped[str] = mapped_column(
        String(24),
        nullable=True,
    )


class Supplier(Base):
    """Модель Поставщик/Производитель."""

    __tablename__ = 'suppliers'

    supplier_id: Mapped[int] = mapped_column(
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
    homepage: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
