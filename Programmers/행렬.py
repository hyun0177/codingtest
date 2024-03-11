"""
A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12], [13, 14]]

result = [ [ 0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            result[i][j] += A[i][k] * B[k][j]

print(result)
"""

""" 다른 사람 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
"""

# zip(*B) B가 2차배열일 경우 열이 아닌 행의 첫부분을 묶어서 가져와준다. 알아두면 좋을 것 같다.
