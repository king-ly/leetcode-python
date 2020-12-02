from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = self.countNodes(root.left)
        r = self.countNodes(root.right)
        return l + r + 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().countNodes(root)
    print(res)
