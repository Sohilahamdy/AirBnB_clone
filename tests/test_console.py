#!/usr/bin/python3

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def create(self):

        return HBNBCommand()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_quit(self, mock_stdout):

        con = self.create()
        result = con.onecmd("quit")
        self.assertTrue(con.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), '')

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_EOF(self, mock_stdout):

        con = self.create()
        result = con.onecmd("EOF")
        self.assertTrue(con.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), '')
