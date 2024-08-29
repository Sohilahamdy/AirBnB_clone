#!/usr/bin/python3
"""
This module contains unit tests for the HBNBCommand class.
It tests the functionality of commands like 'quit', 'EOF',
'create', 'show', 'destroy', 'all', and 'update'.
"""

import unittest
from unittest import mock
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """
    This class contains unit tests for the HBNBCommand class.
    """

    def setUp(self):
        """Helper method to set up a new HBNBCommand instance"""
        self.console = HBNBCommand()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_quit(self, mock_stdout):
        """Test the 'quit' command"""
        self.console.onecmd("quit")
        # Ensure that the 'quit' command does not print anything
        mock_stdout.write.assert_not_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_EOF(self, mock_stdout):
        """Test the 'EOF' command"""
        self.console.onecmd("EOF")
        # Ensure that sys.stdout was called with a newline character
        mock_stdout.write.assert_called_with('\n')

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_create(self, mock_stdout):
        """Test the 'create' command"""
        self.console.onecmd("create BaseModel")
        # Extract the ID from the printed output
        output = mock_stdout.write.call_args[0][0].strip()
        self.assertTrue(output)  # Ensure output is not empty
        self.assertTrue(any(c.isdigit() for c in output))

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_show(self, mock_stdout):
        """Test the 'show' command"""
        # First create an instance to show
        self.console.onecmd("create BaseModel")
        # Get the ID of the created instance
        instance_id = mock_stdout.write.call_args[0][0].strip()
        # Test the 'show' command
        self.console.onecmd(f"show BaseModel {instance_id}")
        # Check if the instance is correctly shown
        output = mock_stdout.write.call_args[0][0].strip()
        self.assertIn(instance_id, output)

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_destroy(self, mock_stdout):
        """Test the 'destroy' command"""
        # First create an instance to destroy
        self.console.onecmd("create BaseModel")
        # Get the ID of the created instance
        instance_id = mock_stdout.write.call_args[0][0].strip()
        # Test the 'destroy' command
        self.console.onecmd(f"destroy BaseModel {instance_id}")
        # Ensure the instance was removed
        self.console.onecmd(f"show BaseModel {instance_id}")
        output = mock_stdout.write.call_args[0][0].strip()
        self.assertEqual(output, "** no instance found **")

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_do_all(self, mock_stdout):
        """Test the 'all' command"""
        con.onecmd("create User")
        con.onecmd("create Place")
        con.onecmd("all")

        # Check that the output contains the instances
        output = mock_stdout.write.call_args[0][0]
        self.assertIn("User", output)
        self.assertIn("Place", output)

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_update(self, mock_stdout):
        """Test the 'update' command"""
        # First create an instance to update
        self.console.onecmd("create BaseModel")
        # Get the ID of the created instance
        instance_id = mock_stdout.write.call_args[0][0].strip()
        # Test the 'update' command
        self.console.onecmd(f"update BaseModel {instance_id} name "
                            "\"new_name\"")
        # Check if the instance is correctly updated
        self.console.onecmd(f"show BaseModel {instance_id}")
        output = mock_stdout.write.call_args[0][0].strip()
        self.assertIn("new_name", output)

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_count(self, mock_stdout):
        """Test the 'count' command"""
        self.console.onecmd("create User")
        self.console.onecmd("create User")
        self.console.onecmd("count User")
        output = mock_stdout.write.call_args[0][0].strip()
        self.assertEqual(output, "2")


if __name__ == '__main__':
    unittest.main()
