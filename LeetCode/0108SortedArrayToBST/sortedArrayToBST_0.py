class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution(object):
    def sortedArrayToBST(self,nums):
        if nums==[]:
            return None
        root=TreeNode(nums[len(nums)//2])
        def makeTree(rootNode,nums1,nums2):
            if nums1!=[]:
                #print nums1
                mid=len(nums1)//2
                rootNode.left=TreeNode(nums1[mid])
                makeTree(rootNode.left,nums1[:mid],nums1[mid+1:])
            if nums2!=[]:
                mid=len(nums2)//2
                rootNode.right=TreeNode(nums2[mid])
                makeTree(rootNode.right,nums2[:mid],nums2[mid+1:])

        makeTree(root,nums[:len(nums)//2],nums[len(nums)//2+1:])
        return root
if __name__=="__main__":
    nums=[-20,-10,-1,0,1,5,9,10]
    #'''
    s=Solution()
    a=s.sortedArrayToBST(nums)
    print a.val
    print a.left.val,a.right.val
    print a.left.left.val,a.left.right.val,a.right.left.val,a.right.right.val
    print a.left.left.left.val
    #'''
