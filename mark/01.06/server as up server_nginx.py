from aiohttp import web
import logging
import json

async def indexhandle(request: web.Request):
    return web.Response(text='Welcome to pymyserver', status=200)

async def handle(request: web.Request):
    print(request.match_info)
    print(request.query_string)  # http://127.0.0.1:8080/1?name=12301
    return web.Response(text=request.match_info.get('id', '0000'), status=200)

async def todopost(request: web.Request):
    print(request.method)
    print(request.match_info)
    print(request.query_string)
    print(request.json)
    js = await request.json()  # 获取post的json数据
    print(js, type(js))
    text = dict(await request.post())  # 一定要await，拿到一个post数据字典
    print(text, type(text))
    js.update(text)  # {}.update(**js, **text)
    res = json.dumps(js)
    print(res)
    return web.Response(text=res, status=201)

app = web.Application()
app.router.add_get('/', indexhandle)  # http://127.0.0.1:8080/
app.router.add_get('/{id}', handle)  # http://127.0.0.1:8080/12301
app.router.add_post('/api/todo', todopost)

app.logger.setLevel(level=logging.NOTSET)
web.run_app(app, host='0.0.0.0', port=8080)
