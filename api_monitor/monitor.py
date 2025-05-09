import aiohttp
import asyncio
import json
import logging

with open("api_monitor/config.json", "r") as f:
    code = json.load(f)

while True:
    async def fetch(url, session):
        async with session.get(url) as response:
            await asyncio.sleep(code['check_interval'])
            return f'{url} -> {response.status}', json.dumps(dict(response.headers), indent=2)
    async def main():
        urls = code['urls']
        async with aiohttp.ClientSession() as session:
            tasks = [fetch(url, session) for url in urls]
            results = await asyncio.gather(*tasks)
            for result in results:
                print(result[0])
                print(result[1])
                print('-' * 70)

    asyncio.run(main())