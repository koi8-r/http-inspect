import logging, socket, sys
from uuid import uuid4


ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%s%z"
DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d -"
    " log_id=%(log_id)s"
    " host_name=%(hostname)s"
    " > %(message)s"
)


class PlainFormatter(logging.Formatter):
    hostname: str = socket.gethostname()

    def __init__(self, fmt, datefmt=ISO_DATE_FORMAT):
        super().__init__(fmt=fmt, datefmt=datefmt)

    @classmethod
    def enrich(cls, record):
        record.hostname = cls.hostname
        record.log_id = str(uuid4())
        return record

    def format(self, record):
        return super().format(self.enrich(record))



class PlainStreamHandler(logging.StreamHandler):
    def __init__(self, fmt=DEFAULT_FORMAT, stream=sys.stderr):
        super().__init__(stream)
        self.setFormatter(PlainFormatter(fmt=fmt))

