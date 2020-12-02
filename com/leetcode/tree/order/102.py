import collections
from typing import List

from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        if root is None:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            nList = list()
            for _ in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                nList.append(node.val)
            res.append(nList)
        return res


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().levelOrder(root)
    print(res)
