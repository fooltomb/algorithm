class Solution:
    def hanxin(self,rowNums):
        """
        rowNums是个三维数组[a,b,c]
        a表示3人一排时队尾的人数
        b表示5人一排时队尾的人数
        c表示7人一排时队尾的人数
        """
        #已知总人数不少于10不超过100
        for i in range(10,100):
            if i%3==rowNums[0]:
                if i%5==rowNums[1]:
                    if i%7==rowNums[2]:
                        return i
        return "No answer"
if __name__=="__main__":
    s=Solution()
    print(s.hanxin([2,1,6]))
    print(s.hanxin([2,1,3]))