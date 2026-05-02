# Problem: Find All Numbers Disappeared in an Array (LeetCode #448)
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Complexity: Time O(n), Space O(1) (excluding result list)
# Strategy: In-place marking by negating values at indices corresponding to the numbers present in the array.

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for n in nums:
        index = abs(n) - 1
        nums[index] = -abs(nums[index])
    
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)

    return res