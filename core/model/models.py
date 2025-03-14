from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from sqlalchemy import ForeignKey, DateTime
from datetime import date, datetime
from sqlalchemy.sql import func


class Sites(Base):
    title: Mapped[Optional[str]]
    url: Mapped[Optional[str]]
    xpath: Mapped[Optional[str]]

class Product(Base):
    sites_id: Mapped[int] = mapped_column(ForeignKey('sites.id'))
    price: Mapped[str]
    dt_create: Mapped[date] = mapped_column(DateTime(timezone=True),default=datetime.now(), server_default=func.now())

    