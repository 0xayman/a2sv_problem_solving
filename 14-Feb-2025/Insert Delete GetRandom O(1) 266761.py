# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if not val in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True

        return False
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.arr.remove(val)
            self.dict.pop(val)
            return True

        return False


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()