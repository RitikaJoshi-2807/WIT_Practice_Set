class Solution(object):
    def missingNumber(self, nums):
        new=len(nums)
        for i in range(new+1):
            if i not in nums:
                return i
