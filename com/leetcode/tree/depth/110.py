from com.leetcode.treeUtils import TreeNode, TreeNodeUtils

"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = self._helper(root)
        return res != -1

    def _helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l, r = self._helper(root.left), self._helper(root.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        else:
            return max(l, r) + 1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().isBalanced(root)
    print(res)
