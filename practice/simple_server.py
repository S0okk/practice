import aiohttp
import asyncio
from aiohttp import web

async def handle(request):
    await asyncio.sleep(2)  # Симуляция долгого запроса
    return web.Response(text="Hello after 2 seconds!")

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app)
