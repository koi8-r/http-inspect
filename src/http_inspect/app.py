from fastapi import FastAPI, Request


app = FastAPI()


@app.get('/')
def index():
    return 'index'


@app.get('/ip')
def ip(req: Request):
    return req.client.host

@app.get('/headers')
def headers(req: Request):
    return req.headers

