import asyncio

from infrastructure.providers.http import HttpProvider


def main():
    loop = asyncio.get_event_loop()

    http_provider = HttpProvider()

    task = loop.create_task(http_provider.run())

    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        pass
    finally:
        loop.stop()


if __name__ == "__main__":
    main()
