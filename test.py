import requests
import json


data = {
    "username": "chr",
    "password": "chr",
}


res = requests.get("http://127.0.0.1:3000/api/v3/fk", params=data )
print(res.text)
