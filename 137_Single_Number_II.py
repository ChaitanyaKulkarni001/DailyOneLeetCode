class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = {}
        for i in range(len(nums)):
            if nums[i] in number.keys():
                number[nums[i]] += 1
            else:
                number[nums[i]] = 1
        # print(number)
        return list(number.keys())[list(number.values()).index(1)]
