from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        return max(lDepth, rDepth) + 1


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().maxDepth(root)
    print(res)
