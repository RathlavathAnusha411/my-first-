from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            balance = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == balance:
                    return [i, j]
                # Test the code
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(result)
