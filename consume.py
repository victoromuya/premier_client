import requests

endpoint = 'http://127.0.0.1:8000/api/'
response = requests.post(endpoint, json={'name':"racheal", 'email':"raceah@yahoo.com", 'course':"course"})


if response.status_code != 204:
    print(response.json())