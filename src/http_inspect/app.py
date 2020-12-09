from fastapi import FastAPI, Request
import logging, yaml


try:
    with open('conf/logging.yaml', 'rt') as f:
        data = yaml.load(f, yaml.Loader)
        logging.config.dictConfig(data)
except FileNotFoundError:
    pass


app = FastAPI()
LOG = logging.LoggerAdapter(logging.getLogger(__name__), extra=dict(component='app'))


@app.get('/')
def index():
    return 'index'


@app.get('/ip')
def ip(req: Request):
    LOG.info('op=ip')
    return req.client.host

@app.get('/headers')
def headers(req: Request):
    LOG.info('op=headers')
    return req.headers

