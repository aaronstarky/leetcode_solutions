class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result += str(len(strs[i])) + '#' + strs[i]
        return result

    def decode(self, s: str) -> list[str]:
        # read the pound sign
        cursor = 0
        results = []
        while cursor < len(s):
            # read until the first pound sign
            pi = s.index('#', cursor)
            s_len = int(s[cursor:pi])
            cursor = pi + 1
            results.append(s[cursor:cursor + s_len])
            cursor += s_len
        return results
