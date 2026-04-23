# Problem: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/
# Complexity: Time O(n), Space O(n)
# Strategy: Using a Hash Map for O(1) lookups.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i