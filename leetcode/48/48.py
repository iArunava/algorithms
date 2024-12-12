class Solution:
    def rotate(matrix):
        n=len(matrix)
        for mn in range(n // 2):
            mx = n - mn - 1
            for i in range(mn, mx):
                offset = i - mn
                top = matrix[mn][i]
                matrix[mn][i] = matrix[mx - offset][mn]
                matrix[mx - offset][mn] = matrix[mx][mx-offset]
                matrix[mx][mx-offset] = matrix[i][mx]
                matrix[i][mx] = top
