from Tools.DataType import *
#import pascalTriangle_0 as SO
from 0222CountCompleteTreeNode.CountCompleteTreeNode import Solution

if __name__=="__main__":
    root=stringToTreeNode("[5,4,8,11,12,13,4,7,2,15,22,7,1]")
    print(root.right.left.right.val)


