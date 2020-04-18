from json import JSONDecodeError
import json
from math import radians, sin, cos, acos


# File path to json files
data_file = 'data/data.json'
geo_file = 'data/geo.json'
new_geo_out = 'data/geo_split.json'
merge_out = 'data/merged.json'
selected_pb = 'data/selected.json' # Output file for last selected items


# Task 2
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


# Start Task 3 & Task 4 Functions

# Split Lat and Lon
def geo_split(file_geo1):
    """
    Split the current GEO file LatLon column in two seperate columns

    """
    with open(file_geo1, 'r') as inp, open(new_geo_out, 'w') as outp:
        json_decode = json.load(inp)
        result = []
        for loca in json_decode:
            lat_lon = loca['geo'].split(",")
            result.append({
                "ipv4": loca["ipv4"],
                "lat": lat_lon[0],
                "lon": lat_lon[1]
            })
        data = json.dumps(result)
        outp.write(data)
    with open(new_geo_out, 'r') as f:
        geosplit = json.load(f)
    return geosplit
