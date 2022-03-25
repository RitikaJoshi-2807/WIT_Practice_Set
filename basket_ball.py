class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for value in ops:
            if value == "C":        #It will remove the last item from list 
                record.pop()
            elif value == "+":         # It will append the sum of last two items in the list
                record.append(record[-1] + record[-2])
            elif value == "D":          #It will append the product of last item to 2  in the list
                record.append(2*record[-1])
            else:                       # It will add the integer value to the list
                record.append(int(value))
        return sum(record)
