# Problem: Subsets (LeetCode #78)
# Link: https://leetcode.com/problems/subsets/

# Complexity: Time O(n * 2^n), Space O(n * 2^n) 
# Strategy: Bitmasking - Iterating from 0 to 2^n - 1, using bitwise operations to represent inclusion/exclusion of each element.

def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)

    subsets = []
    for i in range(2 ** n):
        cur = []
        for k in range(n):
            if (i >> k) & 1: cur.append(nums[k])
        subsets.append(cur)

    return subsets

# Complexity: Time O(n * 2^n), Space O(n) (recursion depth)
# Strategy: Backtracking (Decision Tree) - For each element, we decide whether to include it or not.

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        backtrack(i + 1)

        subset.pop()
        backtrack(i + 1)

    backtrack(0)
    return res