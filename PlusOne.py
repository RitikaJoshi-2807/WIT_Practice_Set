class Solution(object):
    def plusOne(self, digits):
        sum=0
        for i in range(len(digits)):
            sum+=digits[i]*pow(10, len(digits)-1-i)
        return [int(i) for i in str(sum+1)]
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
