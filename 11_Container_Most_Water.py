class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        i = 0
        j= size-1   
        
        depth = size-1
        allAreas = []
        while (i<j):
            water =  depth * min(height[i],height[j])
            allAreas.append(water)
            if min(height[i],height[j]) == height[i]:
                i+=1
            else:
                j-=1
            depth-=1
        # print(allAreas)
        return max(allAreas)
