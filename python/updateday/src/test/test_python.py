from ..main.projects.python import PythonProject
import pytest


def test_test_small():
    data = {'path': '/home/comaass/otto/hopper_gocd/go-server', 'name': 'go-server',
            'project_root_path': '/home/comaass/otto/hopper_gocd/go-server'}
    expected_data = {'path': '/home/comaass/otto/hopper_gocd/go-server', 'name': 'go-server',
                     'project_root_path': '/home/comaass/otto/hopper_gocd'}
    project = PythonProject(data)
    print(project.__dict__)

    assert project.__dict__ == expected_data


def test_big_path():
    data = {'path': '/home/comaass/otto/hopper_gocd/hoolla/go-server', 'name': 'go-server',
            'project_root_path': '/home/comaass/otto/hopper_gocd/hoolla/go-server'}
    expected_data = {'path': '/home/comaass/otto/hopper_gocd/hoolla/go-server', 'name': 'go-server',
                     'project_root_path': '/home/comaass/otto/hopper_gocd'}
    project = PythonProject(data)
    print(project.__dict__)

    assert project.__dict__ == expected_data


def test_xxl_path():
    data = {'path': '/home/comaass/otto/hopper_gocd/a/b/c/d/e/go-server', 'name': 'go-server',
            'project_root_path': '/home/comaass/otto/hopper_gocd/a/b/c/d/e/go-server'}
    expected_data = {'path': '/home/comaass/otto/hopper_gocd/a/b/c/d/e/go-server', 'name': 'go-server',
                     'project_root_path': '/home/comaass/otto/hopper_gocd'}
    project = PythonProject(data)
    print(project.__dict__)

    assert project.__dict__ == expected_data
