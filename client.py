import requests


HOST = "http://127.0.0.1:5000/"


# GET
def method_get(variable):
    resp = requests.get(f"{HOST}/api/v1/{variable}")
    return resp.json()


# POST
def method_post(json_data):
    requests.post(f"{HOST}/api/v1", json=json_data)


# DELETE
def method_del(variable):
    requests.delete(f"{HOST}/api/v1/{variable}")


# PATCH
def method_patch(variable, json_data):
    resp = requests.patch(f"{HOST}/api/v1/{variable}", json=json_data)
    return resp.json()


advert = [{"title": "Iron",
          "description": "Electric. With a steamer.",
           "author": "Sid Vicious"},
          {"title": "Washer.",
           "description": "New. Bosh",
           "author": "Chester benington"},
          {"title": "grinder.",
           "description": "Electric. Siemens",
           "author": "Kurt Cobain"},
          ]

for i in advert:
    method_post(i)

# print(method_get(1))
# print(method_get(3))
# advert_up = {"title": "Car"}
# method_patch(3, advert_up)
# print(method_get(3))
#
# method_del(2)
