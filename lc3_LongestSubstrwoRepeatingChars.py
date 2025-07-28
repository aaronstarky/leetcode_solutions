# DONE

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        longest = 0
        current = 0
        start = 0
        while start < len(s):
            i = start
            while i < len(s):
                if s[i] not in letters:
                    letters.add(s[i])
                    current += 1
                    i += 1
                elif s[i] in letters:
                    if current > longest:
                        longest = current
                    current = 0
                    letters.clear()
                    start += 1
                    break
        if current > longest:
            longest = current
        return longest
            
solution = Solution()

print(f"Case 1: {solution.lengthOfLongestSubstring("abcabcbb") == 3 }")
print(f"Case 2: {solution.lengthOfLongestSubstring("bbbbb") == 1 }")
print(f"Case 3: {solution.lengthOfLongestSubstring("pwwkew") == 3 }")
print(f"Case 4: {solution.lengthOfLongestSubstring("dvdf") == 3 }")





        