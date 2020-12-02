from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self._preOrder(root, res)
        return res

    def _preOrder(self, root: TreeNode, res: List):
        if root is None:
            return
        res.append(root.val)
        self._preOrder(root.left, res)
        self._preOrder(root.right, res)


if __name__ == '__main__':
    nums = [1, None, 2, None, None, 3]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().preorderTraversal(root)
    print(res)