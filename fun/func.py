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


# Get Euclidean distance
def latlon_dist(input_lat, input_lon):
    """
    Load the two JSON files and take the custom starting LAT and LON
    inputs and calculate the Euclidean distance from starting point
    to all other points in the GEO file with coordinates.

    """
    eudist = []
    for dis in newgeo:
        slat = radians(float(input_lat)) # Input static Latitudefrom user
        slon = radians(float(input_lon)) # Input static Lontitude from user
        elat = radians(float(dis['lat']))
        elon = radians(float(dis['lon']))
        dist = round(6371.01 * acos(sin(slat)*sin(elat) +
                                    cos(slat)*cos(elat) *
                                    cos(slon - elon)), 2)
        eudist_un.append({
            "ipv4": dis["ipv4"],
            "lat": dis["lat"],
            "lon": dis["lon"],
            "dist": dist
        })
    return eudist_un


# Parse json files
def data_json(file_data):
    """
    Parse the Data json file

    """
    with open(file_data, 'r') as f:
        datastore = json.load(f)
    return datastore


def merge_geos(data1, data2): # (geodist, datastore)
    """
    Merge the two Geo json's

    """
    data_merged = [
                    dict(**el1, **el2)
                    for el1 in data1
                    for el2 in data2
                    if el1['ipv4'] in el2['meta']
                    ]
    merged_sorted = sorted(
                           data_merged,
                           key=lambda k: k['dist'],
                           reverse=False
                           )
    return merged_sorted


def sort_final(y):
    with open(selected_pb, 'w') as outpb:
        pb = []
        for pr in y:
            pb.append({
                "active": pr["active"],
                "asn": pr["asn"],
                "countrycode": pr["countrycode"],
                "id": pr["id"],
                "statecode": pr["statecode"],
                "meta": pr["meta"],
                "dist": pr["dist"]
            })
        datap = json.dumps(pb)
        outpb.write(datap)
    with open(selected_pb, 'r') as f:
        selected_dist = json.load(f)
    return selected_dist
