from fastapi import FastAPI, Request
import logging, log, yaml



try:
    with open('conf/logging.yaml', 'rt') as f:
        data = yaml.load(f, yaml.Loader)
        logging.config.dictConfig(data)
except:
    pass



app = FastAPI()
LOG = logging.getLogger(__name__)


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

