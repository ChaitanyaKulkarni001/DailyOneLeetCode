class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <=1:
            return  intervals
        intervals.sort()
        Output = [intervals[0]]
        
        # Output = [intervals[0]]
        for i in range(1,len(intervals)):
            current = intervals[i]
            previous = Output[-1]

            # merged = Output[-1]
            if current[0]<=previous[1]:
                Output[-1] = ([previous[0],max(previous[1],current[1])])
            else:
                Output.append(current)

        return Output
