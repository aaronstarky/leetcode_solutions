class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # create the data structure
        classes = {}
        for pre in prerequisites:
            if pre[0] not in classes:
                classes[pre[0]] = []
            classes[pre[0]].append(pre[1])
        
        # define recursive helper
        curr_visited = set()
        visited = set()
        def dfs(node):
            if node in curr_visited:
                return False
            if node in visited:
                return True
            curr_visited.add(node)
            if node in classes:
                for pre_req in classes[node]:
                    if not dfs(pre_req):
                        return False
            curr_visited.remove(node)
            visited.add(node)
            return True

        # iterate over classes
        for course in range(numCourses):
            if course in visited:
                continue
            curr_visited = set()
            no_cycle = dfs(course)
            if not no_cycle:
                return False
        return True

    