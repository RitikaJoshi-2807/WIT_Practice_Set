class Solution(object):
    def intToRoman(self, num):
        number = {
            1   : "I",
            4   : "IV",
            5   : "V",
            9   : "IX",
            10  : "X",
            40  : "XL",
            50  : "L",
            90  : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }

        
        values = number.keys() #store the key values
        result = []            
# q stores the quotient and num stores the remainder when divided by the keys in reversed order.If quotient is greater than 0 ,temp will store the value present at that key and multiply it with the quotient to get how many sum of it is actually present in the num.

        for val in reversed(values):   
            q, num = divmod(num, val)
            if q > 0:
                temp = [number[val]] * q
                result.extend(temp)
                        
        return ''.join(result)
        
