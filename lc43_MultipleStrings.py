class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        i = 0
        results = []

        while len(num1) - 1 - i >= 0:
            result = ''
            j = 0
            carry = 0
            while len(num2) - 1 - j >= 0:
                product = (ord(num1[len(num1) - 1 - i]) - ord('0')) * (ord(num2[len(num2) - 1 - j]) - ord('0'))
                curr_place = (product + carry) % 10
                result = str(curr_place) + result
                carry = (product + carry) // 10
                j += 1
            for zero in range(i):
                result += '0'
            if carry > 0:
                result = str(carry) + result
            results.append(result)

            i += 1
        print(f'results: {results}')
        overall_result = results[0]
        for i in range(1, len(results)):
            prev = overall_result
            overall_result = self.add_strings(overall_result, results[i])
            print(f"{prev} + {results[i]} = {overall_result}")
        return overall_result

    def add_strings(self, s1, s2):
        result = ''
        s1 = s1[::-1]
        s2 = s2[::-1]
        longer = ''
        shorter = ''
        if len(s1) > len(s2):
            longer = s1
            shorter = s2
        else:
            longer = s2
            shorter = s1

        carry = 0
        for i in range(len(longer)):
            total = 0
            if i >= len(shorter):
                total = (ord(longer[i]) - ord('0')) + carry
            else:
                total = (ord(longer[i]) - ord('0')) + (ord(shorter[i]) - ord('0')) + carry
            curr_place = (total) % 10
            result += str(curr_place)
            carry = (total) // 10
        if carry > 0:
            result = result + str(carry)
            
        return result[::-1]


solution = Solution()

print(solution.multiply('123', '49'))
print(solution.add_strings('1107', '4920'))

