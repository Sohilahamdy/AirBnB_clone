#!/usr/bin/python3
"""
This module contains unit tests for the HBNBCommand class.
It tests the functionality of commands like 'quit', 'EOF',
'create', 'show', 'destroy', 'all', and 'update'.
"""

import unittest
from io import StringIO
import sys
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

    def run_command(self, command):
        """Helper method to run a command and capture its output"""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            self.console.onecmd(command)
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

    def test_quit(self):
        """Test the 'quit' command"""
        output = self.run_command("quit")
        self.assertEqual(output, '')

    def test_EOF(self):
        """Test the 'EOF' command"""
        output = self.run_command("EOF")
        self.assertEqual(output, '')

    def test_create(self):
        """Test the 'create' command"""
        output = self.run_command("create BaseModel")
        self.assertTrue(output)  # Ensure output is not empty
        self.assertTrue(any(c.isdigit() for c in output))

    def test_show(self):
        """Test the 'show' command"""
        create_output = self.run_command("create BaseModel")
        instance_id = create_output
        show_output = self.run_command(f"show BaseModel {instance_id}")
        self.assertIn(instance_id, show_output)

    def test_destroy(self):
        """Test the 'destroy' command"""
        create_output = self.run_command("create BaseModel")
        instance_id = create_output
        self.run_command(f"destroy BaseModel {instance_id}")
        show_output = self.run_command(f"show BaseModel {instance_id}")
        self.assertEqual(show_output, "** no instance found **")

    def test_do_all(self):
        """Test the 'all' command"""
        self.run_command("create User")
        self.run_command("create Place")
        output = self.run_command("all")
        self.assertIn("User", output)
        self.assertIn("Place", output)

    def test_update(self):
        """Test the 'update' command"""
        create_output = self.run_command("create BaseModel")
        instance_id = create_output
        self.run_command(f"update BaseModel {instance_id} name \"new_name\"")
        show_output = self.run_command(f"show BaseModel {instance_id}")
        self.assertIn("new_name", show_output)

    def test_count(self):
        """Test the 'count' command"""
        self.run_command("create User")
        self.run_command("create User")
        output = self.run_command("count User")
        self.assertEqual(output, "2")


if __name__ == '__main__':
    unittest.main()
