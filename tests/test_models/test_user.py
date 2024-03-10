#!/usr/bin/python3

import json
import datetime
import unittest
import pep8

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_doc_module(self):
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_user(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_doc_constructor(self):
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
