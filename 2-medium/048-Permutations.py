# Problem: Permutations (LeetCode #46)
# Link: https://leetcode.com/problems/permutations/
# Complexity: Time O(n * n!), Space O(n!) 
# Strategy: Backtracking using in-place swapping to generate all possible arrangements without extra space for tracking visited elements.

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)

    def backtrack(first):
        if first == n:
            res.append(nums.copy())
            return

        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack(0)
    return res