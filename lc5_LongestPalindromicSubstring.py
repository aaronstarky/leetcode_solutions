class Solution:        
    def is_palindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        longestSubstr = ""
        for i in range(len(s)):
            if len(longestSubstr) >= len(s) - i:
                break
            char = s[i]
            rBound = len(s)
            while rBound > i:
                furthest = s.rfind(char, i, rBound)
                if furthest == -1:
                    break
                substr = s[i:furthest+1]
                if self.is_palindrome(substr) and len(substr) > len(longestSubstr):
                    longestSubstr = substr
                    break
                rBound = furthest
        return longestSubstr
                

    
    
solution = Solution()
print(f"Case 1: {solution.longestPalindrome("ababad")}")
print(f"Case 2: {solution.longestPalindrome("babad")}")
print(f"Case 3: {solution.longestPalindrome("cbbd")}")
print(f"Case 4: {solution.longestPalindrome("aacabdkacaa")}")
print(f"Case 5: {solution.longestPalindrome("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")}")
print(f"Case 6: {solution.longestPalindrome("a")}")




