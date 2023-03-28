from typing import Optional, List, Type, Any
from types import TracebackType
from aio_pika import connect, Message, IncomingMessage



class WorckerClientContextManager:

    def __init__(self, url_rabbit, user, password):
        self.url_rabbit = url_rabbit
        self.user = user
        self.password = password
        self.connect_rabbit: connect = connect(url=self.url_rabbit,  login=self.user,
                                               password=self.password)


    async def __aenter__(self) -> connect:
        return await self.connect_rabbit

    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None,
                        tb: TracebackType | None):
             self.connect_rabbit.close()



class Worcker_Client:

    @staticmethod
    async def put(connection: connect, message_data:Any , queue_name: str):
        # Creating a channel
        channel = await connection.channel()
        # Declaring queue
        await channel.declare_queue(queue_name)
        # Sending the message
        await channel.default_exchange.publish(
            Message(str(message_data).encode()),
            routing_key=queue_name,
        )