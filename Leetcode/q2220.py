from typing import Optional 

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flipCounter = 0 

        def intToBinary(n: int) -> str:
            return bin(n)[2:] # returns binary representation of n, [2:] to remove '0b' prefix
        
        startBin = intToBinary(start)
        goalBin = intToBinary(goal)

        startBinL = [x for x in startBin]
        goalBinL = [x for x in goalBin] 

        # if the start is less than goal (in binary terms) 
        if len(startBinL) < len(goalBinL):
            _ = len(goalBinL) - len(startBinL) #temp count
            # insert it into the start 
            for i in range(_): 
                startBinL.insert(0, '0') # insert the binary representation of 0 to the startBinL list
        # if the goal is less than start (in binary terms)
        elif len(goalBinL) < len(startBinL):
            _ = len(startBinL) - len(goalBinL)
            # insert it into the goal
            for i in range(_): 
                goalBinL.insert(0, '0')

        # loop through the startBinL list
        for i in range(len(startBinL)): 
            # if the startBinL[i] is not equal to goalBinL[i]
            if startBinL[i] != goalBinL[i]:
                flipCounter += 1
                print (f"startBinL[{i}]: {startBinL[i]} != goalBinL[{i}]: {goalBinL[i]}")

        return flipCounter 
    
if __name__ == '__main__':
    start = 222
    goal = 3
    s = Solution()
    print (s.minBitFlips(start, goal))
    
'''
Does not need to convert it fully since it only requires to count the amount of bits that need to be flipped
'''