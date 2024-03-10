#!/usr/bin/python3

import json
import datetime
import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_doc_module(self):
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings).")

    def test_doc_constructor(self):
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)

if __name__ == '__main__':
    unittest.main()
