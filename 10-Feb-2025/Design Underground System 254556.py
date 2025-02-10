# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time = self.check_ins[id][1]
        duration = t - start_time
        self.times[(self.check_ins[id][0]), stationName].append(duration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.times[(startStation, endStation)]
        return sum(time)/len(time)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)