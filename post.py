import requests

url = 'http://127.0.0.1:8000/predict/'
myobj = {
"data": {
    "area": 220,
    "property-type": "APARTMENT",
    "rooms-number": 2,
    "zip-code": 1000,
    "land-area": 200,
    "garden": True,
    "garden-area": 10,
    "equipped-kitchen": True,
    "full-address": "address",
    "swimming-pool": False,
    "furnished": False,
    "open-fire": False,
    "terrace": False,
    "terrace-area": 0,
    "facades-number": 2,
    "building-state": "NEW"
  }
}

x = requests.post(url, json = myobj)

print(x.text)