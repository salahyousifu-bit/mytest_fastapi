import httpx
import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        
        response.raise_for_status()

        return response.json()