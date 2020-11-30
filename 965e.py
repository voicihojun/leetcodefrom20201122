# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.output = []

        def helper(root):
            if root is None:
                return

            self.output.append(root.val)
            # print(self.output)

            helper(root.left)
            helper(root.right)

        helper(root)
        return len(set(self.output)) == 1