class Solution:
    def maxArea(self, height: List[int]) -> int:
        new=0
        lower=0
        upper=len(height)-1
        while lower<upper:
            area=(upper-lower)*min(height[lower],height[upper])
            if height[lower]<height[upper]:
                lower+=1
            else:
                upper-=1
            new=max(new,area)
        return new
        
