from datetime import datetime, timezone, timedelta

from dishka.integrations.aiogram import FromDishka

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from faststream.rabbit import RabbitBroker

from app.infrastructure.db.holder import HolderRepository
from app.core.service.user import create_user


router = Router()

@router.message(CommandStart())
async def start(message: Message, repository: FromDishka[HolderRepository]):
    await message.answer(
        text=(
            f'Привет, {message.from_user.full_name}\n\n'
            'Это демонстрационный бот, в котором ZoRex тестирует работу с RabbitMQ.'
        )
    )
    await create_user(
        repository.user_repository,
        message.from_user.id,
        message.date.date()
    )

@router.message(Command('delay'))
async def send_delay_message(message: Message, broker: FromDishka[RabbitBroker]):
    seconds = int(message.text.split(' ')[-1])
    scheduled_time = (datetime.now(timezone.utc) + timedelta(seconds=seconds)).isoformat()
    await broker.publish(
        message={
            'user_id': message.from_user.id,
            'text': f'Delay message: {seconds}',
            'scheduled_time': scheduled_time
        },
        queue='delayed_queue',
        exchange='main_delayed_exchange'
    )

# @router.message(Command('spam'))
# async def start_spam(message: Message, repository: HolderRepository, broker: Broker):
#     await broker.create_spam_list_for_users(
#         text='Hi',
#         repository=repository
#     )