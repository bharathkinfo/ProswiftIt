from fastapi import FastAPI

# Get - get the data, intpost - create or send the data,put - update the existing data, delete- delete the data

app = FastAPI()

users = {
    1: {"name": "Kevin", "age": 22, "email": "kevin@example.com", "status": "active"},
    2: {"name": "John", "age": 25, "email": "john@example.com", "status": "active"},
    3: {"name": "David", "age": 17, "email": "david@example.com", "status": "inactive"},
    4: {"name": "Alice", "age": 30, "email": "alice@example.com", "status": "active"},
    5: {"name": "Sophia", "age": 28, "email": "sophia@example.com", "status": "active"},
    6: {"name": "Rahul", "age": 24, "email": "rahul@example.com", "status": "pending"}
}

@app.get('/user')
def get_users():
    return users

@app.post('/user')
def create_users(user_id:int, name:str, age:int):
    users[user_id] = {
        "name" : name,
        "age" : age
    }

    return {
        "message" : "user Created",
        "content" : users[user_id]
    }

@app.put('/user')
def update_user (user_id:int, name:str, age:int):
    users[user_id] = {
        "name" : name,
        "age" : age
    }

    return {
        "message" : "user updated",
        "content" : users[user_id]
    }

@app.delete('/user/{user_id}')
def del_user(user_id:int):
    if user_id not in users:
        return "this user doesn't exisit"

    deleted_user = users.pop(user_id)

    return{
        "message": "user deleted",
        "deleted Content" : deleted_user
    }

#Query parameter
@app.get('/user/search')
def search_by_age(age: int):

    result = []

    for user in users.values():

        if user["age"] >= age:
            result.append(user)

    return result

#Query parameter
@app.get('/user/searchname')
def search_by_name(name: str):

    result = []

    for user in users.values():

        if user["name"].lower() == name.lower():
            result.append(user)

    return result


@app.get('/user/search_active_name')
def search_by_name(name: str):

    result = []

    for user in users.values():
        if user["status"] == "active":
            result.append(user)

    return result