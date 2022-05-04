class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        for i in range(len(num)):
            if num[i]=="6":
                # print(i)
                break
        else: 
            return num
        return int(num)+(3*(10**(len(num)-1-i)))
