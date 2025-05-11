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

async def handle_get(request):
    return web.Response(text="GET request received")

async def handle_post(request):
    data = await request.json()
    return web.Response(text=f"POST request received with data: {data}")

app = web.Application()
app.router.add_get('/', handle_get)
app.router.add_post('/', handle_post)

