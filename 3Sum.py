class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        last = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            le, ri = i + 1, n - 1

            while le < ri:
                total = nums[i] + nums[le] + nums[ri]

                if total == 0:
                    last.append([nums[i], nums[le], nums[ri]])
                    while le < ri and nums[le] == nums[le + 1]:
                        le += 1
                    while le < ri and nums[ri] == nums[ri - 1]:
                        ri -= 1
                    le += 1
                    ri -= 1
                elif total < 0:
                    le += 1
                else:
                    ri -= 1
        return last
