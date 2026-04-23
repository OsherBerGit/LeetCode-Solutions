# Problem: Palindrome Number (LeetCode #9)
# Link: https://leetcode.com/problems/palindrome-number/
# Complexity: Time O(log n), Space O(1)
# Strategy: Reversing the integer mathematically digit-by-digit using modulo, avoiding extra memory from string conversion.

def isPalindrome(self, x: int) -> bool:
    temp = x
    reveresed = 0

    while temp > 0:
        reveresed = 10 * reveresed + temp % 10
        temp //= 10
    
    return reveresed == x