#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()

print("-- Reloaded objects--")
for obj_id, obj in all_objs.items():
    print("--create a new object--")
    my_model = BaseModel()
    my_model.name = "holberton"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
