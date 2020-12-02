class Solution:

    def isHappy(self, n: int) -> bool:
        list1 = list()
        while True:
            list2 = [int(k) ** 2 for k in list(str(n))]
            sum1 = int(sum(list2))
            #如果sum值已存在过，所以就会无限循环
            if sum1 in list1:
                return False
            else:
                list1.append(sum1)
            if sum1 == 1:
                return True
            n = sum1

if __name__ == '__main__':
    n = 11
    res = Solution().isHappy(n)
    print(res)
