class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        if not root:
            return None

        for i in root.children:
            output.extend(self.postorder(i))

        return output + [root.val]

        # if root is None:
        #     return
        # result=[]
        # stack=[]
        # stack.append(root)
        # while stack:
        #     node=stack.pop()
        #     result.append(node.val)
        #     for i in node.children:
        #         stack.append(i)
        # return result[::-1]

# I learn how to use extend and what is difference between append and extend.
# and the grammar like output + [List]