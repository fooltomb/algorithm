class Solution:
    def convert(self, s, numRows):#3
        length=len(s)
        res=""
        if length<=numRows or numRows==1:
            return s
        c=(2*numRows-2)#4
        r=length%c#1
        array=[]
        for i in range(length/c):
            res+=s[i*c]
            array.append(i*c)
        if r>0:
            array.append(length-r)
            res+=s[length-r]
            
        if numRows>2:
            for i in range(0,numRows-2):
                res+=s[i]
                for j in array:
                    res+=s[j+c-i]
            
        for i in range(length/c):
            res+=s[i*c+numRows-1]        
        
        print(res)
        return res


if __name__=="__main__":
        s=Solution()
        s.convert("fefaeadef",3)
