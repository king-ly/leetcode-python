class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        listPath = path.split("/")
        for p in listPath:
            if p == '..':
                stack.pop()
            else:
                if p != '.':
                    stack.append('/' + p)
        fullStr = "".join(stack)
        while "//" in fullStr:
            fullStr = fullStr.replace("//", '/')
        if len(fullStr) > 1 and fullStr[-1] == '/':
            fullStr = fullStr[:-1]
        return fullStr


if __name__ == '__main__':
    path = "/a/../../b/../c//.///////"
    res = Solution().simplifyPath(path)
    print(res)
