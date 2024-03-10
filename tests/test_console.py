#!/usr/bin/python3
import console
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def create(self):
        return HBNBCommand()

    def test_quit(self):
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
