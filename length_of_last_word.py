class Solution(object):
    def lengthOfLastWord(self, s):
        new=s.split()
        return len(new[-1])
        """
        :type s: str
        :rtype: int
        """
