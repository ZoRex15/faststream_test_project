from typing import List

from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import ScalarResult
from sqlalchemy import select

from app.infrastructure.db.models.user import User
from app.core.models import dto

from .base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def get_by_id(self, id: int) -> dto.User:
        return (await self._get_by_id(id)).to_dto()
    
    async def _get_by_tg_id(self, tg_id: int) -> User:
        try:
            result: ScalarResult[User] = await self.session.scalars(
                select(User).where(User.tg_id == tg_id)
            )
            return result.one()
        except Exception:
            return None
        
    async def create(self, tg_id: int, join_date: date | None = None):
        user = await self._get_by_tg_id(tg_id)
        if not user:
            user = User(
                tg_id=tg_id,
                join_date=join_date
            )
            self._save(user)
            await self._flush(user)
        return user.to_dto()
    
    async def get_all(self) -> List[dto.User]:
        result = await self._get_all()
        return [i.to_dto() for i in result]
    

    