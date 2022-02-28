class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        for i,j in enumerate(nums):
            res1=(target-j)
            if res1 in nums:
                if i!= nums.index(res1):
                    res.append(i)
                    res.append(nums.index(res1))
                    return res
