import unittest
from unittest.mock import *
from friendships import Friendships


class TestFriendships(unittest.TestCase):

    def setUp(self):
        self.temp = Friendships()
        self.temp.fr = {'p1': [], 'p2': ['p1', 'p3'], 'p3': ['p2']}

    def test_add_friend(self):
        self.assertEqual(self.temp.addFriend('p1', 'p2'), ['p2'])

    def test_add_friend_brak_person(self):
        self.assertRaises(Exception, self.temp.addFriend, 'p4', 'p1')

    def test_add_friend_juz_jest_friend(self):
        self.assertRaises(Exception, self.temp.addFriend, 'p2', 'p1')

    def test_make_friends(self):
        self.assertEqual(self.temp.makeFriends('p1', 'p3'), {'p1': ['p3'], 'p2': ['p1', 'p3'], 'p3': ['p2', 'p1']})

    def test_get_friends_list(self):
        self.assertEqual(self.temp.getFriendsList('p2'), ['p1', 'p3'])

    def test_get_empty_friends_list(self):
        self.assertEqual(self.temp.getFriendsList('p1'), [])

    def test_get_friends_list_brak_person(self):
        self.assertRaises(Exception, self.temp.getFriendsList, 'p4')

    def test_are_friends(self):
        self.assertTrue(self.temp.areFriends('p2', 'p3'))

    def test_are_not_friends(self):
        self.assertFalse(self.temp.areFriends('p1', 'p3'))

    def test_are_friends_brak_person(self):
        self.assertRaises(Exception, self.temp.areFriends, 'p1', 'p4')

    def tearDown(self):
        self.temp = None
