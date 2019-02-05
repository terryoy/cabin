import json

def dumps(data={}, format='default'):
    if format == 'pretty':
        return json.dumps(data, indent=4)

    return json.dumps(data)
