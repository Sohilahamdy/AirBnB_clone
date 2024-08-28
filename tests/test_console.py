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

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_create(self, mock_stdout):
        con = self.create()
        con.onecmd("create BaseModel")
        mock_stdout.write.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_show(self, mock_stdout):
        con = self.create()
        con.onecmd("show BaseModel 1234")
        mock_stdout.write.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={
        'BaseModel.1234': mock.MagicMock(id='1234')
    })
    @mock.patch('models.storage.save')
    def test_destroy(self, mock_save, mock_all, mock_stdout):
        con = self.create()
        con.onecmd("destroy BaseModel 1234")
        mock_all().pop('BaseModel.1234', None)
        mock_save.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={})
    def test_destroy_instance_not_found(self, mock_all, mock_stdout):
        con = self.create()
        con.onecmd("destroy BaseModel 1234")
        mock_stdout.write.assert_called_with("** no instance found **\n")

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={
        'BaseModel.1234': mock.MagicMock(id='1234'),
        'User.5678': mock.MagicMock(id='5678')
    })
    def test_all(self, mock_all, mock_stdout):
        con = self.create()
        con.onecmd("all")
        mock_stdout.write.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={
        'BaseModel.1234': mock.MagicMock(id='1234')
    })
    def test_all_class(self, mock_all, mock_stdout):
        con = self.create()
        con.onecmd("all BaseModel")
        mock_stdout.write.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={
        'BaseModel.1234': mock.MagicMock(id='1234')
    })
    @mock.patch('models.storage.save')
    def test_update(self, mock_save, mock_all, mock_stdout):
        con = self.create()
        con.onecmd('update BaseModel 1234 name "NewName"')
        instance = mock_all().get('BaseModel.1234')
        instance.name = 'NewName'
        mock_save.assert_called()

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_update_class_not_found(self, mock_stdout):
        con = self.create()
        con.onecmd('update NonExistentClass 1234 name "NewName"')
        mock_stdout.write.assert_called_with("** class doesn't exist **\n")

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    @mock.patch('models.storage.all', return_value={})
    def test_update_instance_not_found(self, mock_all, mock_stdout):
        con = self.create()
        con.onecmd('update BaseModel 1234 name "NewName"')
        mock_stdout.write.assert_called_with("** no instance found **\n")

    @mock.patch('sys.stdout', new_callable=mock.MagicMock)
    def test_update_missing_arguments(self, mock_stdout):
        con = self.create()
        con.onecmd('update BaseModel 1234')
        mock_stdout.write.assert_called_with("** attribute name missing **\n")


if __name__ == '__main__':
    unittest.main()
