import requests

# 1. GET users
users = requests.get('https://jsonplaceholder.typicode.com/users')
user = users.json()[4]  # id=5
print(f"Выбран пользователь: {user['name']} (id={user['id']})")

# 2. POST (создание поста)
new_post = {
    "userId": user['id'],
    "title": "My API Post",
    "body": "Learning REST API is fun!"
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print("POST:", response.status_code)
created_post = response.json()
print(created_post)

# 3. PUT (полное обновление поста)
updated_post = {
    "userId": 5,
    "id": 5,  # обязательно id от 1 до 100
    "title": "Updated title",
    "body": "Updated content"
}

response = requests.put('https://jsonplaceholder.typicode.com/posts/5', json=updated_post)
print("Status code:", response.status_code)

try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Сервер не вернул JSON")
# 4. PATCH (частичное обновление)
patch_data = {"title": "Final Title (patched)"}
response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{created_post["id"]}', json=patch_data)
print("PATCH:", response.status_code)
print(response.json())

# 5. DELETE
response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{created_post["id"]}')
print("DELETE:", response.status_code)
