def characterReplacement(s: str, k: int) -> int:
    if len(s) == 0:
        return 0
    maj_char, sub_len, longest_sub = '', 0, 0
    chars = {'': 0}
    prev = None
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            sub_len += 1
        else:
            sub_len = 0
        longest_sub = max(sub_len, longest_sub)
        chars[s[i]] = 1 if s[i] not in chars else chars[s[i]] + 1
        if chars[s[i]] > chars[maj_char]:
            maj_char = s[i]
    if k == 0:
        return longest_sub
    l, r, num_replacements, greatest = 0, 0, 0, 0
    while r < len(s):
        print(f'current substring: {s[l:r+1]}')
        print(f'num_replacements: {num_replacements}')
        print(f'greatest: {greatest}')
        # move the pointers
        if num_replacements > k:
            if s[l] != maj_char:
                num_replacements -= 1
            l += 1
            r += 1
            continue
        if s[r] != maj_char:
            num_replacements += 1
        greatest = max(greatest, r - l)
        r += 1

    return greatest        

'''
This solution is insanely simple. I really struggle keeping my solutions simple.
The for loop here is some serious sauce wow.
'''
class GeminiSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        max_len = 0
        max_freq = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_freq = max(max_freq, chars[s[r]])
            window = r - l + 1
            if window - max_freq > k:
                chars[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len