from sqlalchemy import Mapped, mapped_column
from sqlalchemy import Boolean, String
from app.database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    completed: Mapped[bool]  = mapped_column(Boolean, nullable=False, default=False)




