"""Categories"""

from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Category(Base):
    """Модель категорий."""

    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    category_name: Mapped[str] = mapped_column(
        String(16),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    picture: Mapped[bytes] = mapped_column(
        nullable=True,
    )
