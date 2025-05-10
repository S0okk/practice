import aiohttp
import asyncio
import json
import logging
import time

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
main_handler = logging.FileHandler('api_monitor/logs/monitor.log')
main_handler.setLevel(logging.INFO)
logger.addHandler(main_handler)

error_logger = logging.getLogger("errors")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('api_monitor/logs/errors.log')
error_handler.setLevel(logging.ERROR)
error_logger.addHandler(error_handler)

with open("api_monitor/config.json", "r") as f:
    config = json.load(f)



async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return f'{url} -> {response.status}', json.dumps(dict(response.headers), indent=2)
    except Exception as e:
        error_logger.error(f"Error fetching {url}: {e}")
        return f'{url} -> ERROR', str(e)

async def monitor_loop():
    urls = config['urls']
    interval = config['check_interval']
    async with aiohttp.ClientSession() as session:
        while True:
            cur_time = time.perf_counter()
            logger.info(f'{time.ctime(time.time())}: Started')

            tasks = [fetch(url, session) for url in urls]
            results = await asyncio.gather(*tasks)

            for result in results:
                print(result[0])
                print(result[1])
                print('-' * 70)

            end_time = time.perf_counter()
            logger.info(f'Latency is: {end_time - cur_time}')
            logger.info(f'{time.ctime(time.time())}: Finished\n')

            await asyncio.sleep(interval)

def main():
    asyncio.run(monitor_loop())

if __name__ == "__main__":
    main()