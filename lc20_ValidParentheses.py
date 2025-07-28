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