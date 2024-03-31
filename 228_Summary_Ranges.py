class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length =len(nums)
        final=[]
        i=0
        flag=0
        while i < length:
            pair = [nums[i]]
            while i < length - 1 and nums[i + 1] == nums[i] + 1:
                pair.append(nums[i + 1])
                i += 1
            final.append(pair)
            i += 1
        output = []
        for pair in final:
            if len(pair) == 1:
                output.append(str(pair[0]))
            else:
                output.append(str(pair[0]) + "->" + str(pair[-1]))
        return output
                
