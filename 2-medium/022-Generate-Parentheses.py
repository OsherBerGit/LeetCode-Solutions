# Problem: Generate Parentheses (LeetCode #22)
# Link: https://leetcode.com/problems/generate-parentheses/
# Complexity: Time O(4^n / sqrt(n)), Space O(n) (recursion depth)
# Strategy: Backtracking by maintaining counts of open and closed parentheses. 

def generateParenthesis(self, n: int) -> List[str]:
    res = []

    def backtrack(S, open_count, close_count):
        if len(S) == 2 * n:
            res.append(S)
            return

        if open_count < n:
            backtrack(S + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(S + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res