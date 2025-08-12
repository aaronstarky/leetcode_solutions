class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                print(f's[l]: {s[l]} s[r]: {s[r]}')
                return False
        return True
        