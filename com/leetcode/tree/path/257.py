from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


# 二叉树的所有路径
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + path for path in sub_paths]


if __name__ == '__main__':
    nums = [1, 2, 3, None, 5]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().binaryTreePaths(root)
    print(res)
