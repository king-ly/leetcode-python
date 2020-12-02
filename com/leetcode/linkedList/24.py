from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        pre = dummyHead
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next
            nextNode = node2.next
            # 进行交换  pre->node2->node1->nextNode
            pre.next = node2
            node2.next = node1
            node1.next = nextNode
            # 激动pre指针，进行下一轮
            pre = node1
        return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().swapPairs(head)
    ListNodeUtils.printListNode(res)
