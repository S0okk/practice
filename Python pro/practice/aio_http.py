import aiohttp
import asyncio

async def post_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.json()

async def main():
    url = 'http://example.com/api'
    data = {'key': 'value'}
    response = await post_data(url, data)
    print(response)

asyncio.run(main())
