"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
"""


from heapq import *


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    current_cpu, max_cpu, min_heap = 0, 0, []
    for job in jobs:
        while len(min_heap) > 0 and min_heap[0].end <= job.start:
            current_cpu -= min_heap[0].cpu_load
            heappop(min_heap)
        heappush(min_heap, job)
        current_cpu += job.cpu_load
        max_cpu = max(max_cpu, current_cpu)
    return max_cpu


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()
