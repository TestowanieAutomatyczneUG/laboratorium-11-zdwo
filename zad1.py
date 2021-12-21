import os
import unittest
from unittest.mock import *


class FileOED:
    def openFile(self, file):
        with open(file, 'r') as f:
            d = f.read()
        return d

    def editFile(self, file, l):
        with open(file, 'w') as f:
            f.write(l)
        return True

    def deleteFile(self, file):
        if os.path.exists(file):
            os.remove(file)


class TestFileOED(unittest.TestCase):
    def setUp(self):
        self.temp = FileOED()

    @patch("builtins.open", new_callable=mock_open, read_data="abcd")
    def test_openFile(self, mock_file):
        self.assertEqual(self.temp.openFile(mock_file), "abcd")

    @patch("builtins.open", new_callable=mock_open)
    def test_editFile(self, mock_file):
        self.assertTrue(self.temp.editFile(mock_file, "abcd"))

    @patch("os.path.exists")
    @patch("os.remove")
    def test_deleteFile(self, mock_rm, mock_path):
        mock_path.return_value = False
        self.temp.deleteFile("path/file.txt")
        mock_rm.assert_not_called()

    @patch("os.path.exists")
    @patch("os.remove")
    def test_deleteFile_noFile(self, mock_rm, mock_path):
        mock_path.return_value = True
        self.temp.deleteFile("path/file.txt")
        mock_rm.assert_called_with("path/file.txt")

    def tearDown(self):
        self.temp = None
