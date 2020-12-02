from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self._postOrder(root, res)
        return res

    def _postOrder(self, root: TreeNode, res: List):
        if root is None:
            return
        self._postOrder(root.left, res)
        self._postOrder(root.right, res)
        res.append(root.val)


if __name__ == '__main__':
    nums = [1, None, 2, None, None, 3]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().postorderTraversal(root)
    print(res)
