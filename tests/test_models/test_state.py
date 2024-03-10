#!/usr/bin/python3

import json
import datetime
import unittest
import pep8

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_doc_module(self):
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_doc_constructor(self):
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.place_id, str)


if __name__ == '__main__':
    unittest.main()
