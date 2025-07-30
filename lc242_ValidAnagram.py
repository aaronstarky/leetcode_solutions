class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letters, t_letters = {}, {}
        for i in range(len(s)):
            s_letters[s[i]] = 1 + s_letters.get(s[i], 0)
            t_letters[t[i]] = 1 + t_letters.get(t[i], 0)

        for key in s_letters:
            if s_letters[key] != t_letters.get(key, 0):
                return False
        return True
    
    
class AlternateSolution:
    '''
    This solution is super smart
    Instead of storing two dictionaries, he stores one
    Then he subtracts from the value that was stored of occurences of a char in s
    If he reaches zero and encounters another instance, it fails
    But if the string is an anagram, he will never encounter another instance so the zero will never be seen again.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if dic.get(c, 0) == 0:
                return False
            dic[c] -= 1
        return True