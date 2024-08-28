#!/usr/bin/python3

import unittest
from unittest import mock
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def create(self):
        return HBNBCommand()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_quit(self, mock_stdout):
        con = self.create()
        con.onecmd("quit")
        # Ensure that sys.stdout was not called
        mock_stdout.write.assert_not_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_EOF(self, mock_stdout):
        con = self.create()
        con.onecmd("EOF")
        # Ensure that sys.stdout was called with a newline character
        mock_stdout.write.assert_called_with('\n')
