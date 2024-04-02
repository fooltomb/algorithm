class Solution:
    def convert(self, s, numRows):#3
        length=len(s)
        res=""
        if length<=numRows or numRows==1:
            return s
        c=(2*numRows-2)#4
        for j in range(numRows):
            for i in range(length//c+1):
                if (i+1)*c-j<length and (i+1)*c-j!=i*c+j and j!=0:
                    res+=s[i*c+j]
                    res+=s[(i+1)*c-j]
                elif i*c+j<length:
                    res+=s[i*c+j]
            #print(res)
        return res


if __name__=="__main__":
        s=Solution()
        print(s.convert("fefaeadefgpgg",3))
