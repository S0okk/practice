import aiohttp
import asyncio
import json

async def fetch(url, session):
    async with session.get(url) as response:
        
        return f'{url} -> {response.status}', json.dumps(dict(response.headers), indent=2)
async def main():
    urls = [
        "https://google.com",
        "https://httpbin.org/get",
        "https://github.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result[0])
            print(result[1])
            print('-' * 70)

asyncio.run(main())