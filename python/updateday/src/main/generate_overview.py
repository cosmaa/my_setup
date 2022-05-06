import glob
import logging
import os
import pathlib
from pathlib import Path

from .projects.kotlin import KotlinProject
from .projects.python import PythonProject

logger = logging.getLogger("logger")

OTTO_PATH = "/home/comaass/otto"


def find_kotlin_projects():
    result = []
    build_config_file_name = "build.gradle.kts"
    for project_path in glob.glob(f"{OTTO_PATH}/*"):
        head, tail = os.path.split(project_path)
        try:
            if "hopper_" in project_path:
                if build_config_file_name in os.listdir(path=project_path):
                    project = KotlinProject({
                        "project_root_path": project_path,
                        "path": project_path,
                        "name": tail
                    })
                    logger.info(project)
                    result.append(project.__dict__)
        except NotADirectoryError as e:
            logger.error(e)
    return result


def find_python_projects():
    result = []
    path_list = list(Path(f"{OTTO_PATH}").rglob(f"*.[tT][xX][tT]"))

    for project_path in path_list:
        head, tail = os.path.split(project_path)
        path, project = os.path.split(head)
        if tail == "requirements.txt":
            if "hopper_" in head:
                project = PythonProject({
                    "project_root_path": project_path.__str__(),
                    "path": head,
                    "name": project
                })
                logger.info(project)
                result.append(project.__dict__)
    return result


def collect_projects():
    logger.info("##### start collecting PYTHON projects #####")
    find_python_projects()
    logger.info("##### start collecting KOTLIN projects #####")
    find_kotlin_projects()



