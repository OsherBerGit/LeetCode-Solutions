# Problem: Roman to Integer (LeetCode #13)
# Link: https://leetcode.com/problems/roman-to-integer/
# Complexity: Time O(n), Space O(1)
# Strategy: Iterate through the string, comparing the current value to the next value. If the current value is smaller, subtract it; otherwise, add it.

def romanToInt(self, s: str) -> int:
    roman_map = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    integer = 0
    
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            integer -= roman_map[s[i]]
        else:
            integer += roman_map[s[i]]
    
    return integer