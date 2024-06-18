from typing import Any

from datetime import datetime, timezone

from faststream.rabbit.router import RabbitRouter
from faststream.rabbit import RabbitBroker

from aiogram import Bot

from dishka import FromDishka

from app.infrastructure.broker.exchanges import delayed_exchange, main_delayed_exchange
from app.infrastructure.broker.queues import delayed_queue


router = RabbitRouter()

@router.subscriber(delayed_queue, main_delayed_exchange)
@router.subscriber(delayed_queue, delayed_exchange)
async def delay_consumer(message: dict[str, Any], broker: FromDishka[RabbitBroker], bot: FromDishka[Bot]):
    scheduled_time = datetime.fromisoformat(message.get('scheduled_time')).astimezone(timezone.utc)
    current_time = datetime.now(timezone.utc)
    if current_time >= scheduled_time:
        await bot.send_message(
            chat_id=message.get('user_id'),
            text=message.get('text')
        )
    else:
        delay = int((scheduled_time - current_time).total_seconds() * 1000)
        await broker.publish(
            message=message,
            queue=delayed_queue,
            exchange=delayed_exchange,
            headers={
                'x-delay': delay,
                'scheduled_time': scheduled_time.isoformat()
            }
        )