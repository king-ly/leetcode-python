from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        stack1 = list()
        stack2 = list()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        x = 0
        while stack1 or stack2:
            sumTmp = None
            if stack1 and stack2:
                sumTmp = stack1.pop() + stack2.pop() + x
            elif stack2:
                sumTmp = stack2.pop() + x
            else:
                sumTmp = stack1.pop() + x
            if sumTmp >= 10:
                sumTmp = sumTmp % 10
                x = 1
            else:
                x = 0
            node = ListNode(sumTmp)
            node.next = dummyHead.next
            dummyHead.next = node
        if x == 1:
            node = ListNode(1)
            node.next = dummyHead.next
            dummyHead.next = node
        return dummyHead.next


if __name__ == '__main__':
    # nums1 = [7, 2, 4, 3]
    # nums2 = [5, 6, 4]
    nums1 = [5]
    nums2 = [5]
    l1 = ListNodeUtils.addNodes(nums1)
    l2 = ListNodeUtils.addNodes(nums2)
    res = Solution().addTwoNumbers(l1, l2)
    ListNodeUtils.printListNode(res)
