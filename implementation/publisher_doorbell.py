import asyncio
import mqttools
from broker import BROKER_ADDRESS, BROKER_PORT

TOPIC_DOORBELL = '/doorbell'
MSG_DING = 'DING'


async def publisher_doorbell_main():
    print('running publisher doorbell')
    async with mqttools.Client(BROKER_ADDRESS, BROKER_PORT) as client:
        while True:
            ding = MSG_DING.encode('ascii')
            client.publish(TOPIC_DOORBELL, ding)
            await asyncio.sleep(10)


async def main():
    await asyncio.gather(
        publisher_doorbell_main()
    )


if __name__ == '__main__':
    asyncio.run(main())
