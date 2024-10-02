from typing import Optional 

'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = [x for x in x] 
        l2 = [ x for x in x[::-1]] # reverse the list
        ans = False

        #all negative numbers can not be palindrome
        for i in range(len(l)):
            if l[i] != l2[i]:
                ans = False
                break # break the loop since we already know the answer
            else:
                ans = True 
        return ans

if __name__ == "__main__":
    s = Solution()'''

""" Improved Solution """
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = [x for x in x] 
        l2 = [ x for x in x[::-1]]

        return l == l2 # return True if the list is the same

if __name__ == "__main__":
    s = Solution()