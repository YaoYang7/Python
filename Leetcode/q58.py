class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ') 
        for i in range(len(s) -1, -1, -1):
            if s[i] != '': 
                return len(s[i])
        

if __name__ == "__main__" :
    s = Solution()
    t = "a "
    print(s.lengthOfLastWord(t))