class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo = [[0 for i in range(len(text1))] for j in range(len(text2))]
        memo = {}
        for i in range(len(text1)):
            matched = False
            for j in range(len(text2)):
                memo[(i,j)] = max(memo.get((i-1,j), 0), memo.get((i,j-1), 0))
                if text1[i] == text2[j] and not matched:
                    memo[(i,j)] += 1
                    matched = True
        return memo[(len(text1)-1, len(text2)-1)]
   
'''
run = O(nm): beats 40%
space = O(nm): beats 25%
'''   
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for i in range(1, len(text2) + 1):
            cur_length = 0
            for j in range(1, len(text1) + 1):
                if text1[j-1] == text2[i-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[-1][-1]

'''
run = O(nm): beats 5%
space = O(nm): beats 17%
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo = [[0 for i in range(len(text1))] for j in range(len(text2))]
        memo = {}
        for i in range(len(text1)):
            matched = False
            cur_length = 0
            for j in range(len(text2)):
                memo[(i,j)] = max(memo.get((i-1,j), 0), memo.get((i,j-1), 0))
                if text1[i] == text2[j]:
                    memo[(i,j)] = 1 + memo.get((i-1, j-1), 0)
                    matched = True
        return memo[(len(text1)-1, len(text2)-1)]