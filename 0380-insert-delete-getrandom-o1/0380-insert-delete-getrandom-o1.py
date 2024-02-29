import random
class RandomizedSet:

    def __init__(self):
        self.mySet = set({})
        

    def insert(self, val: int) -> bool:
        # if item not present, insert into the set and return true; otherwise return falsef
        if val not in self.mySet:
            self.mySet.add(val)
            return True
        else:
            return False
        
        

    def remove(self, val: int) -> bool:
        # if item present, remove it from set and return true; otherwise return false
        if val in self.mySet:
            self.mySet.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        random_ele = random.choice(list(self.mySet))
        return random_ele
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()