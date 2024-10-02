from typing import Optional, List

class Solution: #Vertical scanning
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            minLen = 200
            # gets the shortest string in the list
            for str_ in strs:
                if len(str_) < minLen:
                    minLen = len(str_)
                    minStr = str_
            # compare against all strings / vertical scanning 
            for i in range(minLen):
                for str_ in strs:
                    if i == len(str_) or str_[i] != minStr[i]:
                        return minStr[:i]
            return minStr


if __name__ == "__main__" :
    s = Solution() 
    print(s.longestCommonPrefix(["ab", "a"]))










# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         minLen = 200 # given 
#         minLen2 = 200 
#         maxLen = 0
#         ans = ""
#         minStr = None
#         minStr2 = None
#         maxStr = None

#         if len(strs) == 0:
#             return ans
#         if len(strs) == 1:
#             return strs[0]

#         # gets the shortest string in the list
#         for str_ in strs:
#             if len(str_) < minLen:
#                 minLen = len(str_)
#                 minStr = str_ 
#         strs.remove(minStr) # remove the shortest string from the list

#         # gets the second shortest string in the list
#         for str_ in strs:
#             if len(str_) < minLen2:
#                 minLen2 = len(str_)
#                 minStr2 = str_
#         if minStr2 != None and minStr2 != "":
#             strs.remove(minStr2) # remove the shortest string from the list

#         # finding the longest between the two shortest strings
#         for i in range(len(minStr)):
#             if minStr2 != None and minStr[i] == minStr2[i]:
#                 ans += minStr[i] 
#             else:
#                 break

#         # gets the longest string in the list
#         for str_ in strs:
#             if len(str_) > maxLen:
#                 maxLen = len(str_)
#                 maxStr = str_
#         if ans != "" and (maxStr != None or maxStr[0] != ans[0]):
#             return ""
        
#         # compare against the largest string 
#         for i in range(len(ans)-1, 0, -1): #start, stop, step
#             if ans[i] != maxStr[i]: # first letter is different, no common prefix across all strings
#                 #remove the letter
#                 ans = ans[:-1]
                
#         return ans
