class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        
        for n in nums:
            if n == val:
                pass
            else:
                nums[k] = n
                k +=1
                
        return k
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
