from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        pre = dummyHead
        while pre:
            test = pre
            for i in range(n + 1):
                test = test.next
            if test is None:
                break
            pre = pre.next
        delNode = pre.next
        nextNode = delNode.next
        pre.next = nextNode
        return dummyHead.next


#滑动窗口
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        p = dummyHead     #要删除节点的前一个索引位置
        q = dummyHead
        for _ in range(n + 1):
            q = q.next
        while q:
            p = p.next
            q = q.next
        delNode = p.next
        nextNode = delNode.next
        p.next = nextNode
        return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = ListNodeUtils.addNodes(nums)
    res = Solution2().removeNthFromEnd(head, n=5)
    ListNodeUtils.printListNode(res)
