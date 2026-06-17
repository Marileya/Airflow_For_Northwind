"""Products"""

from __future__ import annotations

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Products(Base):
    """Модель Продукты."""

    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    product_name: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    supplier_id: Mapped[int] = mapped_column(
        ForeignKey('suppliers.supplier_id', ondelete='CASCADE'),
        nullable=True,
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.category_id', ondelete='CASCADE'),
        nullable=True,
    )
    quantity_per_unit: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
    )
    unit_price: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )
    units_in_stock: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True,
    )
    units_on_order: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True,
    )
    reorder_level: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=True,
    )
    discountinued: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
