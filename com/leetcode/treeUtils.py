import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNodeUtils:
    @classmethod
    def arrayToNode(cls, arr: List, index=0) -> TreeNode:
        treeNode = None
        if index <= len(arr) - 1:
            if arr[index]:
                treeNode = TreeNode(arr[index])
                treeNode.left = cls.arrayToNode(arr, index * 2 + 1)
                treeNode.right = cls.arrayToNode(arr, index * 2 + 2)
        return treeNode

    # 中序打印
    @classmethod
    def printPreorder(cls, root: TreeNode):
        res = list()
        cls._preOrder(root, res)
        print(res)

    @classmethod
    def _preOrder(cls, root: TreeNode, res: List):
        if root is None:
            return
        res.append(root.val)
        cls._preOrder(root.left, res)
        cls._preOrder(root.right, res)

    @classmethod
    def printLeveOrder(cls, root: TreeNode):
        res = cls._levelOrder(root)
        print(res)

    @classmethod
    def _levelOrder(cls, root: TreeNode) -> List[List[int]]:
        res = list()
        if root is None:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            nList = list()
            for _ in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                nList.append(node.val)
            res.append(nList)
        return res


if __name__ == '__main__':
    nums = [1, None, 2, None, None, 3]
    root = TreeNodeUtils.arrayToNode(nums)
    TreeNodeUtils.printPreorder(root)
