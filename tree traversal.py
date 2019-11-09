# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def creatTree(A,root,i,n):
    if i<n:
        tmp = TreeNode(A[i])
        root = tmp
        root.left = creatTree(A,root.left,2*i+1,n)
        root.right = creatTree(A,root.right,2*i+2,n)
    return root

def inorderTraversal(root):
        if root:

            if root.val != None:
                print(root.val,end=" ")
            inorderTraversal(root.left)
            inorderTraversal(root.right)
def preorderTraversal(root):
        if root:
            if root.val != None:
                print(root.val,end=" ")
            preorderTraversal(root.right)
            preorderTraversal(root.left)
#
if __name__ == '__main__':
    A = [1,None,2,3]
    root = None
    root = creatTree(A,root,0,A.__len__())
    inorderTraversal(root)
    print(" ")
    preorderTraversal(root)


