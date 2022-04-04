"""
Design a hit counter which counts the number of hits received in the past 5 minutes
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity),
and you may assume that calls are being made to the system in chronological order
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp
(i.e., the past 300 seconds).
"""


class HitCounter:

    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp] = 0
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300
        count = 0

        for i in range(begin + 1, timestamp + 1):
            if i in self.hits:
                count += self.hits[i]
        return count


# Your HitCounter object will be instantiated and called as such:
hitCounter = HitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
hitCounter.getHits(4)
hitCounter.hit(300)
print(hitCounter.getHits(300))
print(hitCounter.getHits(301))
