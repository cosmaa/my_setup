import json
from abc import ABC

from .git_handler import GitHub


class PythonProject(GitHub):

    def update_Versions(self):
        pass

    def __str__(self):
        return f"Python project: \t {self.name}"



if __name__ == '__main__':
    data = {
        "path": "/home/comaass/otto/hopper_auction-presentation",
        "name": "hopper_auction-presentation"
    }

    project = PythonProject(data)
    print(project)