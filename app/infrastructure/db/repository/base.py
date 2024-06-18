from typing import TypeVar, Generic

from collections.abc import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.interfaces import ORMOption

from app.infrastructure.db.models.base import Base


Model = TypeVar('Model', bound=Base, covariant=True, contravariant=False)

class BaseRepository:
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def _get_by_id(
        self, 
        id: int,
        options: Sequence[ORMOption] | None = None,
        populate_existing: bool = False
    ) -> Sequence[Model]:
        result = await self.session.get(
            self.model,
            id,
            options=options,
            populate_existing=populate_existing
        )
        if result is None:
            raise NoResultFound
        return result
    
    async def delete(self, obj: Base) -> None:
        await self.session.delete(obj)

    async def _get_all(self, options: Sequence[ORMOption] = ()) -> Sequence[Model]:
        result: ScalarResult[Model] = await self.session.scalars(
            select(self.model).options(*options)
        )
        return result.all()
    
    async def commit(self):
        await self.session.commit()

    def _save(self, obj: Base):
        self.session.add(obj)

    async def _flush(self, *objects: Base):
        await self.session.flush(objects)