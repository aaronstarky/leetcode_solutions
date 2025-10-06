import collections

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = set()
        self.sources = set(range(numCourses))
        self.dep = collections.defaultdict(list)
        self.start_time = [0] * numCourses
        self.end_time = [0] * numCourses
        # Remove elements that are not sources from the set
        for a, b in prerequisites:
            if a == b:
                return False
            if a in self.sources:
                self.sources.remove(a)
            self.dep[b].append(a)
        # Start the clock
        self.clock = 0
        for source in self.sources:
            if not self.way_to_accomplish(source):
                return False
        if len(self.visited) != numCourses:
            return False
        return True
    
    def way_to_accomplish(self, node):
        self.visited.add(node)
        self.start_time[node] = self.clock
        self.clock += 1
        for adj in self.dep[node]:
            # If edge is a tree edge, traverse
            if adj not in self.visited and not self.way_to_accomplish(adj):
                return False
            else:
                # Back Edge
                if self.start_time[node] > self.start_time[adj] and not self.end_time[adj]:
                    return False
        self.end_time[node] = self.clock
        self.clock += 1
        return True