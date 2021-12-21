import unittest
from unittest.mock import *


class Note:
    def __init__(self, name, note):
        if type(name) is not str:
            raise TypeError('wrong name type')
        elif type(note) is not float:
            raise TypeError('wrong note type')
        elif name in [None, '']:
            raise Exception('name cant be null')
        elif not 2 <= note <= 6:
            raise Exception('note must be <= 6 and >=2')
        else:
            self.name = name
            self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


class NotesStorage:
    def add(self, note):
        pass

    def clear(self):
        pass

    def getAllNotesOf(self, name):
        pass


class NotesService:
    def __init__(self):
        self.ns = NotesStorage()

    def add(self, note):
        return self.ns.add(note)

    def averageOf(self, name):
        sum = 0
        notes = self.ns.getAllNotesOf(name)

        if len(notes) == 0:
            return sum
        for note in notes:
            sum += note
        avg = sum/len(notes)
        return avg

    def clear(self):
        return self.ns.clear()


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.service = NotesService()

    @patch.object(NotesStorage, 'add', MagicMock(return_value='ok'))
    def test_add(self):
        note = Note('aaa', 3.11)
        self.assertEqual(self.service.add(note), 'ok')

    @patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[2.3, 4.4, 2.21]))
    def test_avgOf(self):
        self.assertAlmostEqual(self.service.averageOf('a'), 2.97)

    @patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[]))
    def test_avgOf_empty(self):
        self.assertEqual(self.service.averageOf('b'), 0)

    @patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[5.281]))
    def test_avgOf_one(self):
        self.assertAlmostEqual(self.service.averageOf('c'), 5.281)

    @patch.object(NotesStorage, 'clear', MagicMock(return_value='ok'))
    def test_clear(self):
        self.assertEqual(self.service.clear(), 'ok')



