class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
    
        # now = nums[0]
        currentIndex = 0
        
        while currentIndex< len(nums)-1:
            if currentIndex+nums[currentIndex] >= len(nums)-1:
                count+=1
                break
            # target = nums[-1]
            # print("Upper i can go",iCanGo)
            # iCanGo = [nums[currentIndex+i] for i in range(1,nums[currentIndex]+1)]
            # iCanGoIndex = [currentIndex+i for i in range(1,nums[currentIndex]+1)]
            maxR = 0
            nextIndex =0
            for i in range(1,nums[currentIndex]+1):
                if currentIndex+i<=len(nums)-1 and currentIndex+i+nums[currentIndex+i]>maxR:
                    maxR = currentIndex+i+nums[currentIndex+i]
                    nextIndex = currentIndex +i
            currentIndex= nextIndex
            # step = max(iCanGo)
            # print(step,"Step")
            # print("I can go ",iCanGo)
            # print("I can go index",iCanGoIndex)
            # currentIndex += nums.index(step) 
            
            # nums.remove(step)
            count+=1
            # print(iCanGo)
            # print(iCanGoIndex)
        # print("the count is ",count)
        return count
