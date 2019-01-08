class Sulotion(object):
    def invertTree(self,root):
        def DFS(root):
            if root!=None:
                root.left,root.right=root.right,root.left
                DFS(root.left)
                DFS(root.right)
        def(root)
        return root
