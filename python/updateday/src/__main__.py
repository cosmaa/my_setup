import logging
import os

from .projects.python import PythonProject
from .generate_overview import collect_projects
from .utils.logger import ColorLogFormatter

logger = logging.getLogger("logger")
logger.setLevel('DEBUG')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColorLogFormatter())
logger.addHandler(stream_handler)

# -----------------------------------------------------------------------------------




data = {
    "project_root_path": "/home/comaass/otto/hopper_auction-presentation",
    "path": "/home/comaass/otto/hopper_auction-presentation",
    "name": "hopper_auction-presentation"
}


project = PythonProject(data)
print(project)



collect_projects()