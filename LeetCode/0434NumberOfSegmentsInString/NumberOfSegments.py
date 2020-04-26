class Solution:
    def countSegments(self, s: str) -> int:
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count

if __name__=="__main__":
    s=Solution()
    print(s.countSegments(" hello's "))
