from com.leetcode.treeUtils import TreeNode, TreeNodeUtils


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        #找到叶子节点
        self.invertTree(root.left)
        self.invertTree(root.right)
        #找到叶子节点后，进行交换
        root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    nums = [4, 2, 7, 1, 3, 6, 9]
    root = TreeNodeUtils.arrayToNode(nums)
    res = Solution().invertTree(root)
    TreeNodeUtils.printLeveOrder(res)
