import logging, socket, sys
from uuid import uuid4


assert sys.version_info > (3, 7), "Python version below 3.7 is not supported by logging bacause of msec support"


ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%s%z"
DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d -"
    " log_id=%(log_id)s"
    " host_name=%(hostname)s"
    " > %(message)s"
)


class PlainFormatter(logging.Formatter):
    hostname: str = socket.gethostname()

    def __init__(self, fmt, datefmt=ISO_DATE_FORMAT, *a):
        super().__init__(fmt=fmt, datefmt=datefmt)

    @classmethod
    def enrich(cls, record):
        record.hostname = cls.hostname
        record.log_id = str(uuid4())
        try:
            record.component = record.component
        except:
            record.component = None
        return record

    def format(self, record):
        return super().format(self.enrich(record))



class PlainStreamHandler(logging.StreamHandler):
    def __init__(self, fmt=DEFAULT_FORMAT, stream=sys.stderr):
        super().__init__(stream)
        self.setFormatter(PlainFormatter(fmt=fmt))

