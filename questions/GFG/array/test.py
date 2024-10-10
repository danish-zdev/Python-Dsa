# def outer():
#     print("hi outer")
#     inner()

# def inner():
#     print("hi Inner")
   
# ob = outer()
# ob

# lst1 = [1,2,3,4,5,6]

# print(lst1[::-1])

# hashmap = {
#     "name": 
#            {"age":34, "height": {"upper":194, "lower": 175}},
#     "location": "delhi", "address": 
#           {"area": "jammu", "mobile": [123456723, 487477573485]}
#           }


# print(hashmap['address']['mobile'][0])

import requests

url = requests.get('https://jsonplaceholder.typicode.com/users')

# print(url.json()[0]["name"])
for i in url.json():
    print(i['name'])

