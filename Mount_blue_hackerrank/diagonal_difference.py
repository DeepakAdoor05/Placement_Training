def diagonalDifference(arr):
    count = 0
    primary_diagonal = secondary_diagonal = 0
    for i in arr:
        primary_diagonal += i[count]
        secondary_diagonal += i[len(i)-count-1]
        count += 1
    diagonal = primary_diagonal - secondary_diagonal
    return abs(diagonal)


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(diagonalDifference(arr))

# Sample Input
# STDIN      Function
# -----      --------
# 3           arr[][] sizes n = 3, m = 3
# 11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# 4 5 6
# 10 8 -12

# Sample Output
# 15