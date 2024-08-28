#!/usr/bin/python3
"""
This module contains unit tests for the HBNBCommand class.
It tests the functionality of commands like 'quit', 'EOF',
'create', 'show', 'destroy', 'all', and 'update'.
"""

import unittest
from unittest import mock
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    This class contains unit tests for the HBNBCommand class.
    """

    def create(self):
        """Helper method to create a new HBNBCommand instance"""
        return HBNBCommand()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_quit(self, mock_stdout):
        """Test the 'quit' command"""
        con = self.create()
        con.onecmd("quit")
        # Ensure that sys.stdout was not called
        mock_stdout.write.assert_not_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_EOF(self, mock_stdout):
        """Test the 'EOF' command"""
        con = self.create()
        con.onecmd("EOF")
        # Ensure that sys.stdout was called with a newline character
        mock_stdout.write.assert_called_with('\n')
