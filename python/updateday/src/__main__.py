import logging

from .utils.logger import ColorLogFormatter, Color

logger = logging.getLogger()
logger.setLevel('DEBUG')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColorLogFormatter())
logger.addHandler(stream_handler)


logger.info("This is a green info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")
