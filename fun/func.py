from json import JSONDecodeError
import json
from math import radians, sin, cos, acos


# File path to json files
data_file = 'data/data.json'
geo_file = 'data/geo.json'
new_geo_out = 'data/geo_split.json'
merge_out = 'data/merged.json'
selected_pb = 'data/selected.json' # Output file for last selected items


def is_json(filename):
    """
    Check if the specified file is a valid JSON file

    """
    try:
        with open(filename, 'r') as f:
            dstore = json.load(f)
        except JSONDecodeError:
            return False # In case the file is invalid json file
        return True # In case the file is a valid json file
