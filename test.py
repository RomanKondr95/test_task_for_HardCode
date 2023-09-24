import requests

base_url = 'http://localhost:8000'

def lessonlist():
    url = f'{base_url}/api/lessonlist'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
# print(lessonlist())
# output:
# [{'title': 'python lesson', 'duraton': 90, 'last_viewed': '2023-09-07T06:00:00Z', 'user': 'root', 'status': True},
# {'title': 'django lesson', 'duraton': 85, 'last_viewed': '2023-09-11T08:46:46Z', 'user': 'misha', 'status': False},
# {'title': 'OOP', 'duraton': 25, 'last_viewed': '2023-09-06T12:00:00Z', 'user': 'masha', 'status': True},
# {'title': 'game 2048', 'duraton': 50, 'last_viewed': '2023-09-03T18:00:00Z', 'user': 'root', 'status': False}]

def productlist(product_id):
    url = f'{base_url}/api/productlessons/{product_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
print(productlist(1))
# output
# [{'title': 'python lesson', 'duraton': 90, 'last_viewed': '2023-09-07T06:00:00Z', 'user': 1, 'status': True},
# {'title': 'game 2048', 'duraton': 50, 'last_viewed': '2023-09-03T18:00:00Z', 'user': 1, 'status': False}]