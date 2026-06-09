from sqlalchemy import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Boolean, String


class Base(DeclarativeBase):
    pass

class Product():
    __tablename__ = 'basa dannix 0_0'

    id: Mapped[str] = mapped_column(prinmary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    completed: Mapped[bool]  = mapped_column(String(200), nullable=False)




