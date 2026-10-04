import asyncio

from services.external_api import get_data

async def main():
    data = await get_data()
    print(data)


asyncio.run(main())