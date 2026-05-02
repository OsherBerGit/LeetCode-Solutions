# Problem: Find Peak Element (LeetCode #162)
# Link: https://leetcode.com/problems/find-peak-element/
# Complexity: Time O(log n), Space O(1)
# Strategy: Binary Search on a "mountain slope" logic. By comparing mid to mid+1, we determine which half is guaranteed to contain a peak.

def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left