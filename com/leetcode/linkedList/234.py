from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list1 = list()
        while head:
            list1.append(head.val)
            head = head.next
        i = 0
        j = len(list1) - 1
        while i < j:
            if list1[i] != list1[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    nums = [1]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().isPalindrome(head)
    print(res)
