from faststream.rabbit import RabbitExchange, ExchangeType


main_delayed_exchange = RabbitExchange(
    name='main_delayed_exchange',
    type=ExchangeType.DIRECT
)

delayed_exchange = RabbitExchange(
    name='delayed_exchange',
    type=ExchangeType.X_DELAYED_MESSAGE,
    arguments={'x-delayed-type': ExchangeType.DIRECT}
)