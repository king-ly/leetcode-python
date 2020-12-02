from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            if pre and cur.val == pre.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().deleteDuplicates(head)
    ListNodeUtils.printListNode(res)
