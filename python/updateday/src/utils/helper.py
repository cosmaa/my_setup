import json


def nice_json_string(data):
    return json.dumps(data, indent=4)
