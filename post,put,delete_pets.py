import requests

# POST добавление нового питомца
BASE_URL = 'https://petstore.swagger.io/v2'
new_pets = {
  "id": 1345678901111,
  "category": {
    "id": 0,
    "name": "dog"
  },
  "name": "sharik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "1"
    }
  ],
  "status": "available"
}

res = requests.post(f"{BASE_URL}/pet", json=new_pets,)
print(res.json())
print(res.status_code)

# GET проверка добавленого питомца

res = requests.get(f'{BASE_URL}/pet/1345678901111')
print(res.json())
print(res.status_code)
# PUT изменение питомца
new_pets_put = {
  "id": 1345678901111,
  "category": {
    "id": 0,
    "name": "dogie"
  },
  "name": "bobik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "собака"
    }
  ],
  "status": "pending"
}
res = requests.put(f'{BASE_URL}/pet', json=new_pets_put)
print(res.json())
print(res.status_code)
# проверка изменения животного по petID
res = requests.get(f'{BASE_URL}/pet/1345678901111')
print(res.json())
print(res.status_code)
# Delete удаление питомца
res = requests.delete(f"{BASE_URL}/pet/1345678901111")
print("удален",res.json())
print(res.status_code)
# проверка удаленного питомца
res = requests.get(f'{BASE_URL}/pet/1345678901111')
print(res.json())
print(res.status_code)
