from typing import List

# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         ans = []
#         def convertToBinRep(arr):
#             b = []
#             for i in range(len(arr)):
#                 b.append(bin(arr[i])[2:]) # remove '0b' prefix from binary rep 
#             return b
#         arrBinRep = convertToBinRep(arr) # array now contains the bit rep of each element 

#         for q in queries:
#             l, r = q[0], q[1] # left and right indices of the query
#             xor = 0 
#             for i in range(l, r+1): # xor of the subarray
#                 xor ^= int(arrBinRep[i], 2) # convert binary rep to int
#             ans.append(xor)

#         return ans




"""Optimized by chatGPT"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Compute prefix XOR array
        prefixXOR = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer the queries using the prefix XOR array
        ans = []
        for l, r in queries:
            ans.append(prefixXOR[r + 1] ^ prefixXOR[l])
        
        return ans

if __name__ == "__main__":
    arr = [4,8,2,10]
    queries = [[2,3],[1,3],[0,0],[0,3]]
    print(Solution().xorQueries(arr, queries)) 