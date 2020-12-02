from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        if root.left and root.right:
            return min(l, r) + 1
        else:
            return l + r + 1


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().minDepth(root)
    print(res)
