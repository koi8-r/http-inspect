import sys, socket
import logging, logging.config as logging_config, sys, socket
from uuid import uuid4

import yaml


assert sys.version_info > (3, 7), "Python version below 3.7 is not supported by logging bacause of msec support"


def ex_hook(ex_type, ex_val, traceback):
    logging.exception('Uncaught error', exc_info=(ex_type, ex_val, traceback))


sys.excepthook = ex_hook


DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DEFAULT_FORMAT = (
    "event_time=%(asctime)s",
    "level=%(levelname)s",
    "module=%(name)s",
    "line=%(lineno)d",
    "log_id=%(log_id)s",
    "hostname=%(hostname)s",
    "component=%(component)s",
    "task_id=%(task_id)s",
    "req_id=%(req_id)s",
)
BASE_FORMAT      = ' '.join([*DEFAULT_FORMAT, "message=%(message)r"])
PROCESSOR_FORMAT = ' '.join([
    *DEFAULT_FORMAT,
    "ppl=%(ppl)s",
    "message=%(message)r"
])
FETCHER_FORMAT = ' '.join([
    *DEFAULT_FORMAT,
    "domain=%(domain)s",
    "status=%(status)d",
    "message=%(message)r"
])
TRANSPORTER_FORMAT = ' '.join([
    *DEFAULT_FORMAT,
    "consumer=%(consumer)s",
    "status=%(status)d",
    "message=%(message)r"
])


class PlainFormatter(logging.Formatter):
    hostname: str = socket.gethostname()

    @classmethod
    def enrich(cls, record):
        record.hostname = cls.hostname
        record.log_id = str(uuid4())

        record.component = getattr(record, 'component', None)
        record.task_id   = getattr(record, 'task_id', None)
        record.req_id    = getattr(record, 'req_id', None)

        return record

    def format(self, record):
        return super().format(self.enrich(record))


class TyphoonFormatter(PlainFormatter):
    def __init__(self, fmt=None, datefmt=None, *a, **kw):
        super().__init__(fmt or BASE_FORMAT, datefmt or DATE_FORMAT, *a, **kw)

    def format(self, record):
        orig_fmt = self._style._fmt

        # if record.component == 'processor':
        #     record.ppl = getattr(record, 'ppl', 'first')
        #     self._style._fmt = PROCESSOR_FORMAT

#       raise OSError
        res = super().format(record)
        self._style._fmt = orig_fmt
        return res


def configure(path: str):
    try:
        with open(path, 'rt') as f:
            data = yaml.load(f, yaml.Loader)
            logging_config.dictConfig(data)
    except FileNotFoundError:
        pass


def get_logger(name: str, component: str, **kw):
    return logging.LoggerAdapter(
        logging.getLogger(name),
        extra=dict(
            component=component,
            **kw
        )
    )
