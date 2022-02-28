class Solution(object):
    def addBinary(self, a, b):
        a = int(a, base=2)
        b = int(b, base=2)
        result = bin(a+b)
        return result[2:]
