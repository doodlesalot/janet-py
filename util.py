import json

def jprint(to_print, indent=4, sort_keys=True):
    print(json.dumps(to_print, indent=indent, sort_keys=sort_keys))