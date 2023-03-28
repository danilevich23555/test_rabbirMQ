from aio_pika import connect




class Worcker:

    @staticmethod
    async def resive(connection: connect, queue_name: str):
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=5)
        queue = await channel.declare_queue(queue_name)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body.decode())







