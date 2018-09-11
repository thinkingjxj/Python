import asyncio
from aiohttp import ClientSession


async def get_html(url:str):
    async with ClientSession() as session:
        async with session.get(url) as res:
            print(res.status)
            print(await res.text())


url = 'http://127.0.0.1/ziroom-web/'

loop = asyncio.get_event_loop()
loop.run_until_complete(get_html(url))
loop.close()





