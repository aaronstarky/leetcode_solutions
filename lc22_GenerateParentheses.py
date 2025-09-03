'''
For solving this problem, it was crucial to think about
the parentheses generation as a depth first search
traversal. Beyond that, it was also important to think
about the traversal as walking through a maze, with each
opening parentheses being a left turn and each closing 
being a right turn.
'''
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def depthFirstSearch(o, c, s):
            if o == c and o + c == 2 * n:
                res.append(s)
                return
            if o < n:
                depthFirstSearch(o + 1, c, s + '(')
            if c < o or o == n:
                depthFirstSearch(o, c + 1, s + ')')
        depthFirstSearch(1, 0, '(')
        return res
