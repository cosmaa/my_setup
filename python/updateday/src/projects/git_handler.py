from pathlib import Path


class GitHub(object):

    def __init__(self, data):
        self.project_root_path = data["project_root_path"]
        self.path = data["path"]
        self.name = data["name"]

    def reset_hard_project(self):
        script_with_params = f".{Path().resolve()}/script.sh '%s'" % self.project_root_path
        print(script_with_params)
        # val = subprocess.check_call( script_with_params , shell=True)


