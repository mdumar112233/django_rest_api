import requests
import json
# URL = 'http://127.0.0.1:8000/alldata/'

# path = requests.get(url = URL)

# data = path.json()

# print(data)

##### DE_SERIALIZATION ------------

# URL = 'http://127.0.0.1:8000/createpost/'

# data = {
#     'name' : 'faruk',
#     'roll' : 32,
#     'city' : 'comilla'
# }

# json_data = json.dumps(data)

# post = requests.post(url = URL, data = json_data)

# data = post.json()

# print(data)


#### REST CRUD
URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id} 

    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)

    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name': 'hafij',
        'roll': 20,
        'city': 'norsindi'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)

    data = r.json()
    print(data)

# post_data()

def  update_data():
    data = {
        'id': 2,
        'name': 'hafij new',
        'roll': 10,
        'city': 'new city'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)

    data = r.json()
    print(data)

update_data()

def  delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)

    data = r.json()
    print(data)

# delete_data()

