from datetime import date

from app.core.interfaces.user import UserCreate, GetAllUsers
from app.core.models import dto


async def create_user(repository: UserCreate, tg_id: int, join_date: date) -> dto.User:
    user = await repository.create(tg_id, join_date)
    await repository.commit()
    return user

async def get_all_users(repository: GetAllUsers):
    return await repository.get_all()