from typing import List 
'''Solution using HashMap'''
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        pass
        # using java hashmap 

if __name__ == "__main__" :
    s = Solution()
    print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))

'''Solution does not work for repeated words in the same string'''
# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         # done using vertical scanning
#         if len(s1) == 0: 
#             return s2 #all in s2 are uncommon since s1 doesn't exist 
#         elif len(s2) == 0:
#             return s1 #all in s1 are uncommon since s2 doesn't exist

#         u_words = []
#         # put it in an array 
#         s1 = s1.split(" ")  # get words in s1
#         s2 = s2.split(" ")  # get words in s2

#         if len(s1) < len(s2): 
#             """s1 shortest"""
#             for i in range(len(s1)):
#                 if s1[i] != s2[i]: # if the words are not the same
#                     u_words.append(s1[i])
#                     u_words.append(s2[i]) 

#             for i in range(len(s2)-1, len(s1), -1):
#                 u_words.append(s2[i])

#         else:
#             """s2 shortest"""
#             for i in range(len(s2)):
#                 if s1[i] != s2[i]: # if the words are not the same
#                     u_words.append(s1[i]) 
#                     u_words.append(s2[i]) 

#             for i in range(len(s1)-1, len(s2), -1) :
#                 u_words.append(s1[i])

#         return u_words