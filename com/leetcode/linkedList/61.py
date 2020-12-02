from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    # 思路是对的
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        dummyHead = ListNode(-1)
        dummyHead.next = head
        countCur = dummyHead.next
        count = 0
        while countCur:
            countCur = countCur.next
            count += 1
        for _ in range(k % count):  # 解决非必要的旋转
            p = dummyHead
            q = dummyHead.next
            while q.next:
                p = p.next  # 指向倒数第2个节点
                q = q.next  # 指向最后一个node
            q.next = dummyHead.next
            dummyHead.next = q
            p.next = None
        return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().rotateRight(head, k=2)
    ListNodeUtils.printListNode(res)
