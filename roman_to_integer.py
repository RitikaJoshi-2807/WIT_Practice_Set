class Solution(object):
    def romanToInt(self, s):
        number = {
            "I": "1",
            "V": "5",
            "X": "10",
            "L": "50",
            "C": "100",
            "D": "500",
            "M": "1000"
        }
        '''
   Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.'''   
        num=0
        if 'IV' in s:
            num += 4
            s = s.replace('IV','')
        if 'IX' in s:
            num += 9
            s = s.replace('IX','')
        if 'XL' in s:
            num += 40
            s = s.replace('XL','')
        if 'XC' in s:
            num += 90
            s = s.replace('XC','')
        if 'CD' in s:
            num += 400
            s = s.replace('CD','')
        if 'CM' in s:
            num += 900
            s = s.replace('CM','')
        print(s)
        for element in s: 
            num += int(number.get(element))
        return num
     
        
