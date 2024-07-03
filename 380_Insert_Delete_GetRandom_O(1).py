import random
class RandomizedSet:
    
    def __init__(self):
        self.RandomizedSet = []

    def insert(self, val) :
        if val in self.RandomizedSet:
            return False
        self.RandomizedSet.append(val)
        return True

    def remove(self, val):
        if val in self.RandomizedSet:
            self.RandomizedSet.remove(val)
            return True
        return False

    def getRandom(self) :
        return self.RandomizedSet[random.randint(0,len(self.RandomizedSet)-1)]

