# Problem: Pow(x, n) (LeetCode #50)
# Link: https://leetcode.com/problems/powx-n/
# Complexity: Time O(log n), Space O(1)
# Strategy: Binary Exponentiation (Fast Power) algorithm. Squaring the base and halving the exponent at each step to reach logarithmic time complexity.

def myPow(self, x: float, n: int) -> float:
    isPositive = True if n > 0 else False
    n = abs(n)

    res = 1
    cur = x
    while n > 0:
        if n % 2 != 0: res *= cur
        cur *= cur
        n //= 2
    
    return res if isPositive else 1 / res