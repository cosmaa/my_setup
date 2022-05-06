import os

from .git_handler import GitHub


class KotlinProject(GitHub):

    def update_Versions(self):
        pass

    def __str__(self):
        return f"Kotlin project: {self.project_root_path} : \t  {self.name}"

    def set_project_path(self, path):
        return path
