# Problem: Reverse Integer (LeetCode #7)
# Link: https://leetcode.com/problems/reverse-integer/
# Complexity: Time O(log x), Space O(1)
# Strategy: Reversing the integer mathematically using modulo and integer division. Handles negative values by storing the sign and ensures the result stays within 32-bit signed integer limits.

def reverse(self, x: int) -> int:
    reversed, sign = 0, 1 if x >= 0 else -1
    x = abs(x)
    
    while x > 0:
        reversed = 10 * reversed + x % 10
        x //= 10

    reversed *= sign

    if -2147483648 < reversed < 2147483647:
        return reversed
    return 0
