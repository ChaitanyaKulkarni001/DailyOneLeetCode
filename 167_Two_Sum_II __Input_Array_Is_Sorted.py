# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1

        while(True):
            res = numbers[i]+numbers[j]
            if (res == target):

                return [i+1,j+1]
            elif (target < res):
                j-=1
            else:
                i+=1
