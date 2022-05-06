import json
from abc import ABC

from .git_handler import GitHub


class KotlinProject(GitHub):


    def update_Versions(self):
        pass

    def __str__(self):
        return f"Kotlin project: \t {self.name}"


if __name__ == '__main__':
    data = {
        "path": "/home/comaass/otto/hopper_auction-presentation",
        "name": "hopper_auction-presentation"
    }

    project = KotlinProject(data)
    print(project)