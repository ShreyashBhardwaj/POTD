"""
Given a matrix mat[][] of size n × m and an integer x, find the number of square submatrices whose sum of elements is equal to x.

Examples:

Input: mat[][] = [[2, 4, 7, 8, 10],
               [3, 1, 1, 1, 1],
               [9, 11, 1, 2, 1],
               [12, -17, 1, 1, 1]] ,
x = 10
Output: 3
Explanation: The sub-squares whose sum of elements = 10, are colored in the matrix.

Input: mat[][] = [[3, 3, 5, 3],
               [2, 2, 2, 6],
               [11, 2, 2, 4]] ,
x = 1
Output: 0
Explanation: There is no sub-squares whose sum of elements is 1.
"""

class Solution:
    def countSquare(self, mat, x):
        rows = len(mat)
        cols = len(mat[0])

        # Initialize prefix matrix with 0s
        prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        ans = 0

        # ==========================================
        # STEP 1: Build the 2D Prefix Sum Matrix
        # ==========================================
        for i in range(rows):
            for j in range(cols):
                current_val = mat[i][j]

                # Look at the PREFIX matrix to get the accumulated areas
                top_area = prefix[i - 1][j] if i > 0 else 0
                left_area = prefix[i][j - 1] if j > 0 else 0
                top_left_area = prefix[i - 1][j - 1] if (i > 0 and j > 0) else 0

                # Formula to build: Add above, add left, subtract overlap, add current cell
                prefix[i][j] = current_val + top_area + left_area - top_left_area

        # ==========================================
        # STEP 2: Find all squares that sum to x
        # ==========================================
        for i in range(rows):
            for j in range(cols):
                maxL = min(rows - i, cols - j)

                for L in range(1, maxL + 1):
                    r2 = i + L - 1
                    c2 = j + L - 1

                    # Grab the chunks to subtract to isolate our square
                    top_area = prefix[i - 1][c2] if i > 0 else 0
                    left_area = prefix[r2][j - 1] if j > 0 else 0
                    top_left_area = prefix[i - 1][j - 1] if (i > 0 and j > 0) else 0

                    # Formula to evaluate a specific submatrix
                    square_sum = prefix[r2][c2] - top_area - left_area + top_left_area

                    if square_sum == x:
                        ans += 1

        return ans

sol = Solution()

print(sol.countSquare([[2, 4, 7, 8, 10],
                       [3, 1, 1, 1, 1],
                       [9, 11, 1, 2, 1],
                       [12, -17, 1, 1, 1]],10))

print(sol.countSquare([[3, 3, 5, 3],
               [2, 2, 2, 6],
               [11, 2, 2, 4]],1))
