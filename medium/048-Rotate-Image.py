# Problem: Rotate Image (LeetCode #48)
# Link: https://leetcode.com/problems/rotate-image/
# Complexity: Time O(n²), Space O(1)
# Strategy: Rotating the matrix in-place by first transposing it and then reversing each row.

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] =matrix[i][n - j - 1], matrix[i][j]