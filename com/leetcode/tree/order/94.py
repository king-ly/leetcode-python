from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self._inOrder(root, res)
        return res

    def _inOrder(self, root: TreeNode, res: List):
        if root is None:
            return
        self._inOrder(root.left, res)
        res.append(root.val)
        self._inOrder(root.right, res)


if __name__ == '__main__':
    nums = [1, None, 2, None, None, 3]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().inorderTraversal(root)
    print(res)
