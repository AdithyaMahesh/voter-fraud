import os

string = '''

curl -X POST \
  http://127.0.0.1:9000/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'


'''

string2 = '''

curl -X POST \
  http://127.0.0.1:10000/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'


'''


os.system(string)
os.system(string2)
