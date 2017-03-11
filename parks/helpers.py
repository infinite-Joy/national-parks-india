import json
import os


def parks():
    """
    return the park name and the park coordinates
    park_name: (park coordinate north, park coordinate south)
    from the file the information is in the file
    """
    parks_file_dir = os.path.dirname(os.path.abspath(__file__))
    parks_file = "%s/parks_info.json" % parks_file_dir
    with open(parks_file) as parksfile:
        parks_json = json.load(parksfile)
    return parks_json
