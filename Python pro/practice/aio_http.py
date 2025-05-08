import aiohttp
import asyncio

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
