class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        inList = ['(', '{', '[']
        outMap = {'(': ')', '{': '}', '[': ']'}
        for val in s:
            if val in inList:
                stack.append(val)
            else:
                if not stack or outMap[stack.pop()] != val:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = "[]"
    res = Solution().isValid(s)
    print(res)
