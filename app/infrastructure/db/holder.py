from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.repository import UserRepository


class HolderRepository:
    def __init__(self, session: AsyncSession):
        self.user_repository = UserRepository(session)