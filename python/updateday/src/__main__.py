import logging

from .generate_overview import generate_version_overview
from .utils.logger import ColorLogFormatter, Color

logger = logging.getLogger("logger")
logger.setLevel('DEBUG')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColorLogFormatter())
logger.addHandler(stream_handler)

# -----------------------------------------------------------------------------------

generate_version_overview()