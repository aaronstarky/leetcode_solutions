class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if s is not even, there can't be valid parentheses
        if len(s) % 2 != 0:
            return False
        items = []
        for c in s:
            if c in {'(', '{', '['}:
                items.append(c)
            else:
                if len(items) == 0:
                    return False
                popped = items.pop()
                if c == ')' and popped != '(':
                    return False
                elif c == '}' and popped != '{':
                    return False
                elif c == ']' and popped != '[':
                    return False
        # if items > 0, we didn't match every start to every end
        if len(items) > 0:
            return False
        # after all this, if we made it, return True
        return True
    
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ps = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                ps.append(s[i])
            else:
                if len(ps) == 0:
                    return False
                start = ps.pop()
                if start == '(' and s[i] == ')':
                    continue
                elif start == '{' and s[i] == '}':
                    continue
                elif start == '[' and s[i] == ']':
                    continue
                else:
                    return False
        if len(ps) > 0:
            return False
        return True
                