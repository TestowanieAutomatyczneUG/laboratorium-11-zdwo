class Friendships:
    def __init__(self):
        self.fr = {}

    def addFriend(self, person, friend):
        if person in self.fr.keys():
            if friend not in self.fr[person]:
                self.fr[person].append(friend)
                return self.fr[person]
            else:
                raise Exception('juz jest friend')
        else:
            raise Exception('brak person')

    def makeFriends(self, person1, person2):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)
        return self.fr

    def getFriendsList(self, person):
        if person in self.fr.keys():
            return self.fr[person]
        else:
            raise Exception('brak person')

    def areFriends(self, person1, person2):
        if person2 in self.fr.keys():
            if person1 in self.fr[person2]:
                return True
            else:
                return False
        else:
            raise Exception('brak person')


