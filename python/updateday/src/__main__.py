import logging
import os

from .generate_overview import collect_projects
from .utils.logger import ColorLogFormatter

logger = logging.getLogger("logger")
logger.setLevel('DEBUG')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColorLogFormatter())
logger.addHandler(stream_handler)

# -----------------------------------------------------------------------------------


#
collect_projects()