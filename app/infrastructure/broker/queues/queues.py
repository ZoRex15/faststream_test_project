from faststream.rabbit import RabbitQueue


delayed_queue = RabbitQueue(
    name='delayed_queue'
)