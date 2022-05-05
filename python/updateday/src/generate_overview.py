import glob
import json
import logging
import os
from pathlib import Path

logger = logging.getLogger("logger")
OTTO_PATH = "/home/comaass/otto"


def find_kotlin_projects():
    result = {}
    build_config_file_name = "build.gradle.kts"
    for project_path in glob.glob(f"{OTTO_PATH}/*"):
        head, tail = os.path.split(project_path)
        try:

            if build_config_file_name in os.listdir(path=project_path):
                logger.info(f"found this {build_config_file_name} \t {tail} ")
                result[project_path] = {"name": tail}
        except NotADirectoryError as e:
            logger.error(e)
    return result


def find_python_projects():
    result = {}
    pathlist = list(Path(f"{OTTO_PATH}").rglob(f"*.[tT][xX][tT]"))

    for project_path in pathlist:
        print(project_path.absolute())
        head, tail = os.path.split(project_path)
        path, project = os.path.split(head)
        if tail == "requirements.txt":
            if "hopper_" in head:
                result[f"{head}"] = {"name": project}
    return result


def generate_version_overview():
    overview = {
        "python": find_python_projects(),
        "kotlin": find_kotlin_projects()
    }

    print(json.dumps(overview, indent=4))
