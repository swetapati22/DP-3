# Time Complexity :
- O(n^2), where n is the number of rows/columns in the matrix

# Space Complexity :
- O(1), in-place DP (modifying input matrix)

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(n - 2, -1, -1):
            for j in range(n):
                left = matrix[i + 1][j - 1] if j > 0 else float('inf')
                down = matrix[i + 1][j]
                right = matrix[i + 1][j + 1] if j < n - 1 else float('inf')
                matrix[i][j] += min(left, down, right)

        return min(matrix[0])
