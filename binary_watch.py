class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type num: int
        :rtype: List[str]      
        
        """
        #%d means an integer
        #: is a :
        #%02d means an integer, left padded with zeros up to 2 digits.
        return ['%d:%02d' % (h, m)       
                  for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn]
