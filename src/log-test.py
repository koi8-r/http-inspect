import yaml
import logging, logging.config

from elogger import configure, get_logger


configure('conf/logging.yaml')
LOG = get_logger(__name__, 'processor', ppl='first_callback')


LOG.setLevel(10)
#LOG.debug("TEST")
#LOG.info('EST')
LOG.exception(AssertionError('FUUUUU'))
