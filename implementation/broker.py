import asyncio
import mqttools

BROKER_ADDRESS = 'localhost'
BROKER_PORT = 1883


async def broker_main():
    print('running broker')
    broker = mqttools.Broker((BROKER_ADDRESS, BROKER_PORT))
    await broker.serve_forever()


async def main():
    await asyncio.gather(
        broker_main()
    )


if __name__ == '__main__':
    asyncio.run(main())
