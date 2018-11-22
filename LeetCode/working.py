from Tools.DataType import *
import hasPath_0 as SO

if __name__=="__main__":
    root=stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
    s=SO.Solution()
    print s.hasPathSum(root,18)

