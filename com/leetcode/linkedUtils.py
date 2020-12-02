from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeUtils:
    # nums = {1,2,3,4,5}  变成 1->2->3->4->5->NULL
    @classmethod
    def addNodes(self, nums: List[int]) -> ListNode:
        head = ListNode(nums[0])
        current = head
        for i in range(1, len(nums)):
            current.next = ListNode(nums[i])
            current = current.next;
        return head

    @classmethod
    def printListNode(self, root: ListNode) -> None:
        res = str()
        while root != None:
            res += str(root.val) + "->"
            root = root.next
        res += "NULL"
        print(res)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    root = ListNodeUtils.addNodes(nums)
    ListNodeUtils.printListNode(root)
