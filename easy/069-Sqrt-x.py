# Problem: Sqrt(x) (LeetCode #69)
# Link: https://leetcode.com/problems/sqrtx/
# Complexity: Time O(log x), Space O(1)
# Strategy: Applying Binary Search on the range [0, x] to efficiently find the largest integer where mid * mid <= x.

def mySqrt(self, x: int) -> int:
    low, high = 0, x
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans