from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return l and r


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [1, None, 2]
    p = TreeNodeUtils.arrayToNode(nums1)
    q = TreeNodeUtils.arrayToNode(nums2)
    res = Solution().isSameTree(p, q)
    print(res)
