#!/usr/bin/python3

import json
from time import sleep
import unittest
import pep8
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_doc_module(self):
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files
        (['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_doc_constructor(self):
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        my_model.name = "ALX"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "ALX")
        self.assertEqual(my_model.my_number, 89)

    def test_model_types(self):
        second_model = BaseModel()
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
        }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIsInstance(second_model.__dict__[key], value)

    def test_uuid(self):
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_string_representation(self):
        obj = BaseModel()
        obj.name = "ALX"
        obj.my_number = 89
        json_attributes = obj.to_dict()
        obj2 = BaseModel(**json_attributes)
        self.assertIsInstance(obj2, TestBaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_file_save(self):
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())


if __name__ == '__main__':
    unittest.main()
