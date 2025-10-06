from queue import PriorityQueue

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        edges = PriorityQueue()
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                length = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edgesput