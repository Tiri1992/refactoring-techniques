"""
Introduce a Foreign Method

We require an additional method but cannot modify the existing class from which we made a request. An idea is to create a wrapper method which will
take in the class that is closed for modification. The wrapper method will provide the desired output.
"""

from datetime import datetime

profile = {
    "name": "John",
    "id": 1,
}


class User:

    def __init__(self, name, id):
        self.name = name 
        self.id = id

# Bad: Assume we can't modify this class in anyway.
user = User(profile.get("name"), profile.get("id"))

# Good: Adapt the client object to support modification of an instance of the above class. In this case it adds 1 to the id. 

def client(user, profile):
    return user(profile.get("name"), profile.get("id") + 1)

# Call client
client(User, profile)


