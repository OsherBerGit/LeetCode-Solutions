# Problem: Plus One (LeetCode #66)
# Link: https://leetcode.com/problems/plus-one/
# Complexity: Time O(n), Space O(1)
# Strategy: Traversing the array from right to left, managing the carry. Using in-place modification to optimize space.

def plusOne(self, digits: List[int]) -> List[int]:
    digit = len(digits) - 1
    carry = 1

    while carry != 0 and digit >= 0:
        digits[digit] += carry
        carry, digits[digit] = digits[digit] // 10, digits[digit] % 10
        digit -= 1
    
    if carry != 0:
        digits.insert(0, carry)

    return digits