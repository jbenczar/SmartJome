import asyncio
import mqttools
from broker import BROKER_ADDRESS, BROKER_PORT
from publisher_doorbell import TOPIC_DOORBELL


async def subscriber_phone_main():
    print('running subscriber phone')
    async with mqttools.Client(BROKER_ADDRESS, BROKER_PORT) as client:
        # subscribe to a topic
        await asyncio.gather(
            client.subscribe(TOPIC_DOORBELL)
        )

        while True:
            topic, message = await client.messages.get()
            print(f'Phone: Got {message} on {topic}.')

            if topic is None:
                print('Echo client connection lost.')
                break


async def main():
    await asyncio.gather(
        subscriber_phone_main()
    )


if __name__ == '__main__':
    asyncio.run(main())
