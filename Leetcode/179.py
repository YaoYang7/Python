from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = nums.sort()
        currentH = {"Highest":0}
        for i in range(len(nums)-1):
            x = str(nums[i])
            x = int(x[0])
            y = currentH["Highest"]
            if x > y: 
                currentH["Highest"] = nums[i]


if __name__ == "__main__":
    s = Solution()
    t = s.largestNumber([3,30,34,5,9])
    print(t)