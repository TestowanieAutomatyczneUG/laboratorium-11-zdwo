from friendships import Friendships


class FriendshipsDb:
    def __init__(self):
        self.db = Friendships()

    def addFriend(self, person1, person2):
        return self.db.addFriend(person1, person2)

    def makeFriends(self, person1, person2):
        return self.db.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.db.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.db.areFriends(person1, person2)