from faststream.rabbit.router import RabbitRouter

from .delay import router


master_router = RabbitRouter()
master_router.include_router(router)

__all__ = [
    'master_router'
]