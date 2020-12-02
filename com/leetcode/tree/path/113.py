from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def pathSum(self, root: TreeNode, val: int) -> List[List[int]]:
        res = []
        paths = self._helper(root)
        for i in range(len(paths)):
            if sum(paths[i]) == val:
                res.append(paths[i])
        return res

    def _helper(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        l = self._helper(root.left)
        r = self._helper(root.right)

        return [[root.val].extend(path) for path in sub_paths]


if __name__ == '__main__':
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    val = 22
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().pathSum(root, val)
