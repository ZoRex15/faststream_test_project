from typing import Protocol

from datetime import date

from app.core.models import dto
from app.core.interfaces.base import Commiter


class UserCreate(Commiter, Protocol):
    async def create(self, tg_id: int, join_date: date):
        raise NotImplementedError
    
class GetAllUsers(Commiter, Protocol):
    async def get_all(self):
        raise NotImplementedError