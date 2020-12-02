from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next

    def deleHelp(self, head: ListNode, val: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        cur = dummyHead.next
        while cur:
            if cur.val == val:
                self.deleteNode(cur)
            cur = cur.next
        return dummyHead.next


if __name__ == '__main__':
    nums = [4, 5, 1, 9]
    val = 5
    head = ListNodeUtils.addNodes(nums)
    res = Solution().deleHelp(head, val)
    ListNodeUtils.printListNode(res)
