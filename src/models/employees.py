"""Employees,Employee_Territories, Territories, Region"""

from __future__ import annotations

from datetime import date

from sqlalchemy import ForeignKey, Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class EmployeeTerritories(Base):
    """Промежуточная модель Работник/Территория."""

    __tablename__ = 'employee_territories'

    employee_id: Mapped[int] = mapped_column(
        ForeignKey('employees.employee_id', ondelete='CASCADE'),
        nullable=False,
    )
    territory_id: Mapped[int] = mapped_column(
        ForeignKey('territories.territory_id', ondelete='CASCADE'),
        nullable=False,
    )
    # booking = relationship(
    #     'Booking',
    #     back_populates='table_slots',
    #     lazy='selectin',
    # )
    # table = relationship('Table')
    # slot = relationship('TimeSlot')


class Employee(Base):
    """Модель Работники компании."""

    __tablename__ = 'employees'

    employee_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    last_name: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String(30),
        nullable=True,
    )
    title_of_courtesy: Mapped[str] = mapped_column(
        String(25),
        nullable=True,
    )
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )
    hire_date: Mapped[date] = mapped_column(
        Date,
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
    home_phone: Mapped[str] = mapped_column(
        String(24),
        nullable=True,
    )
    extension: Mapped[str] = mapped_column(
        String(4),
        nullable=True,
    )
    photo: Mapped[bytes] = mapped_column(
        nullable=True,
    )
    notes: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    reports_to: Mapped[int] = mapped_column(
        ForeignKey('employees.employee_id', ondelete='CASCADE'),
        nullable=True,
    )
    photo_path: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )


class Territories(Base):
    """Модель Территория."""

    __tablename__ = 'territories'

    territory_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True, index=True
    )
    territory_description: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
    )
    region_id: Mapped[int] = mapped_column(
        ForeignKey('region.region_id', ondelete='CASCADE'),
        nullable=False,
    )


class Region(Base):
    """Модель Регион."""

    __tablename__ = 'region'

    region_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    region_description: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
    )
