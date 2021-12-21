import unittest
from unittest.mock import *
from friendshipsDb import FriendshipsDb


class TestFrDb(unittest.TestCase):
    def setUp(self):
        self.temp = FriendshipsDb()

    def test_add_friend(self):
        self.temp.db.addFriend = MagicMock(return_value=['p2'])
        self.temp.addFriend('p1', 'p2')
        self.temp.db.addFriend.assert_called_with('p1', 'p2')

    def test_add_friend_brak_person(self):
        self.temp.db.addFriend = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.addFriend, 'nieistniejacyp3', 'p2')
        self.temp.db.addFriend.assert_called_with('nieistniejacyp3', 'p2')

    def test_add_friend_juz_friends(self):
        self.temp.db.addFriend = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.addFriend, 'przyjacielp2', 'przyjacielp1')
        self.temp.db.addFriend.assert_called_with('przyjacielp2', 'przyjacielp1')

    def test_make_friends(self):
        self.temp.db.makeFriends = MagicMock(return_value={'p1': ['p2'], 'p2': ['p1']})
        self.temp.makeFriends('p1', 'p2')
        self.temp.db.makeFriends.assert_called_with('p1', 'p2')

    def test_get_friends(self):
        self.temp.db.getFriendsList = MagicMock(return_value=['p1', 'p3'])
        self.temp.getFriendsList('p2')
        self.temp.db.getFriendsList.assert_called_with('p2')

    def test_get_friends_list_brak_person(self):
        self.temp.db.getFriendsList = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.getFriendsList, 'nieistniejacyp3')
        self.temp.db.getFriendsList.assert_called_with('nieistniejacyp3')

    def test_are_friends(self):
        self.temp.db.areFriends = MagicMock(return_value=True)
        self.temp.areFriends('p1', 'p2')
        self.temp.db.areFriends.assert_called_with('p1', 'p2')

    def test_are_not_friends(self):
        self.temp.db.areFriends = MagicMock(return_value=False)
        self.temp.areFriends('p1', 'p2')
        self.temp.db.areFriends.assert_called_with('p1', 'p2')

    def test_are_friends_brak_person(self):
        self.temp.db.areFriends = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.areFriends, 'p1', 'nieistniejacyp3')
        self.temp.db.areFriends.assert_called_with('p1', 'nieistniejacyp3')

    def tearDown(self):
        self.temp = None
