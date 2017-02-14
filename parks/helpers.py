import json

def parks():
    """
    return the park name and the park coordinates
    park_name: (park coordinate north, park coordinate south)
    from the file the information is in the file
    """
    with open("parks_info.json") as parksfile:
        parks_json = json.load(parksfile)
        return parks_json
