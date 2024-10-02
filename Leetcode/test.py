from typing import Optional, List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = 200 # given 
        minLen2 = 200 
        maxLen = 0
        ans = ""
        minStr = None
        minStr2 = None

        # gets the shortest string in the list
        for str_ in strs:
            if len(str_) < minLen:
                minLen = len(str_)
                minStr = str_
        strs.remove(minStr) # remove the shortest string from the list

        # gets the second shortest string in the list
        for str_ in strs:
            if len(str_) < minLen2:
                minLen2 = len(str_)
                minStr2 = str_
        if minStr2 != None or minStr2 != "":
            strs.remove(minStr2) # remove the shortest string from the list

        # finding the longest between the two shortest strings
        for i in range(len(minStr)):
            if minStr2 != None and minStr[i] == minStr2[i]:
                ans += minStr[i] 

        # gets the longest string in the list
        for str_ in strs:
            if len(str_) > maxLen:
                maxLen = len(str_)
                maxStr = str_
        
        # compare against the largest string 
        for i in range(len(ans)-1, 0, -1): #start, stop, step
            if ans[i] != maxStr[i]: # first letter is different, no common prefix across all strings
                #remove the letter
                ans = ans[:-1]
                
        return ans


if __name__ == "__main__" :
    s = Solution() 
    print(s.longestCommonPrefix(["flower","flow","flight"])) # "fl"