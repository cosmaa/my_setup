from .git_handler import GitHub


class PythonProject(GitHub):

    # GITHUB init:
    # project_root_path
    # path
    # name

    def update_Versions(self):
        pass

    def __str__(self):
        return f"Python project: \t {self.name}"

