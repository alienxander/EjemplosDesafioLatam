from requests import request
from json import loads

URL = "https://jsonplaceholder.typicode.com/posts"

payload = {}
headers = {}

response = request("GET", URL, headers=headers, data=payload)

print(loads(response.text))
print("Status: ", response.status_code)
dicc_posts = loads(response.text)
# for data in dicc_posts:
#     print(f'{data["userId"]} -dic {data["title"]}')


# for k, v in dicc_posts[0].items():
#     print(k, v)

# for k in dict(dicc_posts).keys():
#     print(k)

print([valor["title"] for valor in dicc_posts])
    

