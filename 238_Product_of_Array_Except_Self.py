class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n

        # Step 2: Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Step 3: Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Step 4: Calculate final result using prefix and suffix arrays
        return [prefix[i] * suffix[i] for i in range(n)]
