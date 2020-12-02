from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        outList = ['+', '-', '*', '/']
        for val in tokens:
            if val not in outList:
                stack.append(val)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                tmp = None
                if val == '+':
                    tmp = x + y
                elif val == '-':
                    tmp = x - y
                elif val == '*':
                    tmp = x * y
                else:
                    tmp = x / y
                stack.append(tmp)
        return int(stack.pop())


if __name__ == '__main__':
    nums = ["4", "13", "5", "/", "+"]
    res = Solution().evalRPN(nums)
    print(res)
