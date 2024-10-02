from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        currentH = {"Highest":0}
        x = str(nums[0])
        x = int(x)
        print(type(x)) 
        print("__")
        y = currentH["Highest"]
        print(type(y))

        if x > y:
            print ("AA")

        # if x[0] > currentH["Highest"]: 
        #     print("A")


if __name__ == "__main__":
    s = Solution()
    t = s.largestNumber([3,30,34,5,9])
    print(t)