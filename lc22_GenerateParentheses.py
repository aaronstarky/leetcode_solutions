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
