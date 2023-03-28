import asyncio
from decouple import config

from WorckerClient import WorckerClientContextManager, Worcker_Client
from Worcker import Worcker






async def start_send():
    async with WorckerClientContextManager(url_rabbit=config("REBBITMQ_URL"), user=config("RABBITMQ_DEFAULT_USER"), password=config("RABBITMQ_DEFAULT_PASS")) as connection:
        await asyncio.gather(asyncio.create_task(Worcker_Client.put(connection=connection, message_data="23dfsdfsdfdsffsadfsddsadfsa", queue_name='hello')))


async def start_resive():
    async with WorckerClientContextManager(url_rabbit=config("REBBITMQ_URL"), user=config("RABBITMQ_DEFAULT_USER"), password=config("RABBITMQ_DEFAULT_PASS")) as connection:
        await Worcker.resive(connection=connection, queue_name='hello')

if __name__ == "__main__":
    asyncio.run(start_send())
    asyncio.run(start_resive())
