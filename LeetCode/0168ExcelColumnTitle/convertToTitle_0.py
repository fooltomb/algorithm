class Solution(object):
    def convertToTitle(self,n):
        dict = {1:'A',
                2:'B',
                3:'C',
                4:'D',
                5:'E',
                6:'F',
                7:'G',
                8:'H',
                9:'I',
                10:'J',
                11:'K',
                12:'L',
                13:'M',
                14:'N',
                15:'O',
                16:'P',
                17:'Q',
                18:'R',
                19:'S',
                20:'T',
                21:'U',
                22:'V',
                23:'W',
                24:'X',
                25:'Y',
                26:'Z',
                0:'Z'
                }
        self.res=''
        def DFS(num):
            rest=num%26
            if rest==0:
                self.res+=dict[26]
                num-=26
            else:
                self.res+=dict[rest]
            num=num//26
            if num>1:
                DFS(num)
        DFS(n)
        return self.res[::-1]
if __name__=="__main__":
    s=Solution()
    print s.convertToTitle(701)



