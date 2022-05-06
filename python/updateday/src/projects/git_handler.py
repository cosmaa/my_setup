import json
import subprocess
from abc import ABC, abstractmethod


class GitHub(object):

    def __init__(self, data ):
        self.path = data["path"]
        self.name = data["name"]


    def reset_hard_project(self):
        val = subprocess.check_call("./script.sh '%s'" % self.path, shell=True)
