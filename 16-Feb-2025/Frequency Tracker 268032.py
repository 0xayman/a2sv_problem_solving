# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.values = defaultdict(int)
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:
        self.values[number] += 1
        frequency = self.values[number]
        self.frequencies[frequency] += 1
        if self.frequencies[frequency - 1]:
            self.frequencies[frequency - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.values[number] == 0:
            return
        self.values[number] -= 1
        frequency = self.values[number]
        self.frequencies[frequency] += 1
        if self.frequencies[frequency + 1]:
            self.frequencies[frequency + 1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)