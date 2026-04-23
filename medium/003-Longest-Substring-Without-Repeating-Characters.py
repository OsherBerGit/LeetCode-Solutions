# Problem: Longest Substring Without Repeating Characters (LeetCode #3)
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Complexity: Time O(n), Space O(min(n, m))
# Strategy: Sliding Window approach using two pointers and a HashSet to dynamically track unique characters.

def lengthOfLongestSubstring(self, s: str) -> int:
    visitedChar = set()
    right, left = 0, 0
    maxLen = 0

    for right in range(len(s)):
        while s[right] in visitedChar:
            visitedChar.remove(s[left])
            left += 1
        visitedChar.add(s[right])
        maxLen = max(maxLen, right - left + 1)
    
    return maxLen