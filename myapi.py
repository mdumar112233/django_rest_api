import requests
import json
# URL = 'http://127.0.0.1:8000/alldata/'

# path = requests.get(url = URL)

# data = path.json()

# print(data)

##### DE_SERIALIZATION ------------

URL = 'http://127.0.0.1:8000/createpost/'

data = {
    'name' : 'faruk',
    'roll' : 32,
    'city' : 'comilla'
}

json_data = json.dumps(data)

post = requests.post(url = URL, data = json_data)

data = post.json()

print(data)


