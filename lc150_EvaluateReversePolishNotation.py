class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        nums = []
        for i in range(len(tokens)):
            match tokens[i]:
                case '+':
                    nums.append(nums.pop() + nums.pop())
                case '-':
                    subtractor = nums.pop()
                    base = nums.pop()
                    nums.append(base - subtractor)
                case '*':
                    nums.append(nums.pop() * nums.pop())
                case '/':
                    divisor = nums.pop()
                    dividee = nums.pop()
                    nums.append(int(dividee / divisor))
                case _:
                    nums.append(int(tokens[i]))
        return nums.pop()
        