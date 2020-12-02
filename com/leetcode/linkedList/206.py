from com.leetcode.linkedUtils import ListNodeUtils, ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        while head:
            node = ListNode(head.val)
            node.next = dummyHead.next
            dummyHead.next = node

            head = head.next
        return dummyHead.next


# 三游标
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = ListNodeUtils.addNodes(nums)
    res = Solution2().reverseList(head)
    ListNodeUtils.printListNode(res)
