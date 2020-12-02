from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._helper(root.left, root.right)

    def _helper(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self._helper(p.left, q.right) and self._helper(p.right, q.left)


if __name__ == '__main__':
    nums = [1, 2, 2, None, 3, None, 3]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().isSymmetric(root)
    print(res)
