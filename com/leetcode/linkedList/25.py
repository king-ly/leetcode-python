from com.leetcode.linkedUtils import ListNode, ListNodeUtils

"""
没看清题，
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        pre = dummyHead
        for i in range(1, k):
            pre = pre.next
        cur = pre.next
        next = cur.next
        pre.next = next

        dummyHead.next = cur
        cur.next = head
        return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().reverseKGroup(head, k=2)
    ListNodeUtils.printListNode(res)
