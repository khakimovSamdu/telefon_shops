from tinydb import TinyDB
import random
import requests
tindb = TinyDB('db.json', indent=4)
def get_brends():
    brends = tindb.tables()
    return list(brends)

def get_brend():
    brends = get_brends()
    url = 'http://127.0.0.1:8000/smartphone/add/'
    for item in brends:
        brend = tindb.table(item).all()
        for v in brend:
            r = requests.post(url, json=v)
            print(r.status_code)
    return r.status_code
print(get_brend())
