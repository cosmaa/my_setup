import os

from .git_handler import GitHub


class PythonProject(GitHub):

    # GITHUB init:
    # project_root_path
    # path
    # name
    def __init__(self, data):
        GitHub.__init__(self, data)

    def update_Versions(self):
        pass

    # root project only wit <team-name>
    def set_project_path(self, path):
        head = path
        tail = ""
        while "hopper_" not in tail:
            head, tail = os.path.split(head)
        return f"{head}/{tail}"

    def __str__(self):
        return f"Python project: {self.project_root_path} : \t {self.name}"
