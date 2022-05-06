from abc import ABC, abstractmethod
from pathlib import Path


class GitHub(object):

    def __init__(self, data):
        self.path = data["path"]
        self.name = data["name"]
        self.project_root_path = self.set_project_path(path=data["project_root_path"])

    @abstractmethod
    def set_project_path(self, path):
        pass

    def reset_hard_project(self):
        script_with_params = f".{Path().resolve()}/script.sh '%s'" % self.project_root_path
        # val = subprocess.check_call( script_with_params , shell=True)
