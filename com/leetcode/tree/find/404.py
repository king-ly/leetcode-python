from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self._helper(root, False)

    def _helper(self, root: TreeNode, flag: bool) -> int:
        if root is None:
            return 0
        if flag and root.left is None and root.right is None:
            return root.val
        l = self._helper(root.left, True)
        r = self._helper(root.right, False)
        return l + r


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    # nums = [1]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().sumOfLeftLeaves(root)
    print(res)
