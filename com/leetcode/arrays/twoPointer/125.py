class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        str = s.lower()
        while l < r:
            if not str[l].isalnum():
                l += 1
                continue
            elif not str[r].isalnum():
                r -= 1
                continue
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True



if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    flag = Solution().isPalindrome(s)
    print(flag)
