# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            # print(t2)
            return t2
        if t2 is None:
            # print(t1)
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        # print(t1.val)
        return t1

    # def traverse_preorder(self, root: TreeNode):
    #     if root is None:
    #         return
    #     if root is not None:
    #         print(root.val)
    #         # print(root.left.val)
    #         # print(root.right.val)
    #     self.traverse_preorder(root.left)
    #     self.traverse_preorder(root.right)
    #     # return root


    def traverse_preorder(self, root: TreeNode, output = []):
        if root is None:
            return
        if root is not None:
            output.append(root.val)
            self.traverse_preorder(root.left, output)
            self.traverse_preorder(root.right, output)
        return output

    def traverse_inorder(self, root: TreeNode, output = []):
        if root:
            self.traverse_inorder(root.left, output)
            output.append(root.val)
            self.traverse_inorder(root.right, output)
        return output

    def traverse_postorder(self, root: TreeNode, output = []):
        if root:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            output.append(root.val)
        return output


    def traverse_bfs(self, root: TreeNode):
        visited = []
        need_visit = []
        need_visit.append(root)

        while need_visit:
            node = need_visit.pop(0)
            if node is not None and node not in visited:
                visited.append(node.val)
                need_visit.append(node.left)
                need_visit.append(node.right)
        print(visited)





t1 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5, left=None, right=None), right=None), right=TreeNode(val=2, left=None, right=None))
t2 = TreeNode(val=2, left=TreeNode(val=1, left=None, right=TreeNode(val=4, left=None, right=None)), right=TreeNode(val=3, left=None, right=TreeNode(val=7, left=None, right=None)))
t3 = TreeNode(5, None, None)


s = Solution()
# print(s.traverse_preorder(t3))
# print(s.traverse_preorder(s.mergeTrees(t1,t2)))
print(s.traverse_inorder(s.mergeTrees(t1,t2)))

# print(s.traverse_postorder(s.mergeTrees(t1,t2)))
# s.traverse_bfs(s.mergeTrees(t1,t2))





