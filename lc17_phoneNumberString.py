from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        values = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        if len(digits) == 1:
            return values[digits[0]]
        
        result = []
        for i in range(len(digits)):
            print(i)
            # handle base case
            if i == 0:
                result = values[digits[i]]
                continue
            
            # prep the new result with the previous result
            new_result = []
            for item in result:
                print(item)
                for letter in values[digits[i]]:
                    print(item + letter)
                    new_result.append(item + letter)
            result = new_result
        return result
                    
                    
                
        
        
solution = Solution()

print(solution.letterCombinations('23'))