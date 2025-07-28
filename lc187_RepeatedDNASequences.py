# DONE

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequences = {}
        duplicates = set()
        for i in range(len(s) - 9):
            currSeq = s[i:i+10]
            print(currSeq)
            if currSeq in sequences:
                duplicates.add(currSeq)
                sequences[currSeq] += 1
            else:
                sequences[currSeq] = 1
        return list(duplicates)
    
solution = Solution()

print(f"Case 1: {solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")}")
print(f"Case 2: {solution.findRepeatedDnaSequences("AAAAAAAAAAAAA")}")
print(f"Case 3: {solution.findRepeatedDnaSequences("AAAAAAAAAAA")}")

