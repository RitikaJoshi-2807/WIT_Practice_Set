class Solution(object):
    def search(self, nums, target):
        lower = 0
        upper = len(nums)
    
        while lower<upper:
            mid = int((lower+upper)/2) 
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  
                upper-= 1
            else:
                lower += 1
        return -1
