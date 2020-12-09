from datetime import datetime as dt
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s.%(msecs)09f > %(message)s", datefmt='%Y-%m-%dT%H:%M:%S')
log = logging.getLogger('app')


log.info('hello')

