#!/usr/bin/env python 

import json

dd = {'name':'guankai', 'age':23, 'gender':'male'}
ss = json.dumps(dd)

def _decode_dict(data):
    rv = {}
    for key, value in data.items():
	    value = str(value) + "guankai"
	    rv[key] = value
    return rv

def parse_json_in_str(data):
    return json.loads(data, object_hook=_decode_dict)

result = parse_json_in_str(ss)
print result
