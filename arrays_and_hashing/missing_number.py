"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        # Solution 1
        nums = sorted(nums)
        n = 0
        for i in range(0, len(nums)):
            if n != nums[i]:
                return n
            n+=1
        return n

        # Solution 2 Using Gauss's sum formula from 1 to n: n*(n+1)/2
        # n = len(nums)
        # return n * (n+1) // 2 - sum(nums)

        # Solution 3
        # n = len(nums)
        # return sum(range(n+1)) - sum(nums)


nums = [3,0,1]
# nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))