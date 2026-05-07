"""US_states"""

from __future__ import annotations

from datetime import date

from sqlalchemy import ForeignKey, Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class US_State(Base):
    """Модель Штаты."""

    __tablename__ = 'us_states'

    state_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    state_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    state_abbr: Mapped[str] = mapped_column(
        String(2),
        nullable=True,
    )
    state_region: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
    )
