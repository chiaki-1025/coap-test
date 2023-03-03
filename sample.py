import json

json_open = open('sample.json', 'r')

json_load = json.load(json_open)

print(json_load)

print(json_load['id']['type'])

for v in json_load.values():
    print(v['id'])
