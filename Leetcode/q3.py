from typing import Optional 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l1 = [] 
        temp = []
        strL = [x for x in s] # splits it into a str list to check for duplicates

        '''strL = ['p', 'w', 'w', 'k', 'e', 'w']'''
        for letter in strL:
            if letter in temp:
                #remove letters till we hit dupe 
                while temp[0] != letter: # while the first element in temp is not equal to the letter
                    temp.remove(temp[0]) # remove the first element in temp
            temp.append(letter) # append the letter to temp list
            ans = len(temp) # length of the temp list is the answer




        # """ l1 =   ['p', 'w', '_', 'k', 'e', '_'] """
        # """remove dupes"""
        # for i in range(len(strL)): 
        #     if strL[i] not in l1:
        #         l1.append(strL[i]) # append the element to the list
        #     else :
        #         l1.append("_") # placeholder for duplicates
        # """L1 now consists of all unique elements"""

        # for _ in l1:
        #     if _ != "_":
        #         ans += 1
        #     if _ == "_":
        #         break
        
        return ans


if __name__ == '__main__':
    t1 = "pwwkew"
    s1 = Solution()
    print (s1.lengthOfLongestSubstring(t1))