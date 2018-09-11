from aiohttp import web


async def indexhandle(request:web.Request):
    return web.Response(text=request.path, status=201)

async def handle(request:web.Request):
    print(request.match_info)
    print(request.query_string)   # http://127.0.0.1:8080/1?name=12301
    return web.Response(text=request.match_info.get('id', '0000'), status=200)


app = web.Application()
app.router.add_get('/', indexhandle)
app.router.add_get('/{id}', handle)

web.run_app(app, host='0.0.0.0', port=9977)



