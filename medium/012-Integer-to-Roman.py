# Problem: Integer to Roman (LeetCode #12)
# Link: https://leetcode.com/problems/integer-to-roman/
# Complexity: Time O(1), Space O(1)
# Strategy: Greedy approach using a list of tuples (value, symbol) sorted from largest to smallest.

def intToRoman(self, num: int) -> str:
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    roman = []
    for value, symbol in roman_map:
        if num == 0: break
        count = num // value
        roman.append(symbol * count)
        num -= value * count
    
    return "".join(roman)