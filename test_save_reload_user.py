#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)

print("-- Create a new user --")
my_user = User()
my_user.first_name = "betty"
my_user.last_name = "holberton"
my_user.email = "airbnb@holbertonschool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new user 2 --")
my_user2 = User()
my_user2.first_name = "john"
my_user2.email = "airbnb@holberton.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
