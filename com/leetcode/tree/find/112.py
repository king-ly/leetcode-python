from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return sum == 0

        if self.hasPathSum(root.left, sum - root.val):
            return True

        if self.hasPathSum(root.right, sum - root.val):
            return True

        return False


if __name__ == '__main__':
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    sum = 22
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().hasPathSum(root, sum)
    print(res)
