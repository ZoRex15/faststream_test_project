from typing import AsyncIterable, Any

from dishka import Provider, Scope, provide

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine, create_async_engine

from app.infrastructure.db.holder import HolderRepository
from app.config import Config


class DbProvider(Provider):
    
    @provide(scope=Scope.APP)
    async def get_engine(self, config: Config) -> AsyncIterable[AsyncEngine]:
        print('engine')
        engine = create_async_engine(config.db.url)
        yield engine
        await engine.dispose(True)

    @provide(scope=Scope.APP)
    def get_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        print('pool db')
        return async_sessionmaker(engine, expire_on_commit=False)
    
    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        print('session')
        async with pool() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def get_repository(
        self, session: AsyncSession
    ) -> HolderRepository:
        print('repository')
        return HolderRepository(session)
    

