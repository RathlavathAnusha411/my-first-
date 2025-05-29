from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for a in range(n):
            b = target - nums[a]
            if b in d:
                return [a, d[b]]
            else:
                d[nums[a]] = a
sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)

