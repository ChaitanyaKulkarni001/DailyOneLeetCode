# Problem => # Given an array nums of size n, return the majority element. The majority element is the element that appears more
# than ⌊n / 2⌋ times.You may assume that the majority element always exists in the array.

# First Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        def getKey(mydict,value):
            for key,val in mydict.items():
                if val == value:
                    return key
            return None
        # nums= [2,2,1,1,1,2,2]
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1

# Second Solution
def majorityElement(self, nums: List[int]) -> int:
  nums.sort()
  return nums[(len(nums)//2)]
