from .base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, BigInteger, Date
from sqlalchemy import func

from app.core.models import dto


class User(Base):
    __tablename__ = 'Users'

    id = mapped_column(Integer, primary_key=True)
    tg_id = mapped_column(BigInteger, unique=True, nullable=False)
    join_date = mapped_column(Date, nullable=False)

    def __repr__(self) -> str:
        return (
            f'UserModel('
            f'id={self.id}, '
            f'tg_id={self.tg_id}, '
            f'join_date={self.join_date})'
        )
    
    def to_dto(self):
        return dto.User(
            id=self.id,
            tg_id=self.tg_id,
            join_date=self.join_date
        )
