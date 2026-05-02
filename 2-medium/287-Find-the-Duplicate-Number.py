# Problem: Find the Duplicate Number (LeetCode #287)
# Link: https://leetcode.com/problems/find-the-duplicate-number/
# Complexity: Time O(n), Space O(1)
# Strategy: Floyd's Cycle Finding Algorithm (Tortoise and Hare) to detect the duplicate as the entrance of a cycle in an array-based linked list.

def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow