# Problem: Climbing Stairs (LeetCode #70)
# Link: https://leetcode.com/problems/climbing-stairs/
# Complexity: Time O(n), Space O(1)
# Strategy: Dynamic Programming (Bottom-up) with space optimization, calculating the N-th Fibonacci number.

def climbStairs(self, n: int) -> int:
    if n <= 1: return 1
    prev1, prev2 = 1, 1

    for _ in range(2, n + 1):
        prev1, prev2 = prev1 + prev2, prev1

    return prev1